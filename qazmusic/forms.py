from django import forms
from .models import *


class Upload_Music(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['genre'].empty_label = "Genre not selected"
        self.fields['artist'].empty_label = "Artist not selected"

    class Meta:
        model = Tracks
        fields = ('title', 'artist', 'genre', 'published_date', 'file')
        widgets = {
            'published_date': forms.TextInput(attrs={'placeholder': '2022-03-08'}),
        }
