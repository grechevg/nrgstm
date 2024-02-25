from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return HttpResponse("Страница о нас.")
