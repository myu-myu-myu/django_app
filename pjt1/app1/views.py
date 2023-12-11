from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import MusicForm
from .models import Music

class Home(TemplateView):
    template_name = 'home.html'

def music_list(request):
    playlists = Music.objects.all()
    return render(request, 'music_list.html', {
        'playlists': playlists
    })

def upload_music(request):
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('music_list')
    else:
        form = MusicForm()
    return render(request, 'upload_form.html', {
        'form': form
    })

def delete_music(request, pk):
    if request.method == 'POST':
        music = Music.objects.get(pk=pk)
        music.delete()
    return redirect('music_list')
