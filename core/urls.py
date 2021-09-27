from django.urls import path
from .views import index, getProfiles, create, form


app_name = 'index'
urlpatterns = [
    path('', index, name='index'),
    path('getProfiles', getProfiles, name='getProfiles'),
    path('form/', form, name='form'),
    path('create', create, name='create'),
]
