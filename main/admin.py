from django.contrib import admin
from main.models import CustomUser, Game

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Game)
