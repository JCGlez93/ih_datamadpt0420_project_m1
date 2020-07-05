import pandas as pd
import os
from bs4 import BeautifulSoup
import requests
import re

# wrangling functions

def particionar_lista(table, n):
    return ([table[i * n:i * n + n] for i in range(len(table))])

def wrangle(final_sql):
    import requests
    import pandas as pd



    response = requests.get('http://api.dataatwork.org/v1/jobs?limit=600')  # saco el máximo de jobs
    json_data = response.json()

    json_data[0:3]

    len(json_data)  # tenemos un maximo de 500 que es lo que nos permite
    # we need to extract the jobs description from another API, that api requires an input

    norm_job_codes = final_sql['normalized_job_code'].unique().tolist()
    norm_job_dic = {}
    #  we create a loop to iterate all the dic values

    for i in norm_job_codes[1:]:  # to prevent errors , let's skip none and then we will add it. You can write a  if error pass.
        response = requests.get(f'http://api.dataatwork.org/v1/jobs/{i}')
        norm_job_dic[i] = (response.json())['normalized_job_title']
    norm_job_dic['none'] = 'none'  # adding the none
    pd.DataFrame(norm_job_dic.items())  # extract the dic values to create a dataframe
    job_codes = pd.DataFrame(norm_job_dic.items(), columns=['normalized_job_code', 'normalized_job_title'])

    #Let's add that new info to our dataframe and save it as csv


    final_dataset = final_sql.merge(job_codes, left_on='normalized_job_code', right_on='normalized_job_code')

    mainpath = "/home/jc/Escritorio/Proyectos_finales_ironhack/ih_datamadpt0420_project_m1/data/raw"
    filename= "final_dataset"
    fullpath= os.path.join(mainpath,filename)
    final_dataset.to_csv(fullpath+ ".csv", index=False)


#scrapping
    url = 'https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes'
    html = requests.get(url).content
    html[:500]



    # lxml is the parsing module
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find_all('td')
    table = list(table)


    CLEAN = re.compile('[\s+()]')

    table = [CLEAN.sub(' ', a.text).strip() for a in table]

    table = list(table)
    for i in table:  # iterable to eliminate blanks
        if i == "":
            table.remove(i)
    for i in table:
        if i == "":
            table.remove(i)
    table.append("Great Britain")
    table.append("GB")
    table.append("Greece")
    table.append("GR")



    table_function = particionar_lista(table, 2)
    df = pd.DataFrame(table_function, columns=["country", "country_code"])
    df = df.dropna()  # drop the Nan
    df_scrap = df[["country_code", "country"]]  #reorder the dataframe for the join
    df_scrap = df_scrap['country'].replace('Great Britain', 'United Kingdom')
    df_scrap = df[["country_code", "country"]]  #reorder the dataframe for the join
    final_dataset_raw = pd.merge(final_dataset, df_scrap, how='left', on='country_code')

    mainpath = "/home/jc/Escritorio/Proyectos_finales_ironhack/ih_datamadpt0420_project_m1/data/raw"
    filename = "final_dataset_raw"
    fullpath = os.path.join(mainpath, filename)
    final_dataset_raw.to_csv(fullpath + ".csv", index=False)
    final_dataset_raw.rural.unique()  # let ś understand the data inside the rural column
    final_dataset_raw = final_dataset_raw.replace(
        {"urban": "City", "Country": "Rural", "Non-Rural": "City", "rural": "Rural", "countryside": "Rural",
         "city": "City"})  # homogenise the data into two main categories
    final_dataset_def = final_dataset_raw[["country", "normalized_job_title", "rural", "uuid"]]

    mainpath = "/home/jc/Escritorio/Proyectos_finales_ironhack/ih_datamadpt0420_project_m1/data/raw"
    filename = "final_dataset_def"
    fullpath = os.path.join(mainpath, filename)
    final_dataset_def.to_csv(fullpath + ".csv", index=False)


    print(f'{filename} correctly saved')

    return  final_dataset_def







