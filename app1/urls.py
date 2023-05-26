from django.urls import path
from app1.views import *
app_name='something'
urlpatterns=[
    path('rohit/',rohit,name='rohit'),
    path('dhoni/',dhoni,name='dhoni'),
]