import pandas as pd
import os

# analysis functions

def analyse(final_dataset_def,country='all'):
    final_dataset_def = final_dataset_def.rename(
        columns={"country": "Country", "normalized_job_title": "Job Title", "rural": "Rural"})
    df = final_dataset_def.groupby(["Country", "Job Title", "Rural"]).size().reset_index(name="Quantity")
    df["Percentage"] = df["Quantity"] / df["Quantity"].sum()
    df["Percentage"] = df["Percentage"].round(8)
    df["Percentage"].max()
    df['Percentage'] = df['Percentage'].astype(float).map("{:.2%}".format)


# Analysis b
    most_demanded_jobs = df.sort_values(by="Percentage", ascending=False)
    #for i in df["Percentage"]:  # loop to convert the number to string
        #df["Percentage"] = str(i) + "%"
    mainpath = "/home/jc/Escritorio/Proyectos_finales_ironhack/ih_datamadpt0420_project_m1/data/raw"
    filename = "most_demanded_jobs"
    fullpath = os.path.join(mainpath, filename)
    most_demanded_jobs.to_csv(fullpath + ".csv", index=False)


    if country == None:
     print(country)
     mainpath = "/home/jc/Escritorio/Proyectos_finales_ironhack/ih_datamadpt0420_project_m1/data/raw"
     filename = "df_for_visualisation_all"
     fullpath = os.path.join(mainpath, filename)
     df.to_csv(fullpath + ".csv", index=False)
     print(f'{filename} , correctly saved')
     print(f'saved at : {fullpath}')

     return df

    else :
     df = df[df['Country'] == country]
     mainpath = "/home/jc/Escritorio/Proyectos_finales_ironhack/ih_datamadpt0420_project_m1/data/raw"
     filename = f'df_for_visualisation{country}'
     fullpath = os.path.join(mainpath, filename)
     df.to_csv(fullpath + ".csv", index=False)
     print(f'{filename} , correctly saved')
     print(f'saved at : {fullpath}')


    return df