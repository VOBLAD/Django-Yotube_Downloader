from django.shortcuts import render
from pytube import YouTube
import os

def index(request):
    return render(request, 'yodo2/index.html')


def download(request):
    global url
    url = request.GET.get('url')
    yt = YouTube(url)
    video = []
    video = yt.streams.filter(progressive=True).all()
    title = yt.title
    context = {'video': video, 'title': title}
    return render(request, 'yodo2/download.html', context)


def done(request):
    global url
    YouTube(url).streams.get_highest_resolution().download()
    return render(request, 'yodo2/done.html')


def mp3(request):
    global url
    yto = YouTube(url)
    video = yto.streams.filter(only_audio=True).first()
    out_file = video.download()
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    return render(request, 'yodo2/done.html')
