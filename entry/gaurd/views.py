from django.shortcuts import render, redirect
from . models import gaurds
from . models import guest_entries
import datetime

# Create your views here.
def gaurd(request):
    if request.session.get('guser'):
        return redirect('ghome')
    else:
        return render(request,'gaurd.html')

def glogin(request):
    guser = request.POST['guser']
    gpass = request.POST['gpass']
    
    res = gaurds.objects.filter(guser=guser, gpass=gpass)
    
    if len(res)==1:
        request.session['guser'] = res[0].guser
        return redirect('ghome')
    else:
        return render(request,'gaurd.html',{'error':'Username or Password is Incorrect!!!'})

def ghome(request):
    if request.session.get('guser'):
        return render(request,'ghome.html')
    else:
        return redirect('/gaurd/')

def glogout(request):
    del request.session['guser']
    return redirect('/gaurd/')

def enter(request):
    if request.session.get('guser'):
        return render(request,'enter.html')
    else:
        return redirect('/gaurd/')
    
def insert_entry(request):
    guest_name = request.POST['guest_name']
    purpose = request.POST['purpose']
    guest_num = request.POST['guest_num']
    address = request.POST['address']
    
    intime = datetime.datetime.now().replace(microsecond=0)
    
    q = guest_entries(guest_name=guest_name, purpose=purpose, guest_num=guest_num, address=address, intime=intime)
    
    q.save()
    
    return render(request,'enter.html',{'msg':'Entry inserted successfully!!!'})

def chk_entries(request):
    if request.session.get('guser'):
        res = guest_entries.objects.all()
        return render(request,'chk_entries.html',{'res':res})
    else:
        return redirect('/gaurd/')
    
def exit(request):
    if request.session.get('guser'):
        res = guest_entries.objects.all()
        return render(request,'exit.html',{'res':res})
    else:
        return redirect('/gaurd/')
    
def update_exit(request):
    id = request.GET['id']
    exittime = datetime.datetime.now().replace(microsecond=0)
    
    res = guest_entries.objects.get(id=id)
    res.exittime = exittime
    res.save()
    
    res = guest_entries.objects.all()
    
    return render(request,'exit.html',{'res':res,'msg':'Exit updated successfully!!!'})
    
    
    
    