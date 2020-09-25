from django.contrib import admin

# Register your models here.
from .models import Character, Force, Spaceship

admin.site.register(Character)
admin.site.register(Force)
admin.site.register(Spaceship)
