from django.contrib import admin
from .models import Menu
from .models import Booking
from .models import NewUser

# Register your models here!.
admin.site.register(Menu)
admin.site.register(Booking)
admin.site.register(NewUser)