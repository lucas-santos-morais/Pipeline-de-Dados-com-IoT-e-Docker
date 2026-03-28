
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import streamlit as st


#Conexão com o banco de dados "PostgreSQL"
engine = create_engine("postgresql://postgres:12345@localhost:5432/postgres")

# Função para carregar dados de uma view
def load_data(view_name):
 return pd.read_sql(f"SELECT * FROM {view_name}", engine)

# Título do dashboard
st.title('🌡️ Dashboard de Temperaturas IoT')

# Gráfico 1: Média de temperatura por dispositivo
st.header('Média de Temperatura por Dispositivo')
df_avg_temp = load_data('avg_temp_por_dispositivo')
fig1 = px.scatter(df_avg_temp, x='device_id', y='avg_temp', size='avg_temp', labels={'device_id': 'ID do Dispositivo', 'avg_temp': 'Temperatura Média (°C)'}, color='device_id')
st.plotly_chart(fig1)

# Gráfico 2: Contagem de leituras por hora
st.header('Leituras por Hora do Dia')
df_leituras_hora = load_data('leituras_por_hora')
fig2 = px.line(df_leituras_hora, x='hora', y='contagem', labels={'hora': 'Hora do Dia', 'contagem': 'Total de Leituras'})
st.plotly_chart(fig2)

# Gráfico 3: Temperaturas máximas e mínimas por dia
st.header('Temperaturas Máximas e Mínimas por Dia')
df_temp_max_min = load_data('temp_max_min_por_dia')
df_temp_max_min = df_temp_max_min.rename(columns={'temp_max': 'Temp. Máxima', 'temp_min': 'Temp. Mínima'})
fig3 = px.line(df_temp_max_min, x='data', y=['Temp. Máxima', 'Temp. Mínima'], labels={'data': 'Data da Leitura', 'value': 'Temperatura (°C)', 'variable': 'Métrica'})
st.plotly_chart(fig3)

# Gráfico 4: Comparação de Temperatura In/Out
st.header('Temperatura Média Diária: Interna vs Externa')
df_in_out_dia = load_data('avg_temp_in_out_dia')
df_in_out_dia['out_in'] = df_in_out_dia['out_in'].replace({'In': 'Interna', 'Out': 'Externa'})
fig4 = px.line(df_in_out_dia, x='data', y='avg_temp', color='out_in', labels={'data': 'Data', 'avg_temp': 'Temperatura Média (°C)', 'out_in': 'Localização'})
st.plotly_chart(fig4)