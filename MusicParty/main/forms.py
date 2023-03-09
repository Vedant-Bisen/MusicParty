from django import forms

class CreatePlaylistForm(forms.Form):
    name = forms.CharField(label='Playlist Name', max_length=100)
    description = forms.CharField(label='Description', max_length=1000)