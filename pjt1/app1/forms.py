from django import forms

from .models import Music

class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ('skater', 'title', 'length', 'music')
