import pandas as pd
import numpy as np

def extractData():

    df = pd.read_csv("Data/MPI_All_States.csv")

    # 100 is divided because BMI columns are in percentage , however other columns are fraction
    df["Adults BMI Below Normal"]= (df["Men BMI Below Normal (%)"] + df["Women BMI Below Normal (%)"])/(2*100.0)
    df["Infant Mortality Rate (%)"] = df["Infant Mortality Rate (%)"]/100.0

    df = df.drop(columns=["Men BMI Below Normal (%)","Women BMI Below Normal (%)"])

    # normalise each columns
    colnames = df.drop(columns="State").columns
    for i in colnames:
        df["Orignal_".format(i)] = df[i]
        df[i] = (df[i] - np.min(df[i]))/(np.max(df[i])-np.min(df[i]))

    # from this point onwards "Orignal_" represents raw values , rest all are normalised.

    # calculation for evaluating MPI.
    contribution_dict = {"Adults BMI Below Normal":1/6,"Infant Mortality Rate (%)":1/6,
                         "Illiterate population (%)":1/6,"Attendance Ratio":1/6,
                         "Deprived_Cooking_Fuel (%)":1/18,"Deprived_Sanitisation (%)":1/18,
                         "Deprived_Drinking_Water (%)":1/18,"Deprived_Electricity (%)":1/18,
                         "Deprived_House (%)":1/18,"Deprived_Assets (%)":1/18}
    # generating contributions.
    for i in df.columns[1:]:
        if "Orignal_" not in i:  # remove orinal as they are unscaled.
            df["Contribution_{}".format(i)] = contribution_dict[i]*df[i]
    
    colnames = [i for i in df.columns if "Contribution_" in i]
    df["MPI Index"] = df[colnames].sum(axis=1)

    # convert contributions to percentage contributions
    colnames = [i for i in df.columns if "Contribution_" in i]
    pct_contribution = 100*df[colnames].values/df[colnames].sum(axis=1).values.reshape(-1,1)
    df_pct = pd.DataFrame(pct_contribution ,columns=[i.replace("Contribution","Pct") for i in colnames])

    # concatnat
    df = pd.concat([df,df_pct],axis=1)

    return df

