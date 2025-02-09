def welcome_msg():
    welcome_msg = "Hello !! Welcome to my data base" 
    base_url = "http://127.0.0.1:8000"

    cont_pop =  {"End Points to get population" : {
        "max_population": f"{base_url}/Continent/Population/max",
        "min_population": f"{base_url}/Continent/Population/min",
        "average_population": f"{base_url}/Continent/Population/average",
        "total_population": f"{base_url}/Continent/Population/total"
    }}

    cont_area = {"End point to get area" : {
        "max_area": f"{base_url}/Continent/Area/max",
        "min_area": f"{base_url}/Continent/Area/min",
        "average_area": f"{base_url}/Continent/Area/average",
        "total_area": f"{base_url}/Continent/Area/total"
    }}

    cont_list ={"End point to get list of countries in continent":f"{base_url}/Continent"}
    return welcome_msg, cont_list, cont_pop, cont_area