from dash import Dash, html, dcc
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
from masterlayout import masterLayout

<<<<<<< HEAD
app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME], 
          use_pages=True,url_base_pathname='/')
=======
app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME], use_pages=True)
server = app.server
>>>>>>> 42431fc79a9563af64118c475b862d7c8c356750
app.layout = masterLayout()

if __name__ == '__main__':
	app.run_server(debug=False)
