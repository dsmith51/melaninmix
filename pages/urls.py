from django.urls import path
from .views import home_page_view, ContactView, bios_list, about

urlpatterns = [
    path('', home_page_view, name='home'),
    path('about/', about, name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('bio/', bios_list, name='bio'),
]
