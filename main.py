from flask import Flask, jsonify, redirect, url_for
import pandas as pd
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import threading
from visualizations.dash_apps import sales_dashboard


app = Flask(__name__)
app.debug = True

# Configuração para o Dash
app_dash = dash.Dash(
    __name__,
    server=app,
    routes_pathname_prefix='/dash/'
)

def run_sales_dashboard():
    sales_dashboard.app.run_server(debug=True, port=7082) 

def read_sales_data(semester):
    if semester == '1':
        filepath = "/home/youruser/myproject/ExploratoryDataAnalysis-Business/data/processed/sales_first_semester.csv"
    else:
        filepath = "/home/youruser/myproject/ExploratoryDataAnalysis-Business/data/processed/sales_second_semester.csv"
    return pd.read_csv(filepath)

def process_sales_data(dataframe):
    months = dataframe['month'].tolist()
    sales = dataframe['sales'].tolist()
    return sales, months

def init_sales_dashboard():
    layout = html.Div([
        html.H1('Sales Dashboard'),
        dcc.Graph(id='sales-graph'),
        dcc.Dropdown(
            id='sales-dropdown',
            options=[{'label': 'Semestre 1', 'value': '1'}, {'label': 'Semestre 2', 'value': '2'},
                     {'label': 'Vendas por Produtos', 'value': '3'}],
            value='1'
        ),
    ])

    @app_dash.callback(
        Output('sales-graph', 'figure'),
        [Input('sales-dropdown', 'value')]
    )
    def update_sales_graph(selected_value):
        if selected_value == '3':
            t = threading.Thread(target=run_sales_dashboard)
            t.start()
            return {}
    
        sales_data = read_sales_data(selected_value)
        y_values, x_values = process_sales_data(sales_data)
    
        figure = {
            'data': [{'x': x_values, 'y': y_values, 'type': 'bar', 'name': 'Vendas'}],
            'layout': {'title': 'Gráfico de Vendas'}
        }
        return figure

    app_dash.layout = layout
    

# Inicializando o dashboard
init_sales_dashboard()


@app.route('/', methods=['GET'])
def index():
    return redirect('/dash/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7081)  # Executando na porta 7081



