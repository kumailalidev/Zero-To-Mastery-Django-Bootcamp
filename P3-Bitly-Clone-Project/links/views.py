from django.shortcuts import render
from .models import Link


def index(request):
    links = Link.objects.all()
    context = {"links": links}

    return render(request, "links/index.html", context)
