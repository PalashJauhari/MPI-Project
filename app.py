from dash import Dash, html, dcc
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
from masterlayout import masterLayout

app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME], 
          use_pages=True,url_base_pathname='/')

# name and Icon
app._favicon = 'Application_Icon.PNG'
app.title = "Multidimensional Poverty Index of Indian States"
server = app.server
app.layout = masterLayout()

if __name__ == '__main__':
	app.run_server(debug=False)
