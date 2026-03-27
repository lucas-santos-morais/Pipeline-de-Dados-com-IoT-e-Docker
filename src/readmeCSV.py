"""
Nome: Lucas Santos Morais
Objetivo:
- Ler arquivo CSV
- Organizar o arquivo CSV
- Enviar para o banco de dados
- Criar views para ser usado posteriormente

Data: 26/03/2026
Version: 1.0
"""
print("[1/8] Carregando bibliotecas")

#Importanto bibliotecas necessárias
import pandas as pd
from sqlalchemy import create_engine, text

print("[2/8] Lendo o arquivo IOT-temp.csv...")

#Ler o arquivo CSV dentro da pasta "data"
df = pd.read_csv("data/IOT-temp.csv")

#Transformar a coluna "noted_date" para o datetime
df["noted_date"] = pd.to_datetime(df["noted_date"], format="%d-%m-%Y %H:%M")

print("[3/8] Organizando o arquivo IOT-temp.csv")

#Renomear colunas da tabela
df = df.rename(columns={
    'room_id/id': 'device_id',
    'temp': 'temperature',
    'out/in': 'out_in'
})

#Conexão com o banco de dados "PostgreSQL"
engine = create_engine("postgresql://postgres:12345@localhost:5432/postgres")

print("[4/8] Banco de dados conectado ✅")

print("[5/8] Criando tabela no banco de dados")

#Criação da tabela no banco de dados para inserir os dados
df.to_sql(
    "iot_temp",
    engine,
    if_exists="replace",
    index=False
)

print("[6/8] Dados tratados e enviados para o banco com sucesso! ✅")

# ------------- Criação das VIEWS ------------- #

print("[7/8] Criando Views no banco de dados")

with engine.connect() as conn:
    # View 1: Média de temperatura po dispositivos
    conn.execute(text("""
        CREATE OR REPLACE VIEW avg_temp_por_dispositivo AS
        SELECT device_id, AVG(temperature) AS avg_temp
        FROM iot_temp
        GROUP BY device_id;
    """))
    # View 2: Contagem de Leituras por Hora
    conn.execute(text("""
        CREATE OR REPLACE VIEW leituras_por_hora AS
        SELECT EXTRACT(HOUR FROM noted_date) AS hora, COUNT(*) AS contagem
        FROM iot_temp
        GROUP BY EXTRACT(HOUR FROM noted_date)
        ORDER BY hora;
    """))

    # View 3: Temperaturas Máximas e Mínimas por Dia
    conn.execute(text("""
        CREATE OR REPLACE VIEW temp_max_min_por_dia AS
        SELECT DATE (noted_date) AS data, MAX (temperature) AS temp_max, MIN (temperature) AS temp_min
        FROM iot_temp
        GROUP BY DATE (noted_date)
        ORDER BY data;
    """))

    # Confirma as alterações no banco de dados
    conn.commit()

print("[8/8] Views SQL criadas com sucesso! Pipeline concluído ✅")

