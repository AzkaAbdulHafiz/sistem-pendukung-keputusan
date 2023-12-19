
from http import HTTPStatus
from flask import Flask, request, abort
from flask_restful import Resource, Api 
from models import Baju as ModelBaju
from engine import engine
from sqlalchemy import select
from sqlalchemy.orm import Session

session = Session(engine)

app = Flask(__name__)
api = Api(app)        

class BaseMethod():

    def __init__(self):
        self.raw_weight = {'Bahan': 5, 'Aktivitas': 5, 'Harga': 5, 'Cuaca': 5, 'Panjang_Lengan': 5}

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {k: round(v/total_weight, 2) for k, v in self.raw_weight.items()}

    @property
    def data(self):
        query = select(ModelBaju.No, ModelBaju.Tipe_Kain, ModelBaju.Bahan, ModelBaju.Aktivitas, ModelBaju.Harga, ModelBaju.Cuaca, ModelBaju.Panjang_Lengan)
        result = session.execute(query).fetchall()
        print(result)
        return [{'No': Data_PemilihanBaju.No, 'Tipe_Kain': Data_PemilihanBaju.Tipe_Kain, 'Bahan': Data_PemilihanBaju.Bahan, 'Aktivitas': Data_PemilihanBaju.Aktivitas, 'Harga': Data_PemilihanBaju.Harga, 'Cuaca': Data_PemilihanBaju.Cuaca, 'Panjang_Lengan': Data_PemilihanBaju.Panjang_Lengan} for Data_PemilihanBaju in result]

    @property
    def normalized_data(self):
        Bahan_values = []
        Aktivitas_values = []
        Harga_values = []
        Cuaca_values = []
        Panjang_Lengan_values = []

        for data in self.data:
            Bahan_values.append(data['Bahan'])
            Aktivitas_values.append(data['Aktivitas'])
            Harga_values.append(data['Harga'])
            Cuaca_values.append(data['Cuaca'])
            Panjang_Lengan_values.append(data['Panjang_Lengan'])

        return [
            {'No': data['No'],
             'Tipe_Kain': data['Tipe_Kain'],
             'Bahan': data['Bahan'] / max(Bahan_values),
             'Aktivitas': data['Aktivitas'] / max(Aktivitas_values),
             'Harga': min(Harga_values) / data['Harga'],
             'Cuaca': data['Cuaca'] / max(Cuaca_values),
             'Panjang_Lengan': data['Panjang_Lengan'] / max(Panjang_Lengan_values)
             }
            for data in self.data
        ]

    def update_weights(self, new_weights):
        self.raw_weight = new_weights

class WeightedProductCalculator(BaseMethod):
    def update_weights(self, new_weights):
        self.raw_weight = new_weights

    @property
    def calculate(self):
        normalized_data = self.normalized_data
        produk = []

        for row in normalized_data:
            product_score = (
                row['Bahan'] ** self.raw_weight['Bahan'] *
                row['Aktivitas'] ** self.raw_weight['Aktivitas'] *
                row['Harga'] ** self.raw_weight['Harga'] *
                row['Cuaca'] ** self.raw_weight['Cuaca'] *
                row['Panjang_Lengan'] ** self.raw_weight['Panjang_Lengan'] 
            )

            produk.append({
                'No': row['No'],
                'produk': product_score
            })

        sorted_produk = sorted(produk, key=lambda x: x['produk'], reverse=True)

        sorted_data = []

        for product in sorted_produk:
            sorted_data.append({
                'No': product['No'],
                'score': product['produk']
            })

        return sorted_data


class WeightedProduct(Resource):
    def get(self):
        calculator = WeightedProductCalculator()
        result = calculator.calculate
        return result, HTTPStatus.OK.value
    
    def post(self):
        new_weights = request.get_json()
        calculator = WeightedProductCalculator()
        calculator.update_weights(new_weights)
        result = calculator.calculate
        return {'data': result}, HTTPStatus.OK.value
    

class SimpleAdditiveWeightingCalculator(BaseMethod):
    @property
    def calculate(self):
        weight = self.weight
        result = {row['No']:
                  round(row['Bahan'] * weight['Bahan'] +
                        row['Aktivitas'] * weight['Aktivitas'] +
                        row['Harga'] * weight['Harga'] +
                        row['Cuaca'] * weight['Cuaca'] +
                        row['Panjang_Lengan'] * weight['Panjang_Lengan'], 2)
                  for row in self.normalized_data
                  }
        sorted_result = dict(
            sorted(result.items(), key=lambda x: x[1], reverse=True))
        return sorted_result

    def update_weights(self, new_weights):
        self.raw_weight = new_weights

class SimpleAdditiveWeighting(Resource):
    def get(self):
        saw = SimpleAdditiveWeightingCalculator()
        result = saw.calculate
        return result, HTTPStatus.OK.value

    def post(self):
        new_weights = request.get_json()
        saw = SimpleAdditiveWeightingCalculator()
        saw.update_weights(new_weights)
        result = saw.calculate
        return {'data': result}, HTTPStatus.OK.value


class Baju(Resource):
    def get_paginated_result(self, url, list, args):
        page_size = int(args.get('page_size', 10))
        page = int(args.get('page', 1))
        page_count = int((len(list) + page_size - 1) / page_size)
        start = (page - 1) * page_size
        end = min(start + page_size, len(list))

        if page < page_count:
            next_page = f'{url}?page={page+1}&page_size={page_size}'
        else:
            next_page = None
        if page > 1:
            prev_page = f'{url}?page={page-1}&page_size={page_size}'
        else:
            prev_page = None
        
        if page > page_count or page < 1:
            abort(404, description=f'Halaman {page} tidak ditemukan.') 
        return {
            'page': page, 
            'page_size': page_size,
            'next': next_page, 
            'prev': prev_page,
            'Results': list[start:end]
        }

    def get(self):
        query = select(ModelBaju)
        data = [{'No': Data_PemilihanBaju.No, 'Tipe_Kain': Data_PemilihanBaju.Tipe_Kain, 'Bahan': Data_PemilihanBaju.Bahan, 'Aktivitas': Data_PemilihanBaju.Aktivitas, 'Harga': Data_PemilihanBaju.Harga, 'Cuaca': Data_PemilihanBaju.Cuaca, 'Panjang_Lengan': Data_PemilihanBaju.Panjang_Lengan} for Data_PemilihanBaju in session.scalars(query)]
        return self.get_paginated_result('Data_PemilihanBaju/', data, request.args), HTTPStatus.OK.value


api.add_resource(Baju, '/Data_PemilihanBaju')
api.add_resource(WeightedProduct, '/wp')
api.add_resource(SimpleAdditiveWeighting, '/saw')

if __name__ == '__main__':
    app.run(port='5005', debug=True)
