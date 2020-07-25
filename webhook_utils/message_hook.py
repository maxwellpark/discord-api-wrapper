#!/usr/bin/env python3
import os 
import sys 
import requests 
import urllib.request

if len(sys.argv) > 2:
    raise ValueError("Too many arguments.")

message = sys.argv[1] 
print(message) 

hook_url = os.getenv("HOOK_URL") 

requests.post(hook_url, data=message)
