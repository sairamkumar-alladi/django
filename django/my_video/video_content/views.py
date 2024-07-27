from django.shortcuts import render,redirect
from .models import Video
# Create your views here.


def display(request):
    videos = Video.objects.all()

    context = {
        'videos':videos
    }

    return render(request, 'videos.html',context)

def upload(request):
    if request.method == 'POST':
        title = request.POST['title']
        video = request.POST['video']

        videos = Video(title= title,video=video)
        videos.save()
        return redirect('videos')
    return render (request,'upload.html')