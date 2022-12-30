import pandas as pd
import numpy as np
import dash
from dash import html, dcc, dash_table

dash.register_page(__name__)


def datasourceLayout():


    heading1 = html.Div([html.H4(['What is NDAP?'],style={"font-weight":"bold","margin-left":"5px"})],className="datasource_heading")
    content1 = html.Div([html.P("The National Data and Analytics Platform (or NDAP) is NITI Aayog’s flagship \
                       initiative to improve access and use of government data. NDAP is a user-friendly\
                       web platform that aggregates and hosts datasets from across India’s vast \
                       statistical infrastructure.NDAP seeks to democratize data delivery by making \
                       government datasets readily accessible, implementing rigorous data sharing \
                       standards, enabling interoperability across the Indian data landscape.Datasets\
                       on NDAP are made interoperable by mapping them to a common set of geographical \
                       and temporal identifiers using the Ministry of Panchayati Raj Local Government \
                       Directory Code. This enables users to merge datasets from different sectors and\
                       sources for easier cross-sectoral analysis.NITI Aayog aims to make data more\
                       accessible by hosting data in clean, machine-readable formats, ensuring datasets\
                       are interoperable, and providing detailed documentation on the contents of each\
                       dataset. As of Dec 2022, NDAP hosts 766 datasets from across 15 sectors and 46 \
                       Ministries.")],className="datasource_content")

    heading2 = html.Div([html.H4(['Data Availability'],style={"font-weight":"bold","margin-left":"5px"})],className="datasource_heading")
    content2 = html.Div([html.P("To assess the Multidimensional Poverty Index (MPI) for \
                                 various Indian states, data on a variety of markers must be collected, \
                                 such as child mortality, nutrition level, years of schooling, school\
                                 attendance, accessibility of cooking fuel, sanitation, drinking water,\
                                 electricity, and housing. Unfortunately, much of this data is not\
                                 readily available. To address this challenge, the closest available \
                                 data is used for analysis. The table below compares the data utilized\
                                 by OPHI for the Global Multidimensional Poverty Index study versus the \
                                 data utilized in this analysis for the state-wide Multidimensional \
                                 Poverty Index study.")],className="datasource_content")

    df = pd.read_excel("Data/New Microsoft Excel Worksheet.xlsx")
    data_table = dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns],
                                       fixed_rows={'headers': True},
                                       style_table={'overflowX': 'auto'},
                                       style_cell={'height': 'auto','minWidth': '180px', 
                                                    'width': '180px', 'maxWidth': '180px',
                                                    'whiteSpace': 'normal',
                                                    'fontSize':15, 'font-family':'sans-serif',
                                                    "text-align":"center"},
                                      style_header={'backgroundColor': 'rgb(30, 30, 30)',
                                                    'color': 'white',"font-weight":"bolder"})

    
    heading_table = html.Div([html.H4(['NDAP Data Source'],style={"font-weight":"bold","margin-left":"5px"})],className="datasource_heading")
    content_table = html.Div([data_table],id = "datasource_table")
    
    heading3 = html.Div([html.H4(['Data Extraction'],style={"font-weight":"bold","margin-left":"5px"})],className="datasource_heading")
    content3 = html.Div([html.P("All data available on NDAP is extracted using APIs.")],className="datasource_content")

    heading4 = html.Div([html.H4(['Data Normalisation'],style={"font-weight":"bold","margin-left":"5px"})],className="datasource_heading")
    content4 = html.Div([html.P("To accurately assess the data extracted using APIs, it is necessary \
                                 to normalize the data based on the population size of each District/State.\
                                 Since a majority of the data is expressed in absolute numbers, \
                                 normalization is essential in order to account for the varying population \
                                 sizes across different Districts/States. This process ensures the data is\
                                 accurately represented and provides a more equitable comparison between \
                                 the various States.")],className="datasource_content")

    heading5 = html.Div([html.H4(['Data Aggregation'],style={"font-weight":"bold","margin-left":"5px"})],className="datasource_heading")
    content5 = html.Div([html.P("The data available on NDAP from various ministries varies in terms of\
                                 granularity. For example, data related to child mortality and nutrition \
                                 is available on a state-level, whereas data about the availability of \
                                 cooking fuel, sanitation, and drinking water is available on a \
                                 district-level. To ensure the data is accurately analyzed, the \
                                 granularity of the different data sources must be matched. Since the MPI\
                                 is being assessed at the state-level, district-level data must be \
                                 aggregated to estimate the indicators at the state-level. Different \
                                 aggregation methods are used for different indicators depending on the\
                                 context. The aggregation methods used for each indicator are listed in \
                                 the data aggregation table above.")],className="datasource_content")

    heading6 = html.Div([html.H4(['Data Merge'],style={"font-weight":"bold","margin-left":"5px"})],className="datasource_heading")
    content6 = html.Div([html.P("After aggregating the data at the state level, the data from the various \
                                 sources is merged together using the state name as the common identifier,\
                                 resulting in the final dataset.")],className="datasource_content")
    
    layout = html.Div([heading1,content1,heading2,content2,heading_table,content_table,heading3,content3,
                       heading4,content4,heading5,content5,heading6,content6 ])
    
    return layout

layout = datasourceLayout()