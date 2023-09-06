import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd


# Arquivo CSV precisa estar acessível e tem as colunas certas
try:
    sales_data = pd.read_csv("/home/youruser/myproject/ExploratoryDataAnalysis-Business/data/raw/sales_summary.csv")
except Exception as e:
    print(f"Erro ao carregar o arquivo CSV: {e}")
    sales_data = pd.DataFrame() 

# Criar a aplicação Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='sales-graph'),
    dcc.Dropdown(
        id='sales-dropdown',
        options=[
            {'label': 'Vendas por Produto', 'value': 'product'},
            {'label': 'Vendas Mensais', 'value': 'monthly'}
        ],
        value='product'
    )
])

@app.callback(
    Output('sales-graph', 'figure'),
    [Input('sales-dropdown', 'value')]
)
def update_graph(selected_value):
    try:
        if selected_value == 'product':
            fig = {
                'data': [{
                    'x': sales_data['Product_Name'],
                    'y': sales_data['Total_Units_Sold'],
                    'type': 'bar'
                }],
                'layout': {
                    'title': 'Vendas por Produto'
                }
            }
        else:
            # Agrupando por mês para obter o total de unidades vendidas em cada mês
            monthly_sales = sales_data.groupby('Month')['Total_Units_Sold'].sum().reset_index()
            fig = {
                'data': [{
                    'x': monthly_sales['Month'],
                    'y': monthly_sales['Total_Units_Sold'],
                    'type': 'line'
                }],
                'layout': {
                    'title': 'Vendas Mensais'
                }
            }
    except Exception as e:
        print(f"Erro ao atualizar o gráfico: {e}")
        return {}

    return fig

if __name__ == '__main__':
    app.run_server(debug=True, port=7082)

