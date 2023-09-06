
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

# Carregar os dados de atividade do usuário
user_data = pd.read_csv("/home/youruser/myproject/ExploratoryDataAnalysis-Business/data/raw/user_activity_daily.csv")

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='user-graph'),
    dcc.Dropdown(
        id='user-dropdown',
        options=[
            {'label': 'Atividade Diária (Total de Logins)', 'value': 'daily'},
            {'label': 'Atividades Mais Comuns', 'value': 'common'}
        ],
        value='daily'
    )
])

@app.callback(
    Output('user-graph', 'figure'),
    [Input('user-dropdown', 'value')]
)
def update_graph(selected_value):
    if selected_value == 'daily':
        # Plot para atividade diária
        fig = {
            'data': [{
                'x': user_data['Date'],
                'y': user_data['Total_Logins'],
                'type': 'line'
            }],
            'layout': {
                'title': 'Atividade Diária (Total de Logins)'
            }
        }
    else:
        # Plot para atividades mais comuns
        fig = {
            'data': [
                {'x': ['Total_Logins', 'Total_Product_Views', 'Total_Add_to_Cart', 'Total_Purchases'],
                 'y': [user_data['Total_Logins'].sum(), user_data['Total_Product_Views'].sum(),
                       user_data['Total_Add_to_Cart'].sum(), user_data['Total_Purchases'].sum()],
                 'type': 'bar'}
            ],
            'layout': {
                'title': 'Atividades Mais Comuns'
            }
        }
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
