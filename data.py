import pandas as pd
import numpy as np

def extractData():

    df = pd.read_csv("Data/MPI_All_States.csv")

    # 100 is divided because BMI columns are in percentage , however other columns are fraction
    df["Adults BMI Below Normal"]= (df["Men BMI Below Normal (%)"] + df["Women BMI Below Normal (%)"])/(2*100.0)
    df["Infant Mortality Rate (%)"] = df["Infant Mortality Rate (%)"]/100.0

    df = df.drop(columns=["Men BMI Below Normal (%)","Women BMI Below Normal (%)"])
    # all other columns are in fraction.

    contribution_dict = {"Adults BMI Below Normal":1/6,"Infant Mortality Rate (%)":1/6,
                         "Illiterate population (%)":1/6,"Attendance Ratio":1/6,
                         "Deprived_Cooking_Fuel (%)":1/18,"Deprived_Sanitisation (%)":1/18,
                         "Deprived_Drinking_Water (%)":1/18,"Deprived_Electricity (%)":1/18,
                         "Deprived_House (%)":1/18,"Deprived_Assets (%)":1/18}

    # generating contributions.
    for i in df.columns[1:]:
        df["Contribution_{}".format(i)] = contribution_dict[i]*df[i]
    
    colnames = [i for i in df.columns if "Contribution_" in i]
    df["MPI Index"] = df[colnames].sum(axis=1)

    return df

