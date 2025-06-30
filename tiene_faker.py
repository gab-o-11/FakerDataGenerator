import csv
import random
import os

def obtener_ids_csv(nombre_archivo, campo_id):
    with open(nombre_archivo, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return [row[campo_id] for row in reader]

def generar_tiene_con_replicas(nombre_archivo, libros, categorias, titulos_unicos, replicas):
    os.makedirs(os.path.dirname(nombre_archivo), exist_ok=True)

    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Libro.ID', 'Categoria.ID'])

        for i in range(titulos_unicos):
            num_categorias = random.randint(1, 4)
            categorias_del_titulo = random.sample(categorias, num_categorias)

            for j in range(replicas):
                libro_id = f"LIB{(i * replicas + j + 1):07d}"
                for categoria_id in categorias_del_titulo:
                    writer.writerow([libro_id, categoria_id])

escalas = {
    '1k':   (100, 10),
    '10k':  (1000, 10),
    '100k': (10000, 10),
    '1M':   (20000, 50),
}

for escala, (titulos, replicas) in escalas.items():
    print(f"Generando Tiene.csv para escala: {escala}")
    libros = obtener_ids_csv(f'output/{escala}/Libro.csv', 'ID')
    categorias = obtener_ids_csv(f'output/{escala}/Categoria.csv', 'ID')
    generar_tiene_con_replicas(f'output/{escala}/Tiene.csv', libros, categorias, titulos, replicas)
    print(f"Tiene.csv generado para {escala}")
