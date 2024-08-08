from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import director_login
from gaurd.models import gaurds
from gaurd.models import guest_entries

# Create your views here.
def director(request):
    if request.session.get('duser'):
        return redirect('home')
    else:
        return render(request, 'director.html')

def dlogin(request):
    duser = request.POST['duser']
    dpass = request.POST['dpass']
    
    res = director_login.objects.filter(duser=duser, dpass=dpass)
    
    if len(res)==1:
        request.session['duser'] = res[0].duser
        return redirect('home')
    else:
        return render(request,'director.html',{'error':'Username or Password is Incorrect!!!'})

def home(request):
    if request.session.get('duser'):
        return render(request,'home.html')
    else:
        return redirect('/director/')

def logout(request):
    del request.session['duser']
    return redirect('/director/')

def account(request):
    if request.session.get('duser'):
        return render(request,'account.html')
    else:
        return redirect('/director/')

def create_account(request):
    guser = request.POST['guser']
    gname = request.POST['gname']
    gpass = request.POST['gpass']
    
    res = gaurds.objects.filter(guser=guser)
    
    if len(res)>0:
        return render(request,'account.html',{'msg':'Gaurd is already exists with this username!!!'})
    else:
        q = gaurds(guser=guser, gname=gname, gpass=gpass)
        q.save()
        return render(request,'account.html',{'msg':'Account created successfully!!!'})
    
def check(request):
    if request.session.get('duser'):
        res = guest_entries.objects.all()
        return render(request,'check.html',{'res':res})
    else:
        return redirect('/director/')
    
    
    