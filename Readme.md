 ## Analise de Negócios - Exploratory Data Analysis Business - Python 🛍️📈 

Codificação de uma aplicação em Python voltada para Análise de Negócios, integrando visualizações de Dashboard com foco em vendas por semestre, vendas por produto e atividades de usuários. Estas visualizações são enriquecidas com gráficos informativos. Na parte de engenharia de dados, implementamos DAGs para Apache Airflow e utilizamos Apache Spark para tratamento de grandes volumes de dados, tanto brutos quanto processados. Fazemos uso de notebooks em Jupyter para análises detalhadas, e aplicamos processos de ETL (Extrair, Transformar e Carregar), essenciais na integração e processamento de grandes conjuntos de dados. O sistema possui modelagem de banco de dados SQL com tabelas específicas para consultas de vendas e informações de usuários. Também integrei notebooks RStudio em liguagem R, modelos de Machine Learning e estatística com bibliotecas personalizadas em Python. Toda essa estrutura é implementada e gerenciada usando fluxos Prefect, Dockerfile e configurações para contêineres.

Essa aplicação representa uma solução abrangente para Análise de Negócios, combinando a ingestão e processamento de dados, modelagem estatística e machine learning, e visualização interativa. Cada tecnologia empregada desempenha um papel específico no ecossistema da aplicação, assegurando eficiência e adaptabilidade.

## Tecnologias:

- Python
- Pandas
- Dash
- Flask
- Docker
- Jupyter Notebooks
- RStudio
- SQL
- Apache Airflow
- Prefect
- Shiny
- Tableau


## Instalação 🚀

Para iniciar com este repositório:

1. Clone o repositório para sua máquina local.
2. Instale as dependências necessárias.
3. Explore a estrutura de diretórios e comece sua análise!

## Rode os seguintes comandos para iniciar: 🖥️

```
python -m venv ExploratoryDataAnalysis-Business
```

### No Linux/macOS
```
source ExploratoryDataAnalysis-Business/bin/activate
```

### No Windows
```
.\ExploratoryDataAnalysis-Business\Scripts\activate
```

```   
pip install -r requirements.txt
```

### Rode o comando para rodar aplicação de forma Local: 🖥️

```   
python3 main.py
```   


### Rode para ver Vendas por Produtos e Usuários 🖥️

Acesse para rodar nesse diretório:
``` 
cd /visualizations/dash_apps
``` 
Vendas por Usuários
``` 
python3 sales_dashboard.py
``` 

Movimentação de Usuários:
``` 
python3 user_activity_dashboard.py
``` 

## Acesse aplicação na porta:

- Para ver Vendas por Semestre
http://172.28.133.1:7081

- Vendas por Produtos
http://127.0.0.1:7082

## Tecnologias Utilizadas 🛠️

- ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) - Linguagem de programação principal.
- ![Spark](https://img.shields.io/badge/-Spark-E25A1C?style=flat-square&logo=apache-spark&logoColor=white) - Para processamento de dados.
- ![Airflow](https://img.shields.io/badge/-Airflow-017CEE?style=flat-square&logo=apache-airflow&logoColor=white) - Para orquestração de tarefas.
- ![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=docker&logoColor=white) - Para containerização.


###Sequence Diagram
                    
```seq
Emerson->Brazil: Says Hello 
Note right of Brazil: Brazil thinks\nabout it 
Brazil-->Emerson: How are you? 
Emerson->>Emerson: I am good thanks!
```
## Fórmula dos elementos químicos do Café
```
Cafeína (C8H10N4O2):            Água (H2O):              Ácido clorogênico (simplificado, C16H18O9):

      N-C-N                            O                                    O
      |   |                           / \                                  ||
      C   C                          H  H                            O-C-C
      |   |                                                        /   |   \
      N   O                                                       O   O   O
      |   |                                                            |
      C   O                                                       C     C     C
          |                                                       |     |     |
          CH3                                                    ...   ...   ...


```



## echo "README.md Autor:"
Emerson Amorim
