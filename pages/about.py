import dash
from dash import html, dcc

dash.register_page(__name__)


def aboutLayout():

    heading1 = html.Div([html.H4(['Global Multidimensional Poverty Index'],style={"font-weight":"bold","margin-left":"5px"})],className="about_heading")
    
    img1 = html.Img(src="assets/MPI.png",style={"display":"inline-block","width":"475px","height":"375px","border-radius":"25px"})
    text1 = html.P("The Global Multidimensional Poverty Index (MPI) is a powerful tool for measuring poverty in \
             over 100 developing countries. Developed by the Oxford Poverty and Human Development \
             Initiative (OPHI) in partnership with the United Nations Development Programme (UNDP), \
             the MPI provides a comprehensive picture of people living in poverty by capturing acute \
             deprivations in health, education and living standards. The extent or intensity of the poverty is also measured\
             through the percentage of deprivations experienced by the individual. This makes the MPI \
             invaluable as an analytical tool to identify the most vulnerable people, and to reveal poverty \
             patterns within countries and over time.\
             The Global MPI is made up of three dimensions: health, education and living standards.\
             Each dimension is composed of various indicators, all of which are weighted differently. \
             In terms of health, indicators include the presence of undernourishment, child mortality, \
             and access to safe drinking water, for example. Similarly, for education, indicators include\
             years of schooling and school attendance, and for living standards, indicators include access\
             to cooking fuel, sanitation, electricity, and housing.",\
             style={"display":"inline-block","height":"400px","margin-right":"10px"})


    text2 = "The Global MPI is an important tool for measuring poverty, and its results can be used to \
             inform policy decisions. For example, the 2020 MPI Report found that reducing poverty at \
             scale is possible, and also unveiled new ‘poverty profiles’ that can offer a breakthrough \
             in understanding the causes of poverty. The Report also highlighted that 1.2 billion people \
             are multidimensionally poor, and that half of them live in severe poverty. The Global MPI \
             investigation is an invaluable analytical tool to identify the most vulnerable \
             people – the poorest among the poor, revealing poverty patterns within countries and over \
             time, enabling policy makers to target resources and design policies more effectively.\
             The Global MPI serves as an effective tool in measuring poverty, and its results can be used\
             to inform policy decisions to reduce poverty. By understanding the causes of poverty, policy \
             makers can design policies that are more effective in tackling poverty and improving the lives\
             of those living in poverty. The MPI is an important tool for governments and other \
             organisations working towards the common goal of reducing poverty and creating a better future \
             for all."

    
    content1 = html.Div([text1 , img1],className="about_content_1")

    img2 = html.Img(title="Global MPI",src="assets/global_mpi.jpg",
                    style={"display":"inline-block","height":"400px","width":"530px","border-radius":"25px"})
    content2 = html.Div([img2,text2],className="about_content_2")
    
    layout = html.Div([heading1,content1,content2])

    return layout

layout = aboutLayout()