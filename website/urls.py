from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('home', views.home_page_view, name='home'),
    path('printer', views.printer_page_view, name='printer'),
    path('aboutme', views.aboutme_page_view, name='aboutme')
]