# import json
# import requests
import dash
from dash import dcc, html
#
# key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

# requesting data from url
# data = requests.get(key)
# data = data.json()
# print(f"{data['symbol']} price is {data['price']}")


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1('SAMPLE'),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 10], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])


if __name__ == '__main__':
    app.run_server(debug=False)
