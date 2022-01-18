from django.contrib import admin
from dashboard.models import Pushpa, Room, Training, Notif,Chocolates, Productionperhr

class PushpaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Pushpa, PushpaAdmin)

class RoomAdmin(admin.ModelAdmin):
    pass
admin.site.register(Room, RoomAdmin)

class TrainingAdmin(admin.ModelAdmin):
    pass
admin.site.register(Training, TrainingAdmin)

class NotifAdmin(admin.ModelAdmin):
    pass
admin.site.register(Notif, NotifAdmin)

class ChocoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Chocolates, ChocoAdmin)

class ProductionperhrAdmin(admin.ModelAdmin):
    pass
admin.site.register(Productionperhr, ProductionperhrAdmin)
# Register your models here.
