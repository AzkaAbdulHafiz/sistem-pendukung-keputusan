PGDMP      "                {            pemilihan_baju    16.0    16.0 	    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    24773    pemilihan_baju    DATABASE     �   CREATE DATABASE pemilihan_baju WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Indonesia.1252';
    DROP DATABASE pemilihan_baju;
                postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
                pg_database_owner    false            �           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                   pg_database_owner    false    4            �            1259    24774    Data_PemilihanBaju    TABLE     �   CREATE TABLE public."Data_PemilihanBaju" (
    "No" character varying NOT NULL,
    "Tipe_Kain" character varying,
    "Bahan" integer,
    "Aktivitas" integer,
    "Harga" integer,
    "Cuaca" integer,
    "Panjang_Lengan" integer
);
 (   DROP TABLE public."Data_PemilihanBaju";
       public         heap    postgres    false    4            �          0    24774    Data_PemilihanBaju 
   TABLE DATA           {   COPY public."Data_PemilihanBaju" ("No", "Tipe_Kain", "Bahan", "Aktivitas", "Harga", "Cuaca", "Panjang_Lengan") FROM stdin;
    public          postgres    false    215   �       P           2606    24866 *   Data_PemilihanBaju Data_PemilihanBaju_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public."Data_PemilihanBaju"
    ADD CONSTRAINT "Data_PemilihanBaju_pkey" PRIMARY KEY ("No");
 X   ALTER TABLE ONLY public."Data_PemilihanBaju" DROP CONSTRAINT "Data_PemilihanBaju_pkey";
       public            postgres    false    215            �   �   x�M���0E��AI[��KEba����B*�T�>NS�۱s�삋Pk,}�`b�^"W4�Bu�����%�5�L�R�¡^�I�"*#�Lkl%��$�q6mЍipE��m��.�Qwx��~��������
�>��O�T���c���=� �7 j-�     