from django.contrib import admin
from .models import *   #this manual
# Register your models here.

#import models here(manual)
admin.site.register(Emenities)
admin.site.register(Hotels)