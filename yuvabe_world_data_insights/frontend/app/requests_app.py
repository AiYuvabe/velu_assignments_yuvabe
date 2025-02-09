import requests

def get_api(end_point : str = None):
    r = requests.get(f"http://127.0.0.1:8000/{end_point}")
    return r.json()