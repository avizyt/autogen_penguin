# filename: download_penguins.py
import requests

url = "https://raw.githubusercontent.com/vega/vega-datasets/main/data/penguins.json"
response = requests.get(url)

with open("penguins.json", "wb") as f:
    f.write(response.content)