from django.urls import path
from app2.views import *
app2_name='everything'
urlpatterns=[
    path('virat/',virat,name='virat'),
    path('sky/',sky,name='sky'),
]

