from atexit import register
from django.contrib import admin
from base.models import MyUsers

# Register your models here.
admin.site.register(MyUsers)
