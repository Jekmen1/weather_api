from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
import requests, json
# Create your views here.
class WeatherApi(APIView):

    def get(self, request, temp):
        API_KEY = "509d1236aab16bb823897a206a5b2fd0"
        city_name = temp
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units={'metric'}"
        response = requests.get(url)
        j = json.loads(response.text)
        city = j['main']['temp']
        return Response({"Your city's weather": city})
