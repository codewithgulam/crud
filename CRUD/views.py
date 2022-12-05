from django.shortcuts import render
from .forms import User_Registration
from django.http import HttpResponseRedirect
from.models import User
# Create your views here.

def addShow(request): #It add new data and show them
    if request.method== 'POST':
         fm = User_Registration(request.POST)
         if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            new_user = User(name=nm, email= em, password = pw)
            new_user.save()
            fm=User_Registration()
    else:
         fm = User_Registration()
    user_obj = User.objects.all()
    params = {
            'formdata':user_obj,
            'form':fm ,
         }
    return render(request, 'CRUD/showandadd.html', params)


def deleteUser(request, id):
    if request.method =='POST':
        dl = User.objects.get(id=id)
        dl.delete()
    return HttpResponseRedirect('/')


def updateUser(request, id):

    if request.method =="POST":
        user= User.objects.get(id=id)
        fm = User_Registration(request.POST, instance=user)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
 
    else:
        user = User.objects.get(id=id)
        fm = User_Registration(instance=user)
    return render(request, 'CRUD/update.html', {'form':fm})