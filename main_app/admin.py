from django.contrib import admin
from .models import Console, Accessory, Game

# Register your models here.
admin.site.register(Console)
admin.site.register(Accessory)
admin.site.register(Game)
