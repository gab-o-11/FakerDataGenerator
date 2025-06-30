import csv
import os

def generar_categorias_csv(nombre_archivo):
    categorias = [
        "Matemáticas", "Física", "Química", "Biología", "Cálculo", "Álgebra", "Geometría", "Estadística",
        "Algoritmos", "Programación", "Inteligencia Artificial", "Ciencias de la Computación", "Bases de Datos",
        "Arquitectura de Computadoras", "Electrónica", "Circuitos", "Señales y Sistemas", "Ingeniería de Software",
        "Redes", "Telecomunicaciones", "Mecánica", "Termodinámica", "Energía", "Ingeniería Ambiental", "Investigación",
        "Economía", "Sociología", "Psicología", "Filosofía", "Ética Profesional", "Historia", "Derecho", "Literatura",
        "Arte", "Música", "Teatro", "Religión", "Antropología", "Educación", "Lingüística", "Comunicación",
        "Administración", "Marketing", "Contabilidad", "Negocios", "Fantasía", "Ciencia Ficción", "Romance", "Misterio",
        "Terror", "Novela Gráfica"
    ]

    os.makedirs(os.path.dirname(nombre_archivo), exist_ok=True)

    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'nombre'])

        for i, nombre in enumerate(categorias, 1):
            cat_id = f"CAT{i:03d}"
            writer.writerow([cat_id, nombre])

generar_categorias_csv('output/1k/Categoria.csv')
generar_categorias_csv('output/10k/Categoria.csv')
generar_categorias_csv('output/100k/Categoria.csv')
generar_categorias_csv('output/1M/Categoria.csv')