import pdb

from django.shortcuts import render
from .models import *
from .forms import *

header_menu = {
    'Artists': 'artists',
    'Genres': 'genres',
    'Charts': 'charts',
    'Lyrics': 'lyrics',
    'Golden fund': 'archive',
    'Upload music': 'upload'
}


# useful objects

def get_tracks():
    get_tracks = Tracks.objects.all()
    return get_tracks


def get_artists():
    get_artists = Artists.objects.all()
    return get_artists


def get_genres():
    get_genres = Genres.objects.all()
    return get_genres


def get_charts():
    get_charts = Charts.objects.all()
    return get_charts


def get_lyrics():
    get_lyrics = Lyrics.objects.all()
    return get_lyrics


def get_tracks_artists(id):
    tracks_artists = TracksArtist.objects.filter(artist_id=id)
    return tracks_artists


# view functions

def index(request):
    context = {
        'title': 'qazmusic',
        'header_menu': header_menu,
        'tracks': get_tracks()
    }
    return render(request, 'qazmusic/index.html', context=context)


def artists_view(request):
    context = {
        'title': 'qazmusic',
        'header_menu': header_menu,
        'tracks': get_tracks(),
        'artists_list': get_artists()
    }
    return render(request, 'qazmusic/artists.html', context=context)


def artist_page(request, artist_id, fullname):
    context = {
        'title': 'qazmusic',
        'header_menu': header_menu,
        'tracks': get_tracks(),
        'artists': get_artists(),
        'artist_id': artist_id,
        'tracks_artists': get_tracks_artists(artist_id)
    }

    return render(request, 'qazmusic/artist-view.html', context=context)


def upload(request):
    succesful = False
    if request.method == 'POST':
        form = Upload_Music(request.POST, request.FILES)
        if form.is_valid():
            succesful = True
            form.save()

    else:
        form = Upload_Music()

    context = {
        'title': 'qazmusic - Upload',
        'header_menu': header_menu,
        'form': form,
        'genres': get_genres(),
        'artists': get_artists(),
        'upload_message': succesful
    }
    return render(request, 'qazmusic/upload.html', context=context)
