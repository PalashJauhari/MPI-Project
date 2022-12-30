import dash
from dash import html, dcc

dash.register_page(__name__)


def aboutLayout():

    heading1 = html.Div([html.H4(['Global Multidimensional Poverty Index'],style={"font-weight":"bold","margin-left":"5px"})],className="about_heading")
    
    img1 = html.Img(src="assets/MPI.png",style={"display":"inline-block","width":"500px","height":"400px"})
    text1 = html.P("The Global Multidimensional Poverty Index (MPI) is a powerful tool for measuring poverty in \
             over 100 developing countries. Developed by the Oxford Poverty and Human Development \
             Initiative (OPHI) in partnership with the United Nations Development Programme (UNDP), \
             the MPI provides a comprehensive picture of people living in poverty by capturing acute \
             deprivations in health, education and living standards. The MPI assesses poverty at the \
             individual level, and if a person is deprived in a third or more of ten weighted indicators, \
             they are identified as ‘MPI poor’. The extent or intensity of the poverty is also measured\
             through the percentage of deprivations experienced by the individual. This makes the MPI \
             invaluable as an analytical tool to identify the most vulnerable people, and to reveal poverty \
             patterns within countries and over time.",style={"display":"inline-block","height":"400px"})

    content1 = html.Div([text1 , img1],className="about_content_1")
    layout = html.Div([heading1,content1])

    return layout

layout = aboutLayout()