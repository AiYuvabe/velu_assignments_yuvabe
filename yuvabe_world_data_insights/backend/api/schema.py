from pydantic import BaseModel,Field

class CountryDetails(BaseModel):
    country_name:str
    continent:str
    population:int
    area:int
    capital:str