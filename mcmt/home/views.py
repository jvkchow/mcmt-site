from django.shortcuts import render
from rest_framework.views import APIView
from django.views import View
import base64
import json
import requests

# Create your views here.
class HomeView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            return render(request, "home.html")
        except Exception as e:
            return render(request, "home.html")