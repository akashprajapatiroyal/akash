import requests
url = requests.get("https://data.covid19india.org/data.json")
coviddata = url.json()

print(coviddata["cases_time_series"][0])