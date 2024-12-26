import requests
import json

def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "centimeter":100,
        "meter": 1,
        "feet": 3.28084,
        "inche": 39.3701,
        "kilometer": 0.001,
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]


def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    
    
def convert_weight(val,from_unit,to_unit):
    conversion={
        "Gram":1000,
        "Kilogram":1,
        "Pound":2.20462,
        "Ounce":35.274
    }
    return val * conversion[to_unit]/conversion[from_unit]



def convert_time(val,from_unit,to_unit):
    conversion={
        "Second":3600,
        "Minute":60,
        "Hour":1,
        "Day":0.0416667,
    }
    return val * conversion[to_unit]/conversion[from_unit]
    
    
def convert_speed(val,from_unit,to_unit):
    conversion={
        "kph":3.6,
        "mps":1
    }
    return val * conversion[to_unit]/conversion[from_unit]
    
api_key="api"
def convert_currency(val,from_unit,to_unit):
    if from_unit==to_unit:
        return val
    response=requests.get(f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_unit}").json()["conversion_rates"]
    return val * response[to_unit]

    
