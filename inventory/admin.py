from django.contrib import admin
from .models import Location, Consumable, Inventory, DateTable, User


# Register your models here.
admin.site.register(Location)
admin.site.register(Consumable)
admin.site.register(Inventory)
admin.site.register(DateTable)
admin.site.register(User)