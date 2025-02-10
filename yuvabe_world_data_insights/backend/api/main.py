from fastapi import FastAPI
import os
import sys
src_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "backend"))
sys.path.append(src_directory)
from modules import home_page
from api.schema import CountryDetails
from utils import logger

app = FastAPI()

# file_path =  "C:/Users/Vijay/Downloads/world_population.csv"
df = home_page.process_data()

@app.get("/")
def display_data():
    return df.to_csv()

@app.get("/ShowAllContinents")
def display_continents():
    continents = home_page.display_continents(df)
    return continents.tolist()

@app.get("/ShowAllCountries")
def display_countries():
    countries = home_page.display_countries(df)
    return countries.tolist()

@app.get("/ShowContinentwithHighestPopulation")
def display_cont_with_high_pop():
    highest_pop = home_page.continent_with_highest_population(df)
    return  highest_pop

@app.get("/ShowContinentwithLowestPopulation")
def display_cont_with_high_pop():
    lowest_pop = home_page.continent_with_lowest_population(df)
    return  lowest_pop

@app.get("/ShowCountrywithHighestPopulation")
def display_country_with_high_pop():
    highest_pop = home_page.country_with_highest_population(df)
    return  highest_pop

@app.get("/ShowCountrywithLowestPopulation")
def display_country_with_high_pop():
    lowest_pop = home_page.country_with_lowest_population(df)
    return  lowest_pop
























# highest_pop = home_page.display_countries(df).tolist()
# print(type(highest_pop))

# @app.get("/")
# def home():
#     return end_points.welcome_msg()
    
# @app.get('/{continent}')
# def present_countries(continent : str):
#     return home_page.list_country_by_continent(df, continent)


# @app.get("/{continent}/{data_type}/{stat}") 
# def get_stats_of_cont(continent:str, data_type : str, stat:str):
#     return home_page.get_stat_by_continent(df,continent,data_type,stat)

# @app.get("/{key}/{value}")
# def get_stats_of_cont(key : str ,value : str):
#     return home_page.get_continent_with_max_value(df, key, value)


  