from django.contrib import admin

# Register your models here.
from .models import coffee,sell

admin.site.register(coffee)
admin.site.register(sell)