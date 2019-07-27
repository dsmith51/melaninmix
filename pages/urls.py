from django.urls import path
from .views import home_page_view, ContactView, bios_list, about
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home_page_view, name='home'),
    path('about/', about, name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('bio/', bios_list, name='bio'),
]

urlpatterns += staticfiles_urlpatterns()