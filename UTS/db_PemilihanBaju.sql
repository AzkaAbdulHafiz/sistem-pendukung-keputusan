PGDMP      5            	    {            db_PemilihanBaju    16.0    16.0     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16398    db_PemilihanBaju    DATABASE     �   CREATE DATABASE "db_PemilihanBaju" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Indonesia.1252';
 "   DROP DATABASE "db_PemilihanBaju";
                postgres    false            �            1259    16399    Data_PemilihanBaju    TABLE     �   CREATE TABLE public."Data_PemilihanBaju" (
    "No" integer NOT NULL,
    "Tipe_Kain" text,
    "Bahan" text,
    "Aktivitas" text,
    "Harga" integer,
    "Cuaca" text,
    "Panjang_Lengan" text
);
 (   DROP TABLE public."Data_PemilihanBaju";
       public         heap    postgres    false            �          0    16399    Data_PemilihanBaju 
   TABLE DATA           {   COPY public."Data_PemilihanBaju" ("No", "Tipe_Kain", "Bahan", "Aktivitas", "Harga", "Cuaca", "Panjang_Lengan") FROM stdin;
    public          postgres    false    215   k                  2606    16405 *   Data_PemilihanBaju Data_PemilihanBaju_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public."Data_PemilihanBaju"
    ADD CONSTRAINT "Data_PemilihanBaju_pkey" PRIMARY KEY ("No");
 X   ALTER TABLE ONLY public."Data_PemilihanBaju" DROP CONSTRAINT "Data_PemilihanBaju_pkey";
       public            postgres    false    215            �   �   x�m�AN�0E�ߧ�(eYQu�� ��f�N�I�I������i���x����q���}��I�e�e�,U�IѓOi���Y\��εd�&Gnˎ�3��'��o+�R�'�����g�qc����lc����QIH�����nn�MN��D���k>�@�Y�g7[?���<�c�*m4�؞�?��1�E��F��`�T"Ʀx%��]��2��c~τ�     