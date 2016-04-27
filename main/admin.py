from django.contrib import admin
from main.models import CustomUser, Game, Game_result

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Game)
admin.site.register(Game_result)