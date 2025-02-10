import pandas as pd
import os
import sys
src_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "backend"))
sys.path.append(src_directory)
from utils import logger


file_path =  "C:/Users/Vijay/Downloads/world_population.csv"
# data_frame = pd.read_csv(file_path)

def process_data():
    try:
        logger.log("I'm going to read the csv")
        data_frame = pd.read_csv(file_path)
        logger.log("I'm reading the csv")
        return data_frame
    except Exception as e :
        logger.log("I couldn't read the file")
        return f"Unable to read the file {e}"
    
def display_continents(dataframe):
    continents = dataframe['Continent'].unique()
    logger.log("Displaying the list of continents in the data")
    return continents

def display_countries(dataframe):
    countries = dataframe['Country'].values
    logger.log("Displaying the list of countries in the data")
    return countries

def continent_with_highest_population(dataframe):
    highest= dataframe.groupby('Continent')['Population'].agg(total_population = 'sum')
    max_continent = highest.idxmax().item()
    max_population = highest.max().item()
    result = {max_continent:max_population}
    logger.log("Displaying the continent with highest population in the data")
    return result

def continent_with_lowest_population(dataframe):
    lowest= dataframe.groupby('Continent')['Population'].agg(total_population = 'sum')
    min_continent = lowest.idxmin().item()
    min_population = lowest.min().item()
    result = {min_continent:min_population}
    logger.log("Displaying the continent with lowest population in the data")
    return result

def country_with_lowest_population(dataframe):
    index= dataframe['Population'].idxmin()
    min_country = dataframe['Country'][index]
    min_population = dataframe['Population'][index]
    result = {min_country:min_population.item()}
    logger.log("Displaying the country with lowest population in the data")
    return result

def country_with_highest_population(dataframe):
    index= dataframe['Population'].idxmax()
    max_country = dataframe['Country'][index]
    max_population = dataframe['Population'][index]
    result = {max_country:max_population.item()}
    logger.log("Displaying the country with highest population in the data")
    return result

























    

def list_country_by_continent(dataframe,continent):
    try:
        df_countries = dataframe[dataframe['Continent'] == continent]
        countries= df_countries['Country'].to_list()
        logger.log("Separated data by continent")
        return countries
    except Exception as e:
        return f"{e}"

def get_stat_by_continent(df ,continent: str, data_type: str, stat: str , ):

    if continent.lower() == "NorthAmerica".lower():
        continent = "North America"
    if continent.lower() == "SouthAmerica".lower():
        continent = "South America"

    valid_stats = ['max', 'min', 'mean' , 'sum' , 'count']
    if stat not in valid_stats:
        return f"Invalid stat. Please use one of the following: {valid_stats}."
    
    continent_population_stats = df.groupby('Continent')[data_type].agg(
        Maximum='max', Minimum='min', Average = 'mean',Total='sum' , Number_of_Countries = 'count')
    
    continent_countries = df[df['Continent'] == continent]

    if continent not in continent_population_stats.index:
        return f"Continent '{continent}' not found in the data."
    
    if stat == 'max':
        population_result = continent_population_stats.loc[continent]['Maximum']
        country_id = continent_countries.loc[continent_countries[data_type].idxmax()]
        country_name = country_id['Country']
        population_value = country_id[data_type]
        return f"{continent}'s {stat} {data_type} is {int(population_result)}. Country: {country_name} , {data_type} :{population_value}"
    if stat == 'min':  
        population_result = continent_population_stats.loc[continent]['Minimum']
        country_id = continent_countries.loc[continent_countries[data_type].idxmin()]
        country_name = country_id['Country']
        population_value = country_id[data_type]
        return f"{continent}'s {stat} {data_type} is {int(population_result)}. Country: {country_name} , {data_type} :{population_value}"
    if stat == 'mean':
        population_result = continent_population_stats.loc[continent]['Average']
        return f"{continent}'s average {data_type} is {int(population_result)}"
    if stat == 'sum':
        population_result = continent_population_stats.loc[continent]['Total']
        return f"{continent}'s total {data_type} is {int(population_result)}"
    if stat == 'count' :
        population_result = continent_population_stats.loc[continent]['Number_of_Countries']
        return f"Total countries in {continent} is {int(population_result)}"
    
def get_continent_with_max_value(dataframe, key, value):
    max_id = dataframe[value].idxmax()
    value_num = dataframe[value][max_id]
    value_country = dataframe[key][max_id]
    return f"{value_country}'s max {value} is {value_num}"


