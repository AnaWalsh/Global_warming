
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
    This is a web scraping function. It extracts the content from a table in the URL and it stores it a dictionary.
    Arggs:
    ()
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
    This function stores in a dictionary the decade and average values for the population of each decade. 
    Arggs:
     decadeStart, decadeEnd, df
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
    ()
    Returns:
    a)Average in a decade (total value of the items in the range divided by the number of items).
    b)Average in a decade (Total value of the items in the range divided by one less of the number of items). 
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
    This function builds a df from dictionaries and a list in a df.
    Arggs:
    - (Temperature dictionary(2000 : "13.5"), population dictionary (2000 : 7003495863047), since(year), till(year)
    Returns:
    a)Total value of the items in the range divided by the number of items.
    b)Total value of the items in the range divided by one less of the number of items. 
    """
    dictionary = {}
    index_counter = 0

    for i in range(since, till, 10):
               # this is the list of decade         
        list_of_temp_population = []
       # to fill the first value of the row 
        list_of_temp_population.append(i)
        
        if temperatura.get(i) is not None:
            list_of_temp_population.append(temperatura.get(i))
        else:
            list_of_temp_population.append("0")
            
            
        if poblacion.get(i) is not None:
            list_of_temp_population.append(poblacion.get(i))
        else:
            list_of_temp_population.append("0")

          # {decada: año, temperatura, poblacion}   
        dictionary[index_counter] = list_of_temp_population
        #{0 : ["1950", "13.5", 123456789]}
        index_counter+=1 

        
    return pd.DataFrame.from_dict(dictionary, orient='index')
