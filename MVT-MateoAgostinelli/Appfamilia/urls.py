from xml.etree.ElementInclude import include
from django.urls import path
from Proyecto1 import view


urlpatterns = [
    path('',view.inicio),
    path('familia',view.familia),
]