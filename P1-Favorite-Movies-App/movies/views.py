from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "movies/index.html", {"movie": "gladiator"})


def about(request):
    return render(request, "movies/about.html", {})
