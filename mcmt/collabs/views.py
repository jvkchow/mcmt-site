from django.shortcuts import render
from rest_framework.views import APIView
from django.views import View
import base64
import json
import requests
from django.conf import settings

# Create your views here.
class CollabView(APIView):

    '''
    Starting Link: https://www.youtube.com/watch?v=
    ID: everything after the end of the link 

    Example: https://www.youtube.com/watch?v=qxAp4qnSkaU
    ID: qxAp4qnSkaU

    API Overview: https://developers.google.com/youtube/v3/docs/videos/list?apix_params=%7B%22part%22%3A%5B%22snippet%22%5D%2C%22id%22%3A%5B%22qxAp4qnSkaU%22%5D%7D
    Useful Github Link: https://github.com/PrettyPrinted/youtube_video_code/blob/master/2019/07/27/Django%20Example%20App%20-%20YouTube%20Search%20With%20YouTube%20Data%20API/django_youtube_search/youtube_search/search/views.py
    
    Form Input:
    * Category/description of what kind of collab?
    
    '''

    def get_collabs(self, video_ids):
        videos_url = 'https://www.googleapis.com/youtube/v3/videos'
        
        video_params = {
            'key' : settings.API_KEY,
            'part' : 'snippet',
            'id' : video_ids
        }

        res = requests.get(videos_url, params=video_params)
        json_res = json.loads(res.content)

        print(video_params)
        
        collabs = []
        for vid in json_res["items"]:
            collab_info = {}
            collab_info["url"] = ''.join(["https://www.youtube.com/watch?v=", vid["id"]])
            collab_info["date"] = vid["snippet"]["publishedAt"]
            collab_info["title"] = vid["snippet"]["title"]
            collab_info["thumbnail"] = vid["snippet"]["thumbnails"]["maxres"]["url"]
            collab_info["channel"] = vid["snippet"]["channelTitle"]

            collabs.append(collab_info)

        return collabs


    def post(self, request, *args, **kwargs):
        None

    def get(self, request, *args, **kwargs):
        try:
            test_ids = 'qxAp4qnSkaU,a0UFPrFbuwQ'
            collabs = self.get_collabs(test_ids)
            return render(request, "collabs.html", {"collabs":collabs})
        except Exception as e:
            print('except')
            return render(request, "home.html")