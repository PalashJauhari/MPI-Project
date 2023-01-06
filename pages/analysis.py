import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from data import *
import plotly.graph_objects as go
import plotly.express as px
import json

dash.register_page(__name__)

def analysisLayout():

    heading_result = html.Div([html.H4(['Clustering of Indian States Based on Multidimensional Poverty Index Indicators'],
                         style={"font-weight":"bold","margin-left":"5px"})],className="analysis_heading")
    
    
    df1 = pd.read_csv("Data/State_Factors_Embeding.csv")
    df2 = pd.read_csv("Data/Final_Processed.csv")
    df = df1.merge(df2,on="State",how="inner")
    df["FA_Cluster"] = df["FA_Cluster"].apply(lambda x : str(x))

    #Normalise MPI Index so that difference in size is visibile
    df["MPI Index Normalised"] = (df["MPI Index"] - np.min(df["MPI Index"]))/(np.max(df["MPI Index"])-np.min(df["MPI Index"]))

    #df['text'] = df['State'] + '<br>' + 'MPI Index: ' + df['MPI Index'].astype(str)

    
    
    # plot clusters
    fig_cluster = px.scatter(df, x="Factor-1", y="Factor-2",color="FA_Cluster",
                             hover_data={'FA_Cluster':False,'MPI Index Normalised':False,
                                         "Factor-1":False,"Factor-2":False,
                                         "State":True , "MPI Index":':.4f'},
                             size="MPI Index Normalised")

    fig_cluster.update_layout(title={'text': "<b>State Clusters Based on MPI Indicators</b>",
                                    'y':1.0,'x':0.51, 'xanchor': 'center','yanchor': 'top'},
                              margin=dict(l=0, r=0, t=25, b=0),height=400,
                              xaxis=dict(title=dict(font=dict(size=16, family='Arial'))),
                              yaxis=dict(title=dict(font=dict(size=16, family='Arial'))))
    
    fig_cluster = dcc.Graph(figure=fig_cluster)  
    fig_cluster_div = html.Div([fig_cluster],id="analysis_state_clusters")

    # plot bar-chart comparisons
    #contribution_colnames = [i for i in df.columns if "Contribution" in i]
    #colnames = [i for i in df.columns if "Contribution" in i]
    #colnames.append("State")
    #colnames.append("MPI Index")
    #colnames.append("FA_Cluster")
    #df = df[colnames]

    #input_state = "Kerala"
    #df_state = df[df["State"]==input_state]
    #contribution_state = [df_state[i].values[0] for i in contribution_colnames]

    #state_cluster = "0"
    #df_cluster = df[df["FA_Cluster"]==state_cluster]
    #df_cluster = df_cluster.mean(axis=0)
    #df_cluster = df_cluster.T
    #contribution_cluster_0 = [df_cluster[i] for i in contribution_colnames]

    #state_cluster = "1"
    #df_cluster = df[df["FA_Cluster"]==state_cluster]
    #df_cluster = df_cluster.mean(axis=0)
    #df_cluster = df_cluster.T
    #contribution_cluster_1 = [df_cluster[i] for i in contribution_colnames]

    #state_cluster = "2"
    #df_cluster = df[df["FA_Cluster"]==state_cluster]
    #df_cluster = df_cluster.mean(axis=0)
    #df_cluster = df_cluster.T
    #contribution_cluster_2 = [df_cluster[i] for i in contribution_colnames]

    #df_india = df.copy()
    #df_india = df_india.mean(axis=0)
    #df_india = df_india.T
    #contribution_india = [df_india[i] for i in contribution_colnames]

    #all_count = len(contribution_colnames)
    #contribution_all = contribution_state + contribution_cluster_0 + contribution_cluster_1 + \
    #                   contribution_cluster_2
    #type_all = [input_state]*all_count+["Cluster_0"]*all_count+["Cluster_1"]*all_count+\
    #           ["Cluster_2"]*all_count

    # change name to display on UI
    #contribution_colnames_display = [i.replace("Contribution_","") for i in contribution_colnames]
    #dff = pd.DataFrame({"Contribution in MPI":contribution_all,"Indicator":contribution_colnames_display*4,
    #                   "Type":type_all})
    #dff = dff.sort_values("Contribution in MPI").reset_index().drop(columns="index")
    
    
    #fig_compare = px.bar(dff, y="Indicator", x="Contribution in MPI", 
    #                     color="Type",color_discrete_sequence=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], 
    #                     barmode="group",orientation='h')

    #fig_compare.update_layout(title={'text': "<b>Comparison</b>",'y':1.0,'x':0.51, 
    #                                 'xanchor': 'center','yanchor': 'top'},
    #                          margin=dict(l=0, r=0, t=25, b=0),height=1000,
    #                          legend=dict(x=0,y=1.025,orientation="h",bgcolor='rgba(255, 255, 255, 0)'))
    
    #fig_compare = dcc.Graph(figure=fig_compare)  
    #fig_compare_div = html.Div([fig_compare],id="analysis_state_compare")

    #fig_cluster_final = html.Div([fig_cluster_div,fig_compare_div],id="analysis_cluster_final")
    
    heading1 = html.Div([html.H4(['Motivation'],style={"font-weight":"bold","margin-left":"5px"})],className="analysis_heading")
    content1 = html.Div([html.P("In our analysis of data on poverty in different states, we found that\
                                 using the Multidimensional Poverty Index (MPI) alone isn't enough to \
                                 understand the full picture. While the MPI can help us identify which \
                                 states are doing poorly in terms of poverty, breaking down the data by\
                                 individual indicators gives us a more nuanced understanding. For example,\
                                 we found that Himachal Pradesh and Arunachal Pradesh both have an MPI of \
                                 0.48 and 0.46 respectively, but the contribution of illiteracy to their \
                                 overall MPI is very different: just 11% for Himachal Pradesh, compared to \
                                 31% for Arunachal Pradesh. Similarly, Jharkhand and Tripura have similar \
                                 MPIs (0.6 and 0.59, respectively), but the contribution of attendance \
                                 ratios to their overall MPI is 8% and 28%, respectively.This highlights \
                                the importance of looking at individual indicators, rather than just relying\
                                on overall MPI scores. By identifying which states have similar contributing\
                                indicators, we can make more targeted policy recommendations to address \
                                poverty in those areas. For instance, our analysis found that Bihar, \
                                Odisha,Assam, and Jharkhand are all struggling with the same set of \
                                indicators, so similar policy improvements could be implemented in those \
                                states.")],className="analysis_content")  

    
    df = pd.read_csv("Data/Final_Processed.csv")
    df = df[['Illiterate population (%)', 'Deprived_Cooking_Fuel (%)','Deprived_Sanitisation (%)', 'Deprived_Drinking_Water (%)',
         'Deprived_Electricity (%)', 'Deprived_House (%)', 'Deprived_Assets (%)','Infant Mortality Rate (%)', 'Attendance Ratio',
         'Adults BMI Below Normal']]
    corr = df.corr()
    mask = np.tri(*corr.shape, k=0)
    corr_masked = np.ma.array(corr, mask=mask)
    fig_corr = go.Figure(data=go.Heatmap(z=(corr.values)*mask,x=corr.columns,y=corr.columns,text=(corr.values)*mask,texttemplate='%{text:.2f}',
                                colorscale="rdbu"))
    
    fig_corr.update_layout(title={'text': "<b>Correlation Between Contributions By Indicators</b>",'y':1.0,'x':0.50, 
                              'xanchor': 'center','yanchor': 'top'},
                           margin=dict(l=0, r=0, t=25, b=0))
    
    correlation_graph = dcc.Graph(figure=fig_corr)  
    correlation_graph_div = html.Div([correlation_graph])

    heading2 = html.Div([html.H4(['Factor Analysis'],style={"font-weight":"bold","margin-left":"5px"})],className="analysis_heading")
    content2 = html.Div([html.P("Factor analysis is a statistical method used to identify underlying \
                                 factors or hidden drivers that contribute to observed variations in a \
                                 set of variables. In our study, we have identified 10 indicators that \
                                 make up the Multidimensional Poverty Index (MPI). However, it is possible \
                                 that there are fewer, underlying factors that are actually responsible for\
                                 the variation in these 10 indicators. By using factor analysis, we can \
                                 try to identify the number of these latent factors and understand how \
                                 they relate to the observed indicators. This can help us identify the \
                                 key factors that we can focus on in order to improve all of the indicators.\
                                 The correlation matrix shows that some of the indicators are correlated \
                                 with each other, making it an appropriate choice to use factor analysis \
                                 to explore the latent factors that may be responsible for the observed \
                                 correlations in the data.")],className="analysis_content")

    heading3 = html.Div([html.H4(['Methodology'],style={"font-weight":"bold","margin-left":"5px"})],className="analysis_heading")
    subheading3 = html.Div([html.H4(['Preliminary Test'],style={"font-weight":"bold","margin-left":"5px"})],className="analysis_subheading")
    content3 = html.Div([html.P("It is important to verify the quality of the data before performing factor \
                                 analysis. The Bartlett sphericity test can be used to determine whether \
                                 the correlation matrix of the data is significantly different from an \
                                 identity matrix. If it is, this suggests that there is sufficient structure\
                                 in the data to proceed with factor analysis. In our study, we found that \
                                 the correlations in the data indicate the presence of latent factors that\
                                 underlie the data.")],className="analysis_content")
    subheading4 = html.Div([html.H4(['Identifying Number of Factors'],style={"font-weight":"bold","margin-left":"5px"})],className="analysis_subheading")
    
    
    df = pd.read_csv("Data/Num_Factors_Eigen_Values.csv")
    y = list(df["Eigen Value"].values)
    x = list(df["Num of Factors"].values)
    fig4 = px.line(df,x="Num of Factors", y="Eigen Value",markers=True)
    fig4.update_layout(title={'text': "<b>Number of Factors Scree Plot</b>",'y':1.0,'x':0.51, 
                              'xanchor': 'center','yanchor': 'top'},
                      margin=dict(l=0, r=0, t=25, b=0),height=300,width=300)
    fig4.add_hline(y=1, line_width=1, line_dash="dash", line_color="red")
    graph_figure_4 = dcc.Graph(figure=fig4)  
    graph_div_4 = html.Div([graph_figure_4],
                           style={"display":"inline-block","width":"350px","border-radius":"25px"})
    
    content4 = html.Div([html.P("To identify the number of factors that contribute to the covariance in\
                                 the data, we used Eigenvalues. These values indicate the amount of \
                                 variance explained by each factor. In our analysis, we only included \
                                 factors that had Eigenvalues greater than 1, as these factors explain \
                                 more variance than a single indicator. As shown in the figure, there \
                                 are two factors that have Eigenvalues greater than 1. Therefore, we \
                                 selected these two factors for our analysis."),graph_div_4],
                                 className="analysis_content",
                                 id="analysis_num_factors")

    heading5 = html.Div([html.H4(['Factor Analysis Results'],style={"font-weight":"bold","margin-left":"5px"})],className="analysis_heading")
    content5 = html.Div([html.P("The results of our factor analysis model showed that 60% of the variation\
                                 in the original dataset could be explained by two factors. These factors,\
                                 labeled as factor-1 and factor-2, had significant influence on several \
                                 variables in the dataset. For example, variables such as Deprived Cooking \
                                 Fuel, Deprived House, and Deprived Assets had high loading on factor-1, \
                                 meaning they were largely influenced by this factor. On the other hand, \
                                 variables such as Deprived Drinking Water, Deprived Electricity, Infant \
                                 Mortality Rate, and Nutrition had high loading on factor-2, indicating \
                                 they were primarily associated with this factor. Other variables, such as\
                                 Illiteracy, Deprived Sanitation, and Attendance Ratio, had loading on both\
                                 factors, suggesting they were impacted by both.The significance of this\
                                 analysis is that if we focus on improving factor-1, we could expect to \
                                 see improvements in indicators like Cooking Fuel, Housing, and Assets. \
                                 Similarly, working to improve factor-2 could lead to positive changes \
                                 in indicators like Drinking Water, Electricity, Infant Mortality Rate, \
                                and Nutrition.")],className="analysis_content")
    #table5

    heading6 = html.Div([html.H4(['Clustering With Factors'],style={"font-weight":"bold","margin-left":"5px"})],className="analysis_heading")
    
    df = pd.read_csv("Data/Num_Cluster_Distortion_Score.csv")
    fig6 = px.line(df,x="Num of Clusters", y="Distortion Score",markers=True)
    fig6.update_layout(title={'text': "<b>Number of Clusters Scree Plot</b>",'y':1.0,'x':0.50, 
                              'xanchor': 'center','yanchor': 'top'},
                      margin=dict(l=0, r=0, t=25, b=0),height=450,width=550)
    fig6.add_vline(x=3, line_width=1, line_dash="dash", line_color="red")
    graph_figure_6 = dcc.Graph(figure=fig6)  
    graph_div_6 = html.Div([graph_figure_6],
                           style={"display":"inline-block","width":"50%","height":"350px","border-radius":"25px"})

    df = pd.read_csv("Data/Silhouette_Score.csv")

    # first sort by silhouete score
    df = df.sort_values("Silhouette Score").reset_index().drop(columns="index")
    df["Labels"] = df["Labels"].apply(lambda x : str(x))
    # now grouby by labels so that similary groups score are plotted together.
    df1 = pd.DataFrame()
    for i,j in df.groupby("Labels"):
        df1 = pd.concat([df1,j],axis=0)
    
    df1 = df1.reset_index().drop(columns="index")
    df = df1.copy()
    fig6_1 = px.bar(df, x='Silhouette Score', color="Labels")
    fig6_1.update_layout(showlegend=False)
    fig6_1.update_layout(title={'text': "<b>Silhouette Score</b>",'y':1.0,'x':0.52, 
                              'xanchor': 'center','yanchor': 'top'},
                         margin=dict(l=0, r=0, t=25, b=0),height=450,width=550)
    fig6_1.add_vline(x=0.48, line_width=1, line_dash="dash", line_color="black")               
    graph_figure_6_1 = dcc.Graph(figure=fig6_1)  
    graph_div_6_1 = html.Div([graph_figure_6_1],
                           style={"display":"inline-block","width":"50%","height":"350px","border-radius":"25px"})

    
    
    content6 = html.Div([html.P("This section describes how clustering analysis was performed using KMeans \
                                 Clustering. Clustering is a technique for dividing a dataset into groups \
                                 (also known as clusters) of similar data points. The motivation of \
                                 clustering has been previously explained. Before applying KMeans \
                                 Clustering, we identified two latent factors. These latent factors are \
                                 underlying features or characteristics that are not directly observed, \
                                 but can be inferred from observed data. Identifying latent factors can \
                                 help to focus the analysis and improve the interpretability of the results.\
                                 Once the latent factors have been identified, we used KMeans Clustering to \
                                 group the data points into clusters.KMeans Clustering is a popular \
                                 algorithm that divides a dataset into a specified number of clusters by\
                                 iteratively reassigning data points to the cluster with the nearest mean,\
                                 until the cluster means no longer change. One issue with using KMeans \
                                 Clustering is determining the appropriate number of clusters to use. \
                                 We addressed this by using a distortion score elbow plot, which is a \
                                 graphical tool that plots the distortion score\
                                 (a measure of within-cluster variance) against the number of clusters.\
                                 The elbow in the plot indicates the optimal number of clusters, \
                                 as it is the point at which the distortion score decreases at a \
                                 diminishing rate. Based on the elbow plot, we selected 3 clusters for our \
                                 analysis. Finally, we performed KMeans Clustering with 3 clusters and \
                                 the two identified latent factors, and obtained a silhouette score of \
                                 0.48. The resulting clusters and silhouette score provide valuable \
                                 insights into the patterns and relationships within the data."),
                                 graph_div_6,graph_div_6_1],
                                 className="analysis_content")


    layout = html.Div([ heading_result,fig_cluster_div,heading1,content1,correlation_graph_div,
                        heading2,content2,heading3,subheading3,content3,
                        subheading4,content4,heading5,content5,heading6,content6])

    return layout

layout = analysisLayout()