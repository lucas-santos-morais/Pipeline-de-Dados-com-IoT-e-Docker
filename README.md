<h1 style="text-align: center;">🚀 Pipeline de Dados com IoT e Docker </h1>


<div align="justify">
  Projeto da faculdade com o intuito de criar um pipeline de dados utilizando Docker. Foi utilizada a linguagem Python para automatizar esse processo. O projeto é focado em três tecnologias disruptivas: 
IoT, Big Data e IA. Ele utiliza uma base de dados em CSV, armazena as informações no PostgreSQL como banco de dados, e o Python foi empregado para limpar os dados da tabela e conectar-se ao banco. Após isso, 
utilizamos algumas bibliotecas do Python para transformar os dados em gráficos, tornando a visualização mais clara e intuitiva.
</div>

<br>![Status](https://img.shields.io/badge/projeto-conclu%C3%ADdo-brightgreen?style=flat)</br>

## 📌 Visão Geral da Arquitetura

- **Iot (Base de dados em CSV)** - Base de dados de temperatura
- **Docker (PostgreSQL)** - Docker usado para o banco de dados 
- **Python (Linguagem principal)** -Usada para processar, inserir os dados e montar a visualização do gráfico.

## 🛠️ Tecnologias Utilizadas

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![IoT](https://img.shields.io/badge/IoT-0078D4?style=flat&logo=iot&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)

## 📂 Estrutura do Projeto

```text
├── data
│   └── dados.csv
├── docs
│   └── relatorio.pdf
├── src
│   ├── dashboard.py
│   └── readmeCSV.py
└── .gitigonore
└── README.md
```
## ▶️ Como executar o projeto

### Pré-requisitos

* Alguma IDE, da sua escolha
* Docker 
* Python
* Baixar a base de dados no site - Kaggle
https://www.kaggle.com/datasets/atulanandjha/temperature-readings-iot-devices

### Passo a Passo

1. Crie á estrutura do projeto seguindo o clean code 

2. Com o Python na IDE crie um ambiente virtual usando o **VENV**
```bash  
python -m venv <nome_do_ambiente>
```
3. Instale as bibliotecas necessárias dentro desse ambiente virtual
* Pandas
* psycopg2-binary
* sqlalchemy
* streamlit
* plotly

```bash 
pip install pandas psycopg2-binary sqlalchemy streamlit plotly
```
4. Criar o PostgreSQL
```bash 
docker run --name postgres-iot -e POSTGRES_PASSWORD=sua_senha -p 5432:5432 -d postgres
```
5. Copie os dois códigos em Python na pasta **SRC**

6. Execute o script readmeCSV.py para processar e inserir os dados
```bash 
python readmeCSV.py
```
7. Execute o script dashboard.py para verificar os gráficos
```bash 
streamlit run dashboard.py
```

## 📖 DOCS

Nesta parta do projeto tem um relatório explicando os passos que segui para criação do projeto, capturas de tela dos gráficos gerados e dados obtidos com as views SQL

### Licença 

Este projeto está licenciado sob a Licença MIT — veja o arquivo [LICENSE](LICENSE) para detalhes.