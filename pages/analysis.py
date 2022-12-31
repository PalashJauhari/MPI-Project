import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from data import *
import plotly.graph_objects as go
import json

dash.register_page(__name__)

def analysisLayout(inputDict):

    df = extractData()


    # summary cards layout
    indicator_dict = {'Contribution_Illiterate population (%)':"Illiteracy",
                     'Contribution_Deprived_Cooking_Fuel (%)':"Deprived Cooking Fuel", 
                     'Contribution_Deprived_Sanitisation (%)':"Deprived Sanitisation", 
                     'Contribution_Deprived_Drinking_Water (%)':"Deprived Drinking Water", 
                     'Contribution_Deprived_Electricity (%)':"Deprived Electricity", 
                     'Contribution_Deprived_House (%)':"Deprived House", 
                     'Contribution_Deprived_Assets (%)':"Deprived Assets", 
                     'Contribution_Infant Mortality Rate (%)':"Infant Mortality Rate", 
                     'Contribution_Attendance Ratio':"Attendance Ratio", 
                     'Contribution_Adults BMI Below Normal':"Deprived Nutrition"}
    colnames = [i for i in df.columns if "Contribution_" in i]
    #print(colnames)
    card_row_1 = []
    for i in range(5):
        indicator = indicator_dict[colnames[i]]
        card_temp = dbc.Card(dbc.CardBody([html.P(indicator, className="card-title"),
                             html.P("0.5", className="card-text"),
                             html.P("14/28", className="rank-text")]),className="card_body")
        card_row_1.append(card_temp)
    
    card_row_2 = []
    for i in range(5,len(colnames)):
        indicator = indicator_dict[colnames[i]]
        card_temp = dbc.Card(dbc.CardBody([html.P(indicator, className="card-title"),
                             html.P("0.5", className="card-text"),
                             html.P("14/28", className="rank-text")]),className="card_body")
        card_row_2.append(card_temp)
    
    card_box_1 = html.Div(card_row_1,id="analysis_card_box_1")
    card_box_2 = html.Div(card_row_2,id="analysis_card_box_2")
    card_box_both = html.Div([card_box_1,card_box_2],id="analysis_card_box_both")

    # all state

    # input dropdown

    metric_dropdown = dcc.Dropdown(options=[{"label":"Overall MPI Index of States","value":"overall_mpi_index"},
                                            {"label":"Distribution of Contribution of Indicators","value":"distribution_indicators"},
                                            ],
                                           value=inputDict["value_analysis_all_states_metric_dropdown"],
                                           id="analysis_all_states_metric_dropdown",
                                           maxHeight=175)

    
    indicator_dict = {'Pct_Illiterate population (%)':"Illiteracy",
                     'Pct_Deprived_Cooking_Fuel (%)':"Deprived Cooking Fuel", 
                     'Pct_Deprived_Sanitisation (%)':"Deprived Sanitisation", 
                     'Pct_Deprived_Drinking_Water (%)':"Deprived Drinking Water", 
                     'Pct_Deprived_Electricity (%)':"Deprived Electricity", 
                     'Pct_Deprived_House (%)':"Deprived House", 
                     'Pct_Deprived_Assets (%)':"Deprived Assets", 
                     'Pct_Infant Mortality Rate (%)':"Infant Mortality Rate", 
                     'Pct_Attendance Ratio':"Attendance Ratio", 
                     'Pct_Adults BMI Below Normal':"Deprived Nutrition"}

    if inputDict["value_analysis_all_states_metric_dropdown"]=='distribution_indicators':
        
        df = df.sort_values("MPI Index",ascending=True)
        colnames = [i for i in df.columns if "Pct_" in i]

        fig = go.Figure()
        for i in colnames:
            x = list(df[i].values)
            y = list(df["State"].values)
            text = [str(np.round(i,0)) for i in list(df[i].values)]
            fig.add_trace(go.Bar(x=x,y=y,orientation='h',name=indicator_dict[i],text=text,textposition='inside'))

        fig.update_layout(barmode='relative',margin=dict(l=0, r=0, t=25, b=0),height=1000)

    graph_figure = dcc.Graph(figure=fig)  
    graph_div = html.Div([graph_figure],id="analysis_all_states_graph_div")
    all_state_box = html.Div([metric_dropdown,graph_div ],id="analysis_all_state_box")


    #state wise
    state_wise_box = html.Div([metric_dropdown,graph_div  ],id="analysis_state_wise_box")

    layout = html.Div([card_box_both,all_state_box,state_wise_box],id='analytics-output')

    return layout




f = open("pages/inputdict.json")
inputdict = json.load(f)
layout = analysisLayout(inputdict)

@callback(
    Output(component_id='analytics-output', component_property='children'),
    Input(component_id="analysis_all_states_metric_dropdown", component_property='value'))

def update_function(value_analysis_all_states_metric_dropdown):

    print(value_analysis_all_states_metric_dropdown)
    inputdict["value_analysis_all_states_metric_dropdown"]=value_analysis_all_states_metric_dropdown
    return analysisLayout(inputdict)
