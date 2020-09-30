import pandas as pd
import matplotlib.pyplot as plt 
from datetime import datetime as dt 
from graph import graph 

def to_celcius(f):
    return (f - 32) * 5 / 9

def parse_csv(filename):
    data = pd.read_csv(filename, sep=";")

    # format date and set cloumn as index
    data["Date"] = pd.to_datetime(data["Date"], format="%d.%b")
    data["Date"] = data["Date"].dt.strftime("%d.%m.2019")
    data.set_index("Date")

    # format time
    data["Time"] = pd.to_datetime(data["Time"]).dt.strftime("%H:%M")

    # format humidity
    data["Humidity"] = data["Humidity"].str.rstrip('%').astype('float') / 100.0

    # format wind speed
    data["Wind Speed"] = data["Wind Speed"].str.rstrip(' mph').astype(int)

    # format gust
    data["Wind Gust"] = data["Wind Gust"].str.rstrip(' mph').astype(int)

    # fahrenheit to celcius
    data["Temperature"] = to_celcius(data["Temperature"]).astype(int)

    return data

df = parse_csv("DATABASE.csv")
print(df.columns)

graph(df, "Wind", "Condition")
