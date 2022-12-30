import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html


# create side bar

def masterLayout():
    
    sidebar_heading = html.Div([html.Img(src="assets\Application_Icon.PNG", style={"width": "3rem","border-radius":"50%"}),
                                html.H2("MPI")],className="sidebar-header")
    
    side_navigation_bar = dbc.Nav(
            [
                dbc.NavLink(
                    [html.I(className="fa-solid fa-house"), html.Span("About MPI",className="sidebar_span")],
                    href="/about",
                    active="exact",
                ),
                
                dbc.NavLink(
                    [html.I(className="fa-solid fa-database"), html.Span("Data Source - NDAP",className="sidebar_span")],
                    href="/datasource",
                    active="exact",
                ),
                dbc.NavLink(
                    [html.I(className="fa-solid fa-magnifying-glass-chart"), html.Span("Analysis",className="sidebar_span")],
                    href="/analysis",
                    active="exact",
                ),
            ],
            vertical=True,
            pills=True,
        )
    
    sidebar = html.Div([sidebar_heading,html.Hr(),side_navigation_bar ],className="sidebar")
    mpi_heading = html.Div([html.H4("Multidimensional Poverty Index of Indian States",style={"margin-top":"10px"})],id="mpi_heading")
    master_layout = html.Div([sidebar,mpi_heading,dash.page_container],id = "master_layout")

    return master_layout
