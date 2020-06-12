#!/usr/bin/env python3
import requests 
import urllib.request
import json 
import time
import os 
from bs4 import BeautifulSoup

site_url = "https://www.gearnews.com/zone/musictech/"
site_response = requests.get(site_url)
soup = BeautifulSoup(site_response.text, "html.parser")

hook_url = "https://discordapp.com/api/webhooks/721006255769911296/6B-oBFipczhGGHGmI8iWRT5_S87C9vtySjjwBsD4dqeWD-NAAmq9Edcm4pcFZCK5cdFZ"

h2 = soup.find_all("h2")
first_link = h2[0].a.get("href")
print(first_link)

latest = False 

with open("latest_link.txt", "r") as file:
    data = file.read()
    if (first_link == data): 
        latest = False 
    else: 
        latest = True 

if (latest):
    with open("latest_link.txt", "w") as file:
        file.write(first_link)

    message = {"content": first_link} 
    requests.post(hook_url, data=message)
