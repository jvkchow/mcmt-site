from django.shortcuts import render
from rest_framework.views import APIView
from django.views import View
from dotenv import load_dotenv
import os
import base64
import json
from requests import post, get

# Create your views here.
class HomeView(APIView):

    # get application's client ID and client secret
    load_dotenv()
    api_key = os.getenv("API_KEY")
    youtube = build('youtube', 'v3')
    
    def get_token(self):
        None
    
    def get_auth_header(self, token):
        return {"Authorization": "Bearer " + token}

    def display(self, token, search):
        None

    def get(self, request, *args, **kwargs):
        token = self.get_token()
        try:
            None
        except Exception as e:
            return render(request, "home.html")