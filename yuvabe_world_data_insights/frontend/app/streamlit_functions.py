import os
import sys
src_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "main"))
sys.path.append(src_directory)
import requests_app

def choose_data_view(st_interface):
    data_view_options  = [
    "Select an option",
    "Show All Continents",
    "Show All Countries",
    "Show Continent with Highest Population",
    "Show Continent with Lowest Population",
    "Show Country with Highest Population",
    "Show Country with Lowest Population"
    ]
    selected_option = st_interface.selectbox("Select Data to Display", data_view_options)
    return selected_option

def display_contents(option, streamlit):
    try:
        cont = requests_app.get_api(option)
        continents = streamlit.table(cont)
        return continents
    except Exception as e:
        streamlit.error(f"An error occurred while processing the CSV: {e}")

# def display_countries(option, streamlit):
#     cont = requests_app.get_api(option)
#     return streamlit.table(cont)

# def display_continent_with_highest_population(option, streamlit):
#     cont = requests_app.get_api(option)
#     return streamlit.table(cont)

# def display_country_by_continents(selected_continent,streamlit):
#     if selected_continent is not "Choose a continent to display countries":
#             countries_list = requests_app.get_api(selected_continent)
#             streamlit.table(countries_list)

















    # else:
    #         streamlit.warning("Please select a valid continent.")
        #     selected_continent = streamlit.selectbox(
    #     "Select a continent",["Choose a continent to display countries"] + list(df['Continent'].unique()),)



          