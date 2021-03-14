from django.shortcuts import HttpResponse
from django.shortcuts import render
import requests
import json

r = requests.get("https://api.spacexdata.com/v3/launches?limit=100.json")
res = r.json()

def initial(request):
    return  render(request,'home.html')


