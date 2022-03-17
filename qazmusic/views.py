from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .utils import *


def index(request):
    context = {
        'title': 'qazmusic',
        'header_menu': header_menu,
        'tracks': get_tracks(),
        'username': 'Aibolat Batyrov'
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
        'title': fullname,
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
        'artists': get_artists(),
        'genres': get_genres()
    }

    return render(request, 'qazmusic/show_genres.html', context=context)


def genre_view(request, genre_id, title):
    context = {
        'title': title,
        'header_menu': header_menu,
        'tracks': get_tracks(),
        'artists': get_artists(),
        'genres': get_genres(),
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
        'chart_id': chart_id,
        'tracks_in_chart': get_charts_tracks(chart_id)
    }

    return render(request, 'qazmusic/chart_view.html', context=context)


def show_lyrics(request):
    context = {
        'title': 'qazmusic',
        'header_menu': header_menu,
        'lyric': get_lyrics(),
        'artists': get_artists(),
        'tracks': get_tracks(),
        'lyrics': get_lyrics()
    }

    return render(request, 'qazmusic/show_lyrics.html', context=context)


def lyric_view(request, lyric_id):
    lyric = get_lyrics().get(pk=lyric_id)
    track = get_tracks().get(pk=lyric.track_id_id)
    artist = get_artists().get(pk=track.artist_id)
    context = {
        'title': 'qazmusic',
        'header_menu': header_menu,
        'tracks': get_tracks(),
        'artists': get_artists(),
        'lyric': lyric,
        'lyric_id': lyric_id,
        'track_title': track.title,
        'artist_photo': artist.photo
    }

    return render(request, 'qazmusic/lyric_view.html', context=context)


def show_archive(request):
    context = {
        'title': 'Golden fund',
        'header_menu': header_menu,
        'tracks': get_tracks(),
        'artists': get_artists(),
        'genres': get_genres(),
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
