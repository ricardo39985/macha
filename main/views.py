from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms = [
    {"id": 1, "name": "Learn Python"},
    {"id": 2, "name": "Learn Ruby"},
    {"id": 3, "name": "Learn JS"}


]


def home(request):
    context = {"rooms":rooms}
    return render(request, 'main/home.html', context)


def room(request, pk):
    room = ""
    for r in rooms:
        if r['id']== int(pk):
            room = r
    context = {"room":room}
    return render(request, 'main/room.html', context)
