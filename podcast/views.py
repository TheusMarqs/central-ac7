from django.shortcuts import render

def podcast(request):
    return render(request, 'podcast.html')