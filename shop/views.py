from django.shortcuts import render

def index(request):
    context = {'a':'a'}
    return render(request, 'index.html', context)