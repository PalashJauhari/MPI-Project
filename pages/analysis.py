import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from data import *
import plotly.graph_objects as go
import plotly.express as px
import json

dash.register_page(__name__)


def get_metric_rank(dff,statename):

    indicator_dict = {'Contribution_Illiterate population (%)':"Illiteracy",
                     'Contribution_Deprived_Cooking_Fuel (%)':"Deprived Cooking Fuel", 
                     'Contribution_Deprived_Sanitisation (%)':"Deprived Sanitisation", 
                     'Contribution_Deprived_Drinking_Water (%)':"Deprived Drinking Water", 
                     'Contribution_Deprived_Electricity (%)':"Deprived Electricity", 
                     'Contribution_Deprived_House (%)':"Deprived House", 
                     'Contribution_Deprived_Assets (%)':"Deprived Assets", 
                     'Contribution_Infant Mortality Rate (%)':"Infant Mortality Rate", 
                     'Contribution_Attendance Ratio':"Attendance Ratio", 
                     'Contribution_Adults BMI Below Normal':"Deprived Nutrition",
                     'MPI Index':"MPI Index"}

    rank_dict = {}
    dff = dff.reset_index().drop(columns="index")
    colnames = [i for i in dff.columns if "Orignal_" in i]
    colnames.append("MPI Index")
    for i in colnames:
        if i != "Orignal_Attendance Ratio":
            dff1 = dff.sort_values(i,ascending=False)
        else:
            dff1 = dff.sort_values(i,ascending=False)
        
        dff1 = dff1.reset_index().drop(columns="index")  
        dff_state = dff1[dff1["State"]==statename]
        rank_dict[indicator_dict[i.replace("Orignal_","Contribution_")]] = [np.round(dff_state[i].values[0],1),dff_state.index[0] + 1]
    
    return rank_dict 

def get_metric_rank_india(dff):

    rank_dict = {}
    dff = dff.reset_index().drop(columns="index")
    colnames = [i for i in dff.columns if "Orignal_" in i]
    colnames.append("MPI Index")
    
    for i in colnames:
        rank_dict[i.replace("Orignal_","")] = np.round(np.mean(dff[i]),2)

    return rank_dict 
    

def analysisLayout(inputDict):

    df = extractData()

    # input dropdown
    metric_dropdown = dcc.Dropdown(options=[{"label":"Overall MPI Index of States","value":"overall_mpi_index"},
                                            {"label":"Distribution of Contribution of Indicators","value":"distribution_indicators"},
                                             {"label":"Cluster Analysis","value":"cluster_analysis"},
                                             {"label":"Illiterate population","value":'Orignal_Illiterate population (%)'},
                                             {"label":"Deprived Cooking Fuel","value":'Orignal_Deprived_Cooking_Fuel (%)'},
                                             {"label":"Deprived Electricity","value":'Orignal_Deprived_Electricity (%)'},
                                             {"label":"Deprived House","value":'Orignal_Deprived_House (%)'},
                                             {"label":"Deprived Sanitisation","value":'Orignal_Deprived_Sanitisation (%)'},
                                             {"label":"Deprived Drinking Water","value":'Orignal_Deprived_Drinking_Water (%)'},
                                             {"label":"Deprived Assets","value":'Orignal_Deprived_Assets (%)'},
                                             {"label":"Infant Mortality Rate","value":'Orignal_Infant Mortality Rate (%)'},
                                             {"label":"Deprived Nutrition","value":'Orignal_Adults BMI Below Normal'},
                                             {"label":"Attendance Ratio","value":'Orignal_Attendance Ratio'}],
                                           value=inputDict["value_analysis_all_states_metric_dropdown"],
                                           id="analysis_all_states_metric_dropdown",
                                           maxHeight=175)

    radio_bottons = dcc.RadioItems(id='analysis_radio-buttons',
        options=[
            {'label': html.Div([html.I(className="fa-solid fa-chart-bar",style={"margin-left":"10px"}),html.Span("  Bar Chart")],
                               style={"display":"inline-block"}), 'value': 'bar-chart'},
            {'label': html.Div([html.I(className="fa-solid fa-map-location",style={"margin-left":"10px"}),html.Span("  Map")],
                               style={"display":"inline-block"}), 'value': 'map-view'}],value='bar-chart')

    
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

    if inputDict["value_analysis_all_states_metric_dropdown"]=='overall_mpi_index':
        
        df = df.sort_values("MPI Index",ascending=True)
        
        x = list(df["MPI Index"].values)
        y = list(df["State"].values)
        text = [str(np.round(i,4)) for i in list(df["MPI Index"].values)]

        fig = go.Figure()
        fig.add_trace(go.Bar(x=x,y=y,orientation='h',name="MPI Index",text=text,textposition='inside',
                      marker=dict(color=x,colorscale='turbo')))
        fig.update_layout(margin=dict(l=0, r=0, t=25, b=0),height=800)
    
    if inputDict["value_analysis_all_states_metric_dropdown"] in ['Orignal_Illiterate population (%)',
                                                                  'Orignal_Deprived_Cooking_Fuel (%)',
                                                                  'Orignal_Deprived_Sanitisation (%)',
                                                                  'Orignal_Deprived_Drinking_Water (%)',
                                                                  'Orignal_Deprived_Electricity (%)',
                                                                  'Orignal_Deprived_House (%)',
                                                                  'Orignal_Deprived_Assets (%)',
                                                                  'Orignal_Infant Mortality Rate (%)',
                                                                  'Orignal_Attendance Ratio', 
                                                                  'Orignal_Adults BMI Below Normal',
                                                                  "Orignal_Attendance Ratio"]:
        
        
        var1 = inputDict["value_analysis_all_states_metric_dropdown"]
        df = df.sort_values(var1,ascending=True)
        
        x = list(df[var1].values)
        y = list(df["State"].values)
        text = [str(np.round(i,1))+' %' for i in x]
            
        fig = go.Figure()

        if var1=="Orignal_Attendance Ratio":
            fig.add_trace(go.Bar(x=x,y=y,orientation='h',name=var1,text=text,textposition='inside',
                      marker=dict(color=x,colorscale='turbo_r')))
        else:
            fig.add_trace(go.Bar(x=x,y=y,orientation='h',name=var1,text=text,textposition='inside',
                      marker=dict(color=x,colorscale='turbo')))
        fig.update_layout(margin=dict(l=0, r=0, t=25, b=0),height=800)

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

    graph_figure = dcc.Graph(figure=fig,id="analysis_all_states_graph_hover")  
    graph_div = html.Div([graph_figure],id="analysis_all_states_graph_div")
    all_state_box = html.Div([metric_dropdown,graph_div ],id="analysis_all_state_box")

    #state wise
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
                     
    # plot graph
    selected_state = inputDict["value_analysis_all_states_graph_hover"]
    selected_state_metric_rank_dict = get_metric_rank(df,selected_state)
    selected_india_metric_rank_dict = get_metric_rank_india(df)

    selected_state_mpi = "MPI : {}".format(selected_state_metric_rank_dict['MPI Index'][0])
    selected_state_mpi_rank = "MPI Rank : {}/26".format(selected_state_metric_rank_dict['MPI Index'][1])
    
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
    card_row_1 = []
    for i in range(5):

        indicator = indicator_dict[colnames[i]]
        metric_score = selected_india_metric_rank_dict[colnames[i].replace("Contribution_","")]
        card_temp = dbc.Card(dbc.CardBody([html.P(indicator, className="card-title"),
                             html.P(str(metric_score)+" %", className="card-text")]),className="card_body")
        card_row_1.append(card_temp)
    
    card_row_2 = []
    for i in range(5,len(colnames)):

        indicator = indicator_dict[colnames[i]]
        metric_score = selected_india_metric_rank_dict[colnames[i].replace("Contribution_","")]
        card_temp = dbc.Card(dbc.CardBody([html.P(indicator, className="card-title"),
                             html.P(str(metric_score)+" %", className="card-text")]),className="card_body")
        card_row_2.append(card_temp)
    
    card_box_1 = html.Div(card_row_1,id="analysis_card_box_1")
    card_box_2 = html.Div(card_row_2,id="analysis_card_box_2")
    card_box_3 = html.Div([dbc.Card(dbc.CardBody([html.P("India MPI", className="card-title-india"),
                          html.P(str(selected_india_metric_rank_dict["MPI Index"]), className="card-text-india")],className="card-body-india"),className="card_body_india")],
                          "analysis_card_box_3")
    
    card_box_both = html.Div([card_box_1,card_box_2],id="analysis_card_box_both")
    card_box_all = html.Div([card_box_3,card_box_both],id="analysis_card_box_all")

    # ploting right side graph
    df_state = df[df["State"] == selected_state]
    colnames = [i for i in df.columns if "Contribution_" in i]
    metric_mean = dict(np.mean(df[colnames],axis=0))

    labels ,y_contribution,y_india_mean_contribution = [],[],[]
    for i in colnames:
        labels.append(indicator_dict[i])
        y_contribution.append(df_state[i].values[0])
        y_india_mean_contribution.append(metric_mean[i])

    # sort both labels and array .
    zipped_arrs = zip(y_contribution,labels,y_india_mean_contribution)
    zipped_arrs = sorted(zipped_arrs)
    y_contribution,labels,y_india_mean_contribution= zip(*zipped_arrs)
    
    # for showing custom hoverdata
    custom_data = [{"labels":labels[i],"y_contribution":str(np.round(y_contribution[i],3)),
                   "z":str(selected_state_metric_rank_dict[labels[i]][0]) + " %"} for i in range(len(labels))]
    hovertext = []
    for d in custom_data:
        hovertext.append(f"<br>{d['labels']}: {d['z']}<br>MPI Contribution: {d['y_contribution']}")
    
    fig_state = go.Figure()
    fig_state.add_trace(go.Bar(x=y_contribution,y=labels,orientation="h",name=selected_state,hovertext=hovertext,
                                textposition='inside'))
    fig_state .add_trace(go.Bar(x=y_india_mean_contribution ,y=labels,orientation="h",name="Indian Average",textposition='inside'))
    fig_state.update_layout(margin=dict(l=0, r=0, t=25, b=0),width=575,height=1000,
                            legend=dict(x=0,y=1.025,orientation="h",bgcolor='rgba(255, 255, 255, 0)'))
    graph_figure_state = dcc.Graph(figure=fig_state)
    
    selected_state_metric = html.Div([html.Div([selected_state]),
                                      html.Div([selected_state_mpi]),
                                      html.Div([selected_state_mpi_rank])],id="analysis_selected_state_metric")

    graph_figure_state_heading = html.P("Indicator Contribution in MPI",id="graph_figure_state_heading")
    state_wise_box = html.Div([selected_state_metric,graph_figure_state_heading,graph_figure_state],id="analysis_state_wise_box")
    # final layout
    layout = html.Div([card_box_all,all_state_box,state_wise_box],id='analytics-output')

    return layout


f = open("pages/inputdict.json")
inputdict = json.load(f)
layout = analysisLayout(inputdict)

@callback(
    Output(component_id='analytics-output', component_property='children'),
    [Input(component_id="analysis_all_states_metric_dropdown", component_property='value'),
    Input(component_id="analysis_all_states_graph_hover", component_property='clickData')])

def update_function(value_analysis_all_states_metric_dropdown,
                    value_analysis_all_states_graph_hover):
    inputdict["value_analysis_all_states_metric_dropdown"]=value_analysis_all_states_metric_dropdown
    #inputdict["value_analysis_radio_buttons"]=value_analysis_radio_buttons
    if value_analysis_all_states_graph_hover is not None:
        inputdict["value_analysis_all_states_graph_hover"] = value_analysis_all_states_graph_hover['points'][0]["label"]
    
    return analysisLayout(inputdict)