from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User, Group
from django.views.generic import View
# Create your views here.

def index(req):

    return render(req, 'index.html')


def rybalka(req):
    ryb = Rybalka.objects.all()
    data = {'rybalovnye': ryb}
    return render(req, 'rybalka.html',data)

def odejda(req):
    shmot = Odejda.objects.all()
    data = {'odejda': shmot}
    return render(req, 'odejda.html',data)

def ohota(req):
    oh = Ohota.objects.all()
    data = {'ohota': oh}
    return render(req, 'ohota.html', data)

def about(req):
    return render(req, 'about.html')

def buy(req,id):
    item = Rybalka.objects.get(id=id)
    if Korzina.objects.filter(rybalka_id=id):
        getRybalka = Korzina.objects.get(rybalka_id=id)
        getRybalka.count+=1
        getRybalka.summa = getRybalka.calcSumma()
        getRybalka.save()
    else:
        Korzina.objects.create(count=1, rybalka=item, summa=item.price)
    return redirect('rybalka')

def buy2(req,id):
    item = Ohota.objects.get(id=id)
    if Korzina_2.objects.filter(ohota_id=id):
        getOhota = Korzina_2.objects.get(ohota_id=id)
        getOhota.count+=1
        getOhota.summa = getOhota.calcSumma2()
        getOhota.save()
    else:
        Korzina_2.objects.create(count=1, ohota=item, summa=item.price)
    return redirect('ohota')

def buy3(req,id):
    item = Odejda.objects.get(id=id)
    if Korzina_3.objects.filter(odejda_id=id):
        getOdejda = Korzina_3.objects.get(odejda_id=id)
        getOdejda.count+=1
        getOdejda.summa = getOdejda.calcSumma3()
        getOdejda.save()
    else:
        Korzina_3.objects.create(count=1, odejda=item, summa=item.price)
    return redirect('odejda')

def korz(req):
    items = Korzina.objects.all()
    itog = 0
    for i in items:
        itog+=i.summa

    data = {'items':items,'itog':itog}
    return render(req, 'korzina.html', data)

def delete(req,id):
    item = Korzina.objects.get(id=id)
    item.delete()
    return redirect('korz')


from .form import SignUpForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
def registr(req):
    if req.POST:
        print(2)
        anketa = SignUpForm(req.POST)
        if anketa.is_valid():
            print(3)
            anketa.save()
            k1 = anketa.cleaned_data.get('username')
            k2 = anketa.cleaned_data.get('password1')
            k3 = anketa.cleaned_data.get('first_name')
            k4 = anketa.cleaned_data.get('last_name')
            k5 = anketa.cleaned_data.get('email')
            user = authenticate(username=k1, password=k2)#сохраняет нового пользователя
            man = User.objects.get(username=k1)#находим нового юзера
            man.email=k5
            man.first_name=k3
            man.last_name=k4
            man.save()
            login(req,user)    #входит на сайт
            return redirect('home')
    else:
        anketa = SignUpForm()
    data={'regform':anketa}
    return render(req,'registration/registration.html',context=data)
