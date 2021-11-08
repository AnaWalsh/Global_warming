import pandas as pd
import numpy as np
from numpy import nan
import re
import sys


import os
from dotenv import load_dotenv

import requests

from bs4 import BeautifulSoup


sys.path.append('/Users/awalsh/Ironhack/PROYECTOS/W3-pipelines-project/src')
import cleaning_functions as cf

df_population = pd.read_csv('../Data/WorldPopulation.csv') 

df_population.head()

df_population['Year']

df_population.isna().sum()

#We delete the columns we don't need for the hypothesis, and we are left with "Year" and "Population."
df_population.drop(["ChangePerc", "NetChange", "Density", "Urban",
       "UrbanPerc"], axis=1, inplace=True)

df_population = df_population.set_index("Year")
df_population.head()


#2. Web Sraping: "Ocean Temperature" and final df

final_df = cf.buildCompleteDataframe(cf.getAverageOceanTemperatureByDecade(), cf.buildDictionaryOfPopulationFrom(1950, 2020, df_population), 1950, 2010)


final_df.columns=['Decade','Temperature','Population']

display(final_df)

final_df = final_df.astype({"Population":int})

df_population.to_csv('../Data/clean_WorldPopulation.csv')

final_df.to_csv('../Data/final_df.csv')

#3. Import DataSet: CO2 Concentrations

df_co2 = pd.read_csv('../Data/monthly-atm-co2.csv') 
display(df_co2)
df_co2.keys()
df_co2.isna().sum()
list(df_co2['Entity'].unique())
list(df_co2['Day'].unique())

df_co2.drop(["Code", "trend_co2_concentrations"], axis=1, inplace=True)

df_co2.to_csv('../Data/df_co2.csv', index= False)



