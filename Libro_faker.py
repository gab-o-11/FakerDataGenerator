from faker import Faker
import csv
import random
import os

faker = Faker()
Faker.seed(2)
random.seed(2)

def generar_libros_csv(nombre_archivo, num_titulos, ejemplares_por_titulo, ids_autores):
    os.makedirs(os.path.dirname(nombre_archivo), exist_ok=True)

    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'titulo', 'isbn', 'editorial', 'anio_publicacion', 'estado', 'disponibilidad', 'Autor.ID'])

        libro_id_counter = 1
        for _ in range(num_titulos):
            titulo = faker.sentence(nb_words=5).rstrip('.')
            isbn = faker.isbn13()
            editorial = faker.company()
            anio = faker.year()
            autor_id = random.choice(ids_autores)

            for _ in range(ejemplares_por_titulo):
                libro_id = f"LIB{libro_id_counter:07d}"
                estado = random.choice(['nuevo', 'usado', 'deteriorado'])
                disponibilidad = random.choice(['disponible', 'prestado', 'perdido'])
                writer.writerow([libro_id, titulo, isbn, editorial, anio, estado, disponibilidad, autor_id])
                libro_id_counter += 1

def obtener_ids_autores(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return [row['ID'] for row in reader]

ids_autores = obtener_ids_autores('output/1k/Autor.csv')
generar_libros_csv('output/1k/Libro.csv', num_titulos=100, ejemplares_por_titulo=10, ids_autores=ids_autores)
ids_autores = obtener_ids_autores('output/10k/Autor.csv')
generar_libros_csv('output/10k/Libro.csv', num_titulos=1000, ejemplares_por_titulo=10, ids_autores=ids_autores)
ids_autores = obtener_ids_autores('output/100k/Autor.csv')
generar_libros_csv('output/100k/Libro.csv', num_titulos=10000, ejemplares_por_titulo=10, ids_autores=ids_autores)
ids_autores = obtener_ids_autores('output/1M/Autor.csv')
generar_libros_csv('output/1M/Libro.csv', num_titulos=20000, ejemplares_por_titulo=50, ids_autores=ids_autores)

