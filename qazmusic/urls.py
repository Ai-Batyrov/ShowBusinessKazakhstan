from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('artists', artists_view, name='artists'),
    path('artist/<int:artist_id>/<slug:fullname>', artist_page, name='artist-view'),
    path('genres', index, name='genres'),
    path('charts', index, name='charts'),
    path('lyrics', index, name='lyrics'),
    path('archive', index, name='archive'),
    path('upload', upload, name='upload')
]
