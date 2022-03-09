from django import forms
from .models import *


class Upload_Music(forms.ModelForm):
    artists = forms.CharField(max_length=255, label='Artists',
                              widget=forms.TextInput(attrs={'placeholder': 'Kairat Nurtas, Toregali Toreali'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['genre'].empty_label = "Genre not selected"

    class Meta:
        model = Tracks
        fields = ('title', 'genre', 'published_date', 'file')
        widgets = {
            'published_date': forms.TextInput(attrs={'placeholder': '2022-03-08'}),
        }
