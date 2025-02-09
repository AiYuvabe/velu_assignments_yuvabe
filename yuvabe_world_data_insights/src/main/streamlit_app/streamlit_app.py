import os
import sys
src_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "main"))
sys.path.append(src_directory)
import streamlit as st
from modules import home_page
import streamlit_functions
from utils import logger

st.title("World Population Data")
csv_file = st.file_uploader("Choose a CSV file", type=['csv'])

if csv_file:
    choosen_data = streamlit_functions.choose_data_view(st)
    if choosen_data == "Show All Continents":
        opt = choosen_data.replace(" ","")
        streamlit_functions.display_contents(opt, st)
    if choosen_data == "Show All Countries":
        opt = choosen_data.replace(" ","")
        streamlit_functions.display_contents(opt, st)
    if choosen_data == "Show Continent with Highest Population":
        opt = choosen_data.replace(" ","")
        streamlit_functions.display_contents(opt, st)
    if choosen_data == "Show Continent with Lowest Population":
        opt = choosen_data.replace(" ","")
        streamlit_functions.display_contents(opt, st)
    if choosen_data == "Show Country with Highest Population":
        opt = choosen_data.replace(" ","")
        streamlit_functions.display_contents(opt, st)
    if choosen_data == "Show Country with Lowest Population":
        opt = choosen_data.replace(" ","")
        streamlit_functions.display_contents(opt, st)
    








    # selected_stat = st.selectbox("Select the stat",stat_list)
    # list_of_selected_cont = home_page.list_country_by_continent(df,selected_continent)
    # selected_key = st.selectbox("Select the key's to fetch data:",df.keys())
    # max_population = home_page.get_continent_with_max_pop(df)
    # st.write(f"Countries data in {selected_continent}:", list_of_selected_cont)
    # st.write(f"{selected_continent}'s with max population is :",max_population)

