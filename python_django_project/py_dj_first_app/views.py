from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.
def home(request):
    #return HttpResponse("Hello World!!!!")
    print("Came in home")
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")