from django.shortcuts import render

def index(request):
    return render(request, 'posts/index.html')


def room(request, room_name):
    return render(request, 'posts/rooms.html', {
        'room_name': room_name
    })