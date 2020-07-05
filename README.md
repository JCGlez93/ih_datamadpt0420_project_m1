# Ironhack data project : MODULE 1

This pipeline extract data from different sources, manipulates it and save the csv locally.
This instructions will allow you to make a copy of the project locally.
Check deployment to understand how  to deploy the project.


![Image](https://res.cloudinary.com/springboard-images/image/upload/q_auto,f_auto,fl_lossy/wordpress/2019/05/aiexcerpt.png)

---

## **Pre-requisites:**

- Python 3.7 (at least)

- Numpy 

- Pandas

- Argsparse

- Sqlalchemy

- os

- Beautiful soap

- Regex

- Time

- Conda

- Pycharm

## **Instalation:**

As a rule of thumb: I do encourage you to install conda, create a working environment and download any library doing : "conda install..."

Example: "conda install numpy"

## **Test execution:**

Any execution must be done from  the terminal using either a fullpath  or shortpath argument  from the main.py file.

Example = "python main.py"

To filter by country use the following = "python main.py -c Spain"



#

**Core technical concepts and inspiration**

The main reason why I created this is to execute a single line of code
that allows you to : extract , wrangle, analyse and visualise data.
Jupyter notebooks are quite good to check your code but quite infficiente when
executing linked functions.

**Usage**

- Parameters: countries (-c , --country)
- return values: it returns a table with the following columns: x,y z
- known issues : you can execute this code in the local directory within the 
correct environment



**Folder structure**
```
└── project
    ├── __trash__
    ├── requeriments.txt
    ├── README.md
    ├── main_script.py
    ├── notebooks
    │   ├── acquisition.ipynb
    │   └── analysis.ipynb
        ├── reporting.ipynb
    │   └── wrangling.ipynb

    ├── p_acquisition
    │   ├── m_acquisition.py
        p_analysis
    │   ├── m_analysis.py
        p_reporting
    │   ├── m_reporting.py
        p_wrangling
    │   ├── m_wrangling.py
    └── data
        ├── raw
        ├── processed
        └── results
        └── .ipynb_checkpoints
        

```

> Do not forget to include `__trash__` and `.env` in `.gitignore` 

**ToDo**
- Next steps: provide more insights from the data extracted



 **Contact info**
Getting help from Octavio and Javier Molins.
Please do email mw for further questions : jcglez93@gmail.com

