# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView

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
