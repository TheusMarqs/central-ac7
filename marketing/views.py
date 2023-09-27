from django.shortcuts import render

def publicidade(request):
    group = request.user.groups.values_list('name', flat=True).first()
    return render(request, 'publicidade.html', {'group': group})