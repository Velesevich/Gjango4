from django.contrib import admin
from .models import Man
from .models import Weman
admin.site.register(Man)
admin.site.register(Weman)
from .models import Task
admin.site.register(Task)
# Register your models here.
