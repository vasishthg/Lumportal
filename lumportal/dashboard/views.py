from django.shortcuts import render, redirect
from .models import Pushpa, Room, Notif, Training, Chocolates, Productionperhr
from users.models import Oompa
import names
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import threading
# importing datetime module
import datetime
import time
import random
import string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
# Create your views here.
def chocoproduction():
    while True:
        chocolate = Chocolates.objects.all()
        if len(chocolate) == 0:
            cc = Chocolates(chocolates=0, time=datetime.datetime.now())
            cc.save()
        chocolate = Chocolates.objects.all()[0]
        chocolate.real_price
t = threading.Thread(target=chocoproduction)
t.setDaemon(True)
t.start()


def index(request):
    if request.method == "POST":
        chocos = request.POST.get('chocos')
        chocolate = Chocolates.objects.all()[0]
        chocolate.chocolates -= int(chocos)
        chocolate.save()
        coins = Pushpa.objects.filter().first()
        coins.coins += int(chocos)*100
        coins.save()
    if request.session.get('user') != "pushpagg":
        return redirect('users:login')

    coins = Pushpa.objects.filter().first()
    print(coins.coins)
    if coins.coins >= 120000:
        room4 ="yes"
        room5 ="yes"
    elif coins.coins < 120000 and coins.coins >= 100000:
        room4="yes"
        room5="no"
    else:
        room4="no"
        room5="no"
    room4th = Room.objects.get(name="Room 4")
    room5th = Room.objects.get(name="Room 5")
    print(room5th.owned)
    if room4th.owned == True:
        room4="owned"
    if room5th.owned == True:
        room5="owned"
    oompas = Oompa.objects.filter().count()
    notification = []
    notifs = Notif.objects.all()
    for nott in notifs:
        notification.append(nott.notification)
    chocos = Chocolates.objects.all()[0].chocolates
    prods = Productionperhr.objects.all()
    labels = []
    dataset = []
    for i in range(0, len(prods)):
        labels.append(i)
    for i in prods:
        dataset.append(i.production)
    trainn = Training.objects.all()
    trainingg = []
    for tra in trainn:
        if (tra.time + datetime.timedelta(seconds=60)).replace(tzinfo=None) > datetime.datetime.now().replace(tzinfo=None):
            timeleft = ((tra.time + datetime.timedelta(seconds=60)).replace(tzinfo=None) - datetime.datetime.now().replace(tzinfo=None)).seconds
            trainingg.append({"oompa": tra.oompa.name, "time": timeleft})
    print(trainingg)

    return render(request, "index.html", {"name": request.session.get('user'), "coins": coins.coins, "room4": room4, "room5": room5, "oompas":oompas, "room_name": "h", "notifs": Reverse(notification), "chocos": chocos, "prhr": Reverse(prods)[0].production, "labels": labels, "dataset": dataset, "training": trainingg})


def Reverse(lst):
    return [ele for ele in reversed(lst)]
def shop(request):
    if request.session.get('user') != "pushpagg":
        return redirect('users:login')
    coins = Pushpa.objects.filter().first()
    print(coins.coins)
    if coins.coins >= 120000:
        room4 ="yes"
        room5 ="yes"
    elif coins.coins < 120000 and coins.coins >= 100000:
        room4="yes"
        room5="no"
    else:
        room4="no"
        room5="no"
    room4th = Room.objects.get(name="Room 4")
    room5th = Room.objects.get(name="Room 5")
    print(room5th.owned)
    if room4th.owned == True:
        room4="owned"
    if room5th.owned == True:
        room5="owned"
    oompas = Oompa.objects.filter().count()
    notification = []
    notifs = Notif.objects.all()
    for nott in notifs:
        notification.append(nott.notification)

    return render(request, "shop.html", {"name": request.session.get('user'), "coins": coins.coins, "room4": room4, "room5": room5, "oompas":oompas, "room_name": "h", "notifs": Reverse(notification)})

def buy(request):
    if request.method == "POST":

        room = request.POST.get('room')
        budget = Room.objects.get(name="Room "+str(room))
        totalcost = budget.price
        pushpa = Pushpa.objects.filter().first()
        pushpa.coins =pushpa.coins - totalcost
        pushpa.save()
        budget.owned = True
        budget.save()
        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(
            'h',
            {
                'type': 'chat_message',
                'message': 'Bought Room' + str(level)
            }
        )
        return redirect('dashboard:shop')
def training(request):
    if request.session.get('user') != "pushpagg":
        return redirect('users:login')
    coins = Pushpa.objects.filter().first()
    print(coins.coins)
    if coins.coins >= 120000:
        room4 ="yes"
        room5 ="yes"
    elif coins.coins < 120000 and coins.coins >= 100000:
        room4="yes"
        room5="no"
    else:
        room4="no"
        room5="no"
    room4th = Room.objects.get(name="Room 4")
    room5th = Room.objects.get(name="Room 5")
    print(room5th.owned)
    if room4th.owned == True:
        room4="owned"
    if room5th.owned == True:
        room5="owned"
    oompas = Oompa.objects.filter().count()
    notification = []
    notifs = Notif.objects.all()
    for nott in notifs:
        notification.append(nott.notification)
    trainingoompa = Oompa.objects.all().order_by("-level")
    traininglist =[]
    for oomp in trainingoompa:
        traininglist.append({"name": oomp.name, "level": oomp.level, "salary": oomp.salary})
    trainn = Training.objects.all()
    trainingg = []
    for tra in trainn:
        if (tra.time + datetime.timedelta(seconds=60)).replace(tzinfo=None) > datetime.datetime.now().replace(tzinfo=None):
            for trainn in traininglist:
                if trainn['name'] == tra.oompa.name:
                    traininglist.remove(trainn)
    return render(request, "training.html", {"name": request.session.get('user'), "coins": coins.coins, "room4": room4, "room5": room5, "oompas":oompas, "room_name": "h", "notifs": Reverse(notification), "trainingoompa": traininglist})

def doCrawl(train):
    print("H")
    while train.real_price == train.oompa.level:

        pass
    print("done")
def trainingpost(request):
    if request.method == "POST":
        if request.POST.get("change") == "level":
            oompa = Oompa.objects.get(name=request.POST.get('oompa'), level = request.POST.get('level'), salary=request.POST.get('salary'))
            timee =datetime.datetime.now()
            totalcost = 100000
            train = Training(oompa=oompa, time=timee)
            train.save()
            pushpa = Pushpa.objects.filter().first()
            pushpa.coins =pushpa.coins - totalcost
            pushpa.save()
            newnotif = Notif(notification=f"{oompa.name} training for level " + str(oompa.level+1))
            newnotif.save()

            channel_layer = get_channel_layer()

            async_to_sync(channel_layer.group_send)(
                'h',
                {
                    'type': 'chat_message',
                    'message': f'{oompa.name} training for level ' + str(oompa.level+1)
                }
            )
            t = threading.Thread(target=doCrawl,args=[train])
            t.setDaemon(True)
            t.start()
            return redirect("dashboard:dashboard")
        else:
            oompa = Oompa.objects.get(name=request.POST.get('oompa'), level = request.POST.get('level'), salary=request.POST.get('salary'))
            oompa.salary += 1
            oompa.save()
            newnotif = Notif(notification=f'Increased {oompa.name} salary to ' + str(oompa.salary))
            newnotif.save()
            channel_layer = get_channel_layer()

            async_to_sync(channel_layer.group_send)(
                'h',
                {
                    'type': 'chat_message',
                    'message': f'Increased {oompa.name} salary to ' + str(oompa.salary)
                }
            )
            return redirect("dashboard:dashboard")


def buyoompa(request):
    if request.method == "POST":
        firstname = names.get_first_name()
        level = request.POST.get('oompa')

        oompa = Oompa(level=int(level), name=firstname+get_random_string(3), passw=firstname+"123")
        if int(level) == 5:
            totalcost = 100000
        else:
            totalcost = 120000
        oompa.save()
        pushpa = Pushpa.objects.filter().first()
        pushpa.coins =pushpa.coins - totalcost
        pushpa.save()
        newnotif = Notif(notification="Bought Oompa Loompa Lvl "+ str(level))
        newnotif.save()
        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(
            'h',
            {
                'type': 'chat_message',
                'message': 'Bought Oompa Loompa Lvl ' + str(level)
            }
        )
        return redirect('dashboard:shop')

def oompa(request):
    if request.session.get('user') == "pushpagg":
        return redirect('users:login')
    elif not request.session.get('user'):
        return redirect('users:oomplogin')
    oomp = Oompa.objects.get(name=request.session.get('user'))


    coins = Pushpa.objects.filter().first()
    print(coins.coins)
    if coins.coins >= 120000:
        room4 ="yes"
        room5 ="yes"
    elif coins.coins < 120000 and coins.coins >= 100000:
        room4="yes"
        room5="no"
    else:
        room4="no"
        room5="no"
    room4th = Room.objects.get(name="Room 4")
    room5th = Room.objects.get(name="Room 5")
    print(room5th.owned)
    if room4th.owned == True:
        room4="owned"
    if room5th.owned == True:
        room5="owned"
    oompas = Oompa.objects.filter().count()
    notification = []
    notifs = Notif.objects.all()
    for nott in notifs:
        notification.append(nott.notification)
    chocos = Chocolates.objects.all()[0].chocolates
    prods = Productionperhr.objects.all()
    labels = []
    dataset = []
    for i in range(0, len(prods)):
        labels.append(i)
    for i in prods:
        dataset.append(i.production)
    trainn = Training.objects.all()
    trainingg = []
    for tra in trainn:
        if (tra.time + datetime.timedelta(seconds=60)).replace(tzinfo=None) > datetime.datetime.now().replace(tzinfo=None):
            timeleft = ((tra.time + datetime.timedelta(seconds=60)).replace(tzinfo=None) - datetime.datetime.now().replace(tzinfo=None)).seconds
            trainingg.append({"oompa": tra.oompa.name, "time": timeleft})
    print(trainingg)

    return render(request, "index.html", {"name": request.session.get('user'), "level": oomp.level, "salary": oomp.salary, "room4": room4, "room5": room5, "oompas":oompas, "room_name": "h", "notifs": Reverse(notification), "chocos": chocos, "prhr": Reverse(prods)[0].production, "labels": labels, "dataset": dataset, "training": trainingg})
