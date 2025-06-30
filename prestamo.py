import csv
import random
import os
from datetime import datetime, timedelta

def obtener_ids_csv(nombre_archivo, campo_id):
    with open(nombre_archivo, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return [row[campo_id] for row in reader]

def generar_prestamos_csv(nombre_archivo, cantidad, usuarios, bibliotecarios, libros):
    os.makedirs(os.path.dirname(nombre_archivo), exist_ok=True)

    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'fecha_entrega', 'fecha_devolucion', 'Bibliotecario.DNI', 'Usuario.DNI', 'Libro.ID'])

        libros_disponibles = libros.copy()
        for i in range(1, cantidad + 1):
            if not libros_disponibles:
                libros_disponibles = libros.copy()

            prestamo_id = f"PRE{i:07d}"

            fecha_entrega = datetime(2025, 1, 1) + timedelta(days=random.randint(0, 180))
            dias_prestamo = random.randint(7, 30)
            fecha_devolucion = fecha_entrega + timedelta(days=dias_prestamo)

            usuario = random.choice(usuarios)
            bibliotecario = random.choice(bibliotecarios)
            libro_id = libros_disponibles.pop(random.randint(0, len(libros_disponibles) - 1))

            writer.writerow([
                prestamo_id,
                fecha_entrega.date(),
                fecha_devolucion.date(),
                bibliotecario,
                usuario,
                libro_id
            ])

escalas = {
    '1k': 1000,
    '10k': 10000,
    '100k': 100000,
    '1M': 1000000,
}

for escala, cantidad in escalas.items():
    usuarios = obtener_ids_csv(f'output/{escala}/Usuario.csv', 'DNI')
    bibliotecarios = obtener_ids_csv(f'output/{escala}/Bibliotecario.csv', 'DNI')
    libros = obtener_ids_csv(f'output/{escala}/Libro.csv', 'ID')

    generar_prestamos_csv(
        f'output/{escala}/Prestamo.csv',
        cantidad,
        usuarios,
        bibliotecarios,
        libros
    )

    print(f"Prestamo.csv generado para {escala}\n")
