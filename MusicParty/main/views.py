from django.shortcuts import render
from .models import Playlist
from .forms import CreatePlaylistForm

# Create your views here.

def home(response):
    return render(response, "main/home.html", {})

def CreatePlaylist(response):
    if response.method == "POST":
        form = CreatePlaylistForm(response.POST)
        if form.is_valid():
            print("Form is valid")
            name = form.cleaned_data["name"]
            description = form.cleaned_data["description"]
            print(name, description)
            playlist = Playlist(name=name, description=description)
            playlist.save()
    return render(response, "main/CreatePlaylist.html", {"form": CreatePlaylistForm()})


def ViewPlaylist(response, id):
    ls = Playlist.objects.get(id=id)
    songs = ls.song_set.all()
    return render(response, "main/ViewPlaylist.html", {"ls": ls, "songs": songs})

def ListPlayLists(response):
    playlists = Playlist.objects.all()
    return render(response, "main/ListPlaylists.html", {"playlists": playlists})