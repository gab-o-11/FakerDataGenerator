from faker import Faker
import csv
import random

faker = Faker('es_ES')
Faker.seed(0)
random.seed(0)

def generar_dni_existente(used_dnis):
    while True:
        dni = str(random.randint(10000000, 99999999))
        if dni not in used_dnis:
            used_dnis.add(dni)
            return dni

def generar_personas_csv(nombre_archivo, cantidad):
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['DNI', 'nombre', 'apellido', 'email', 'telefono', 'fecha_nacimiento'])
        
        used_dnis = set()
        for _ in range(cantidad):
            dni = generar_dni_existente(used_dnis)
            nombre = faker.first_name()
            apellido = faker.last_name()
            email = faker.email()
            telefono = '' if random.random() < 0.05 else faker.msisdn()[:9]
            fecha_nacimiento = faker.date_of_birth(minimum_age=18, maximum_age=80)
            writer.writerow([dni, nombre, apellido, email, telefono, fecha_nacimiento])

generar_personas_csv('output/1k/Persona.csv', 1000)
generar_personas_csv('output/10k/Persona.csv', 10000)
generar_personas_csv('output/100k/Persona.csv', 100000)
generar_personas_csv('output/1M/Persona.csv', 1000000)