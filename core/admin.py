from django.contrib import admin
from .models import *


class RuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'point')

class RegraAdmin(admin.ModelAdmin):
    list_display = ('rule_name', 'rule_description', 'rule_criteria', 'rule_outcome')

class GameDataAdmin(admin.ModelAdmin):
    list_display = ('player', 'score', 'level', 'achievements')
# Register your models here.


admin.site.register(Rule)
admin.site.register(Regra)
admin.site.register(User)
admin.site.register(GameData, GameDataAdmin)
