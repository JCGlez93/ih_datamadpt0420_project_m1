import pandas as pd
from sqlalchemy import create_engine

# acquisition functions

def acquire():


    sqlitedb_path = '/home/jc/Escritorio/Proyectos_finales_ironhack/ih_datamadpt0420_project_m1/data/raw/raw_data_project_m1.db'
    engine = create_engine(f'sqlite:///{sqlitedb_path}')
    # list all tables in database
    pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", engine)
    # query one of 0,1,2 & 3
    df_personal_info = pd.read_sql_query("select * from personal_info", engine)
    country_info = pd.read_sql_query("select * from country_info", engine)
    career_info = pd.read_sql_query("select * from career_info", engine)
    poll_info = pd.read_sql_query("select * from poll_info", engine)

    #Letś do a merge to have a unique dataset

    df_personal_info
    country_info
    career_info
    poll_info

    a = df_personal_info.merge(country_info, left_on='uuid', right_on='uuid')
    b = a.merge(career_info, left_on='uuid', right_on='uuid')
    final_sql= b.merge(poll_info, left_on='uuid', right_on='uuid')

    #letś save the file from the sql

    import os

    mainpath = "/home/jc/Escritorio/Proyectos_finales_ironhack/ih_datamadpt0420_project_m1/data/raw"
    filename= "download_sql"
    fullpath= os.path.join(mainpath,filename)
    final_sql.to_csv(fullpath+ ".csv", index=False)

    print(f'{filename} , correctly saved')

    return final_sql
