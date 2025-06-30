from faker import Faker
import csv
import random
import os

faker = Faker()
Faker.seed(1)
random.seed(1)

def generar_autores_csv(nombre_archivo, cantidad):
    os.makedirs(os.path.dirname(nombre_archivo), exist_ok=True)

    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'nombre', 'apellido', 'fecha_nacimiento', 'nacionalidad'])

        for i in range(1, cantidad + 1):
            autor_id = f"AUT{i:07d}"
            nombre = faker.first_name()
            apellido = '' if random.random() < 0.1 else faker.last_name()
            fecha_nacimiento = faker.date_of_birth(minimum_age=30, maximum_age=90)
            nacionalidad = '' if random.random() < 0.1 else faker.country()
            writer.writerow([autor_id, nombre, apellido, fecha_nacimiento, nacionalidad])

generar_autores_csv('output/1k/Autor.csv', 1000)
generar_autores_csv('output/10k/Autor.csv', 10000)
generar_autores_csv('output/100k/Autor.csv', 100000)
generar_autores_csv('output/1M/Autor.csv', 1000000)