import dash
import dash_html_components as html
from dash import Input, Output, dcc, html
import dash_bootstrap_components as dbc


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME])


app.layout = html.Div([
    # Radio buttons
    dcc.RadioItems(
        id='radio-buttons',
        options=[
            {'label': html.Div([html.I(className="fa-solid fa-house"),html.Span("Hello")],style={"display":"inline-block"}), 'value': 'bar-chart'},
            {'label': html.Div([html.I(className="fa-solid fa-house"),html.Span("Hello")],style={"display":"inline-block"}), 'value': 'map-view'}
        ],
        value='bar-chart'
    ),
    html.Div(id='radio-buttons-output')
])

@app.callback(
    dash.dependencies.Output('radio-buttons-output', 'children'),
    [dash.dependencies.Input('radio-buttons', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server()
