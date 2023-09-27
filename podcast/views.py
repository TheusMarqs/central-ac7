from django.shortcuts import render

def podcast(request):
    group = request.user.groups.values_list('name', flat=True).first()
    return render(request, 'podcast.html', {'group': group})