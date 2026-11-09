import sqlite3
import pandas as pd
import glob
import os

db_name = 'data/processed/olist.db'
conn = sqlite3.connect(db_name)
print(f'Base de datos {db_name} inicializada')

archivos_csv = glob.glob('data/raw/*.csv')

if not archivos_csv:
    print('No se encontraron archivos .csv')
else:
    for file_path in archivos_csv:
        base_name = os.path.basename(file_path).replace('.csv', '')
        table_name = base_name.replace('olist_', '').replace('_dataset', '')

        print(f"Cargando {table_name}...")
        df = pd.read_csv(file_path)

        df.to_sql(table_name, conn, if_exists='replace', index=False)

    print("\nTodas las tablas fueron cargadas a SQLite")


cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tablas = cursor.fetchall()
print("\nTablas disponibles en la base de datos:")
for t in tablas:
    print(f"- {t[0]}")

conn.close()