from django.contrib import admin

# Register your models here.
from .models import coffee,sell
class CoffeeAdmin(admin.ModelAdmin):
    list_display=('name','amount')
admin.site.register(coffee,CoffeeAdmin)
admin.site.register(sell)