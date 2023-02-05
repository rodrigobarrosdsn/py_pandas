from django.contrib import admin
from .models import *


class RuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'point')
# Register your models here.


admin.site.register(Rule)
