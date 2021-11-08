
import pandas as pd
import numpy as np
from numpy import nan
import re
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup





def getAverageOceanTemperatureByDecade():
    """
    This function is a web scraping function. It extracts the content from a table in the URL and it stores it a dictionary.
    Arggs:
    - Table
    Returns:
     Dictionary
    """
    URL = "https://www.currentresults.com/Environment-Facts/changes-in-earth-temperature.php"
    page = requests.get(URL)
    results = BeautifulSoup(page.content, "html.parser")
    table = results.find('table', class_='articletable tablecol-1-left revcolr')

    a = {}

    for row in table.tbody.find_all('tr'):
        columns = row.find_all('td')
        a[int(columns[0].text.strip()[:-1])] = columns[1].text.strip()

    return a


def buildDictionaryOfPopulationFrom(decadeStart, decadeEnd, df):
    """
    This function stores in a dictionary the values from a column in 
    Arggs:()
    - ()
    Returns:
     Dictionary
    """
    d = {}
    for i in range(decadeStart, decadeEnd, 10):
        d[i] = average_on_decade(df, i)
    return d


def average_on_decade(df, decade):
    """
    This function calculates the average of 10 values in a range from a df.
    Arggs:
    - ()
    Returns:
    a)Total value of the items in the range divided by the number of items.
    b)Total value of the items in the range divided by one less of the number of items. 
    """
    total_items = 10
    count_total = 0
    for i in range(decade, decade + 9):
        try:
            count_total += df.loc[i].Population
        except KeyError:
            total_items -= 1

    return count_total / total_items


def buildCompleteDataframe(temperatura: dict, poblacion: dict, since, till):
    """
    This function builds a df from dictionaries and a list in a df..
    Arggs:
    - (Temperature dictionary, population dictionary and list of )
    Returns:
    a)Total value of the items in the range divided by the number of items.
    b)Total value of the items in the range divided by one less of the number of items. 
    """
    dictionary = {}
    index_counter = 0

    for i in range(since, till, 10):
        
        list_of_temp_population = []
        
        list_of_temp_population.append(i)
        
        if temperatura.get(i) is not None:
            list_of_temp_population.append(temperatura.get(i))
        else:
            list_of_temp_population.append("0")
            
            
        if poblacion.get(i) is not None:
            list_of_temp_population.append(poblacion.get(i))
        else:
            list_of_temp_population.append("0")
            
        dictionary[index_counter] = list_of_temp_population
        
        index_counter+=1 

        
    return pd.DataFrame.from_dict(dictionary, orient='index')
