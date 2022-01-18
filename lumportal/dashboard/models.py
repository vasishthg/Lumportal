from django.db import models
from users.models import Oompa
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from dateutil.relativedelta import relativedelta

import datetime
# Create your models here.
class Pushpa(models.Model):
    coins = models.IntegerField(default=0)

class Room(models.Model):
    name = models.CharField(max_length=200)
    eff = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    owned = models.BooleanField(default=False)

class Notif(models.Model):
    notification = models.CharField(max_length=260)

class Training(models.Model):
    oompa = models.ForeignKey(Oompa, on_delete=models.CASCADE)

    time = models.DateTimeField()
    @property
    def real_price(self):
        if (self.time + datetime.timedelta(seconds=60)).replace(tzinfo=None) < datetime.datetime.now().replace(tzinfo=None):
            channel_layer = get_channel_layer()

            async_to_sync(channel_layer.group_send)(
                'h',
                {
                    'type': 'chat_message',
                    'message': f'{self.oompa.name} levelled up to {self.oompa.level + 1}'
                }
            )
            newnotif = Notif(notification=f'{self.oompa.name} levelled up to {self.oompa.level + 1}')
            newnotif.save()
            self.oompa.level += 1
            self.oompa.save()
            return self.oompa.level + 1, self.delete()
        return self.oompa.level


class Productionperhr(models.Model):
    production = models.IntegerField(default=0)

class Chocolates(models.Model):
    chocolates = models.IntegerField(default=0)
    time = models.DateTimeField()
    @property
    def real_price(self):
        if (self.time + datetime.timedelta(seconds=300)).replace(tzinfo=None) < datetime.datetime.now().replace(tzinfo=None):
            oompas = Oompa.objects.all()
            products = 0
            for oomp in oompas:
                produced = oomp.level*10+oomp.salary*2
                products += produced
            self.chocolates += products
            xx = Productionperhr(production=products)
            xx.save()
            self.time = datetime.datetime.now()
            self.save()
            return
        return
