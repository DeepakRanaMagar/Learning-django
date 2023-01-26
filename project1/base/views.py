from django.shortcuts import render
# Create your views here.

rooms = [
    {'id':1, 'name':'Hello world'},
    {'id':2, 'name':'Hello c'},
    {'id':3, 'name':'Hello 1'},
]

def home(request):
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)

def room(request):
    return render(request, 'room.html')