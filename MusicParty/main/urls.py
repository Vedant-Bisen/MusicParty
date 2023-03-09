from django.urls import path
from . import views
urlpatterns = [
    path("", name="home", view=views.home),
    path("createplaylist/", name="CreatePlaylist", view=views.CreatePlaylist),
    path("viewplaylist/<int:id>", name="ViewPlaylist", view=views.ViewPlaylist),
    path("listplaylists/", name="ListPlaylists", view=views.ListPlayLists),
]
