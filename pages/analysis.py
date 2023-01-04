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
    
    content_result = html.Div([],className="analysis_content")

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
                                Uttar Pradesh, Punjab, and Haryana are all struggling with the same set of \
                                indicators, so similar policy improvements could be implemented in those \
                                states.")],className="analysis_content")    

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
    
    
    img4 = html.Img(src="assets/num_factors.PNG",
                   style={"display":"inline-block","width":"350px","height":"250px","border-radius":"25px"})
    content4 = html.Div([html.P("To identify the number of factors that contribute to the covariance in\
                                 the data, we used Eigenvalues. These values indicate the amount of \
                                 variance explained by each factor. In our analysis, we only included \
                                 factors that had Eigenvalues greater than 1, as these factors explain \
                                 more variance than a single indicator. As shown in the figure, there \
                                 are two factors that have Eigenvalues greater than 1. Therefore, we \
                                 selected these two factors for our analysis."),img4],
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
    
    
    img6_1 = html.Img(src="assets/distortion_score.PNG",
                   style={"display":"inline-block","width":"50%","height":"350px","border-radius":"25px"})
    img6_2 = html.Img(src="assets/shillhoute_score.PNG",
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
                                 img6_1,img6_2],
                                 className="analysis_content")


    layout = html.Div([ heading_result,content_result,heading1,content1,heading2,content2,heading3,subheading3,content3,
                       subheading4,content4,heading5,content5,heading6,content6])

    return layout

layout = analysisLayout()