# W3-pipelines-project
In this repository you can find a project that consists of using a dataset to analyze a specific topic and complement the information using an API or web scraping.The repository is divided into several folders containing the following files:

1. README
2. "Cleaning_data.ipynb" : in this file the cleaning methods are applied. The functions that are applied are obtained from the file.
3. "Visualization.ipynb": in this file the data are visualized by means of graphics, using seaborn.

4. Folder src: "data_extraction.py": in this file are the functions used for data cleaning. 4. "visualization_functions.py": the purpose of this file was to contain the functions used for data visualization, but in this case, it was not necessary to use any functions.

5. main.py : this file contains all the changes made to the data and the results obtained.

# Objective
The objective of this project is to test through data whether the hypothesis formulated is true.

# Hypothesis
The increase in ocean temperatures in recent decades is related to population growth.

# DataSets
Two DataSets have been used for this project:
- World Population by Year (Kaggle)
- Global atmospheric CO2 Concentration (https://ourworldindata.org/grapher/monthly-atm-co2?country=~OWID_WRL)


# Web scraping

The ocean temperature data have been extracted from the table found at the following URL: https://www.currentresults.com/Environment-Facts/changes-in-earth-temperature.php


# Conclusion

As can be seen in the graphs, there is a notable increase in the temperature of the oceans at the same time as population growth. This is due to the increase of CO2, and other greenhouse gases, which have also grown significantly during the last decades, especially since the 1950s as can be seen in the analysis.

# Libraries

The following libraries have been used for this project: 

pandas
numpy
seaborn

