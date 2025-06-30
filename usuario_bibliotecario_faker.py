import csv
import random
import os
from faker import Faker

faker = Faker('es_ES')
random.seed(0)

def generar_usuario_y_bibliotecario(persona_csv, usuario_csv, bibliotecario_csv, num_usuarios, num_bibliotecarios):
    with open(persona_csv, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        dnis = [row['DNI'] for row in reader]

    if num_usuarios + num_bibliotecarios > len(dnis):
        raise ValueError("No hay suficientes personas para usuarios y bibliotecarios.")

    random.shuffle(dnis)
    usuarios = dnis[:num_usuarios]
    bibliotecarios = dnis[num_usuarios:num_usuarios + num_bibliotecarios]

    os.makedirs(os.path.dirname(usuario_csv), exist_ok=True)
    os.makedirs(os.path.dirname(bibliotecario_csv), exist_ok=True)

    num_alumnos = int(num_usuarios * 0.9)
    num_profesores = num_usuarios - num_alumnos
    roles = ['alumno'] * num_alumnos + ['profesor'] * num_profesores
    random.shuffle(roles)

    with open(usuario_csv, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['DNI', 'rol'])
        for dni, rol in zip(usuarios, roles):
            writer.writerow([dni, rol])

    with open(bibliotecario_csv, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['DNI', 'fecha_hora_entrada', 'fecha_hora_salida'])
        for dni in bibliotecarios:
            fecha = faker.date_between(start_date='-1y', end_date='today')
            writer.writerow([dni, f"{fecha} 08:00", f"{fecha} 17:00"])

generar_usuario_y_bibliotecario('output/1k/Persona.csv', 'output/1k/Usuario.csv', 'output/1k/Bibliotecario.csv', 800, 200)
generar_usuario_y_bibliotecario('output/10k/Persona.csv', 'output/10k/Usuario.csv', 'output/10k/Bibliotecario.csv', 8000, 2000)
generar_usuario_y_bibliotecario('output/100k/Persona.csv', 'output/100k/Usuario.csv', 'output/100k/Bibliotecario.csv', 80000, 20000)
generar_usuario_y_bibliotecario('output/1M/Persona.csv', 'output/1M/Usuario.csv', 'output/1M/Bibliotecario.csv', 800000, 200000)
