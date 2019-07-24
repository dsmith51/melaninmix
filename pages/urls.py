from django.urls import path
from .views import HomePageView, AboutPageView, ContactView, \
    BioView, EpisodeView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('bio/', BioView.as_view(), name='bio'),
    path('episode/season/<int:id>', EpisodeView.as_view(), name='episode')
]
