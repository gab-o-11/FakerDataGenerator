import csv
import random
from datetime import datetime, timedelta
import os

def obtener_ids_csv(nombre_archivo, campo_id):
    with open(nombre_archivo, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return [row[campo_id] for row in reader]

def generar_sanciones_csv(nombre_archivo, prestamos, porcentaje=0.2):
    os.makedirs(os.path.dirname(nombre_archivo), exist_ok=True)

    tipos = ['multa por retraso', 'libro dañado', 'pérdida de libro']
    total = int(len(prestamos) * porcentaje)
    sancionados = random.sample(prestamos, total)

    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Prestamo.ID', 'tipo', 'monto', 'observaciones', 'fecha'])

        for i, prestamo_id in enumerate(sancionados, 1):
            sancion_id = f"SAN{i:07d}"
            tipo = random.choice(tipos)
            monto = random.randint(10, 100)
            observaciones = '' if random.random() < 0.1 else f"{tipo.capitalize()} aplicada."
            fecha = datetime(2024, 1, 1) + timedelta(days=random.randint(0, 365))
            writer.writerow([sancion_id, prestamo_id, tipo, monto, observaciones, fecha.date()])

escalas = ['1k', '10k', '100k', '1M']

for escala in escalas:
    print(f"🛠 Generando Sancion.csv para {escala}...")
    prestamos = obtener_ids_csv(f'output/{escala}/Prestamo.csv', 'ID')
    generar_sanciones_csv(f'output/{escala}/Sancion.csv', prestamos)
    print(f"✅ Sancion.csv generado para {escala}")
