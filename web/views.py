from django.shortcuts import render
from .models import registration


# Create your views here.
def home(request):
    return render(request, 'home.html')


def add(request):
    name = request.POST['name']
    email = request.POST['email']
    contact = request.POST['contact']
    res = registration(name=name, email=email, contact=contact).save()
    msg="Done"
    return render(request, 'home.html',{"msg":msg})
