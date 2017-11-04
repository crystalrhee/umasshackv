from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^song/$', views.SongPageView.as_view(), name='song'),
    url(r'^map/$', views.MapPageView.as_view(), name='map'),
]