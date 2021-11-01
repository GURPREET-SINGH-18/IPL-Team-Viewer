from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import BaseUser
from .models import addteam
from .forms import addteamform
import os

# Create your views here.
def index(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            print(user)
            if user is not None:
                auth.login(request, user)
                messages.info(request, 'login successfully')
                return redirect('/main')
            else:
                messages.error(request, 'Invalid Username or Password')
                return redirect('/')
        else:
            messages.info(request, 'Please login First')
            return render(request, 'index.html')

def main(request):
    teams=addteam.objects.all()
    return render(request, 'main.html',{'team': teams})

def signup(request):
            if request.method == 'POST':
                username = request.POST['username']
                first = request.POST['first']
                lastname = request.POST['lastname']
                password = request.POST['password']
                email = request.POST['email']
                user = BaseUser.objects.create_user(username=username, first_name=first, last_name=lastname, password=password,
                                            email=email)
                user.address = request.POST['address']
                user.mobile = request.POST['mobile']
                user.date = request.POST['date']
                user.gender = request.POST['gender']
                user.save()
                messages.success(request, "signup successfully")
                return redirect("/")
            else:
                return render(request, 'signup.html')


def logout(request):
    auth.logout(request)
    messages.info(request, 'logout successfully')
    return redirect("/")


def add(request):
    if request.method == 'POST':
        form = addteamform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Team Added successfully")
            return redirect("/main")
        else:
            at = addteamform()
            messages.success(
                request, "Something Wrong happened Please try again")
            return render(request, 'addteam.html', {'info': at})
    else:
        at = addteamform()
        return render(request, 'addteam.html', {'info': at})


def teaminfo(request, myid):
    team = addteam.objects.filter(id=myid)
    tp = team[0].player
    tp = tp.split(",")
    print(type(tp))
    print(tp)
    tc = team[0].coach
    tc = tc.split(",")
    print(tc)
    return render(request, 'team.html', {'team': team[0], 'player': tp, 'coach': tc})


def update(request, myid):
    obj = get_object_or_404(addteam, id=myid)
    form = addteamform(request.POST or None ,request.FILES or None ,instance=obj)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "You successfully updated the Details")
        context = {'form': form}
        return redirect('/main')
    else:
        return render(request,'update.html' , {'info':form})
    
def delete(request,myid):
    myid=int(myid)
    t=addteam()
    t.id=myid
    t.delete()
    messages.success(request, "You successfully Deleted the Team")
    return redirect('/main')
