# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# Create your views here.

class HomePageView(TemplateView):
	template_name = "index.html"

class AboutPageView(TemplateView):
	template_name = "about.html"

class SongPageView(TemplateView):
    def get(self, request, **kwargs):
        context = {
            'data': [
                {
                    'temperature': '65 degrees',
                    'song': 'https://www.youtube.com/watch?v=JyNYkWKHf1Q'
                }
            ]
        }

        return render(request, 'song.html', context)

class MapPageView(TemplateView):
    def get(self, request, **kwargs):
        context = {
            'data': [
                {
                    'temperature': '65 degrees',
                    'zip': '02115'
                }
            ]
        }

        return render(request, 'map.html', context)
        
def spotify_request(request, bpm):
    client_credentials_manager = SpotifyClientCredentials(
        client_id='client_id', 
        client_secret='client_secret'
    )
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 
    return HttpResponse("Here's the text of the Web page.")
