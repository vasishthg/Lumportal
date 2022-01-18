from django.contrib import admin
from users.models import Oompa
class OompaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Oompa, OompaAdmin)
