from django.shortcuts import render, redirect
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


# utils

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


def show_genres(request):
    context = {
        'title': 'qazmusic',
        'header_menu': header_menu,
        'tracks': get_tracks(),
        'artists': get_artists()
    }

    return render(request, 'qazmusic/show_genres.html', context=context)


def genre_view(request, genre_id):
    context = {
        'title': 'qazmusic',
        'header_menu': header_menu,
        'tracks': get_tracks(),
        'artists': get_artists(),
        'genre_id': genre_id
    }

    return render(request, 'qazmusic/genre_view.html', context=context)


def show_charts(request):
    context = {
        'title': 'qazmusic',
        'header_menu': header_menu,
        'tracks': get_tracks(),
        'charts': get_charts()
    }

    return render(request, 'qazmusic/show_charts.html', context=context)


def chart_view(request, chart_id):
    context = {
        'title': 'qazmusic',
        'header_menu': header_menu,
        'tracks': get_tracks(),
        'artists': get_artists(),
        'charts': get_charts(),
        'chart_id': chart_id
    }

    return render(request, 'qazmusic/chart_view.html', context=context)


def show_lyrics(request):
    context = {
        'title': 'qazmusic',
        'header_menu': header_menu,
        'lyric': get_lyrics(),
        'artists': get_artists(),
        'tracks': get_tracks()
    }

    return render(request, 'qazmusic/show_lyrics.html', context=context)


def lyric_view(request, lyric_id):
    context = {
        'title': 'qazmusic',
        'header_menu': header_menu,
        'tracks': get_tracks(),
        'artists': get_artists(),
        'lyric_id': lyric_id
    }

    return render(request, 'qazmusic/lyric_view.html', context=context)


def show_archive(request):
    context = {
        'title': 'Golden fund',
        'header_menu': header_menu,
        'tracks': get_tracks(),
        'artists': get_artists(),
        'genre_id': 3
    }
    return render(request, 'qazmusic/genre_view.html', context=context)


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


def update_track(request, pk):
    succesful = False
    track = Tracks.objects.get(pk=pk)
    form = Upload_Music(instance=track)
    if request.method == 'POST':
        form = Upload_Music(request.POST, instance=track)
        if form.is_valid():
            succesful = True
            form.save()

    context = {
        'title': 'qazmusic - Upload',
        'header_menu': header_menu,
        'form': form,
        'genres': get_genres(),
        'artists': get_artists(),
        'upload_message': succesful
    }

    return render(request, 'qazmusic/upload.html', context=context)


def delete_track(request, pk):
    track = Tracks.objects.get(pk=pk)
    form = Upload_Music(instance=track)
    if request.method == 'POST':
        track.delete()
        return redirect('/artists')

    context = {
        'title': 'qazmusic - Upload',
        'header_menu': header_menu,
        'form': form,
        'item': track
    }
    return render(request, 'qazmusic/delete_track.html', context=context)
