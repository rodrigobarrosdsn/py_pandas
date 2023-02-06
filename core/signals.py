from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from .rules_engine import evaluate_rules

@receiver(post_save, sender=User)
def run_rules_engine(sender, instance, **kwargs):
    game_data = instance
    rules = Rule.objects.all()
    for rule in rules:
      import ipdb
      ipdb.set_trace()
      evaluate_rules(game_data, rule)

@receiver(post_save, sender=User)
def user_changed_handler(sender, instance, **kwargs):
    user = instance
    if user.facebook != None:
        game_data = GameData.objects.get(user=user)
        rules = Rule.objects.all()
        for rule in rules:
            evaluate_rules(game_data, rule)