from django.urls import path, include
from .views import *

urlpatterns = [
    path('', QazmusicHome.as_view(), name='home'),
    path('artists', ShowArtists.as_view(), name='artists'),
    path('artist/<int:artist_id>-<slug:fullname>/', ArtistView.as_view(), name='artist-view'),
    path('genres', ShowGenres.as_view(), name='genres'),
    path('genre/<int:genre_id>_<slug:title>', GenreView.as_view(), name='genre-view'),
    path('charts', ShowCharts.as_view(), name='charts'),
    path('chart/<int:chart_id>', ChartView.as_view(), name='chart_view'),
    path('lyrics', ShowLyrics.as_view(), name='lyrics'),
    path('lyric/<int:lyric_id>_<str:track_title>', LyricView.as_view(), name='lyric-view'),
    path('archive/golden-fund', show_archive, name='archive'),
    path('upload', upload, name='upload'),
    path('update/<str:pk>', update_track, name='update'),
    path('delete/<str:pk>', delete_track, name='delete_track'),
]
