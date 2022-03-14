from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('artists', artists_view, name='artists'),
    path('artist/<int:artist_id>/<slug:fullname>', artist_page, name='artist-view'),
    path('genres', show_genres, name='genres'),
    path('genre/<int:genre_id>/<slug:title>', genre_view, name='genre_view'),
    path('charts', show_charts, name='charts'),
    path('chart/<int:chart_id>', chart_view, name='chart_view'),
    path('lyrics', show_lyrics, name='lyrics'),
    path('lyric/<int:lyric_id>', lyric_view, name='lyrics'),
    path('archive/golden-fund', show_archive, name='archive'),
    path('upload', upload, name='upload')
]
