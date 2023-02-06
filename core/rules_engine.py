from .models import *
def evaluate_rules(user, rule):

    import ipdb
    ipdb.set_trace()


    if rule.rule_criteria:
        field_value = getattr(user, rule.rule_field)
        # Check if the criteria is satisfied
        if field_value is not None:
            # If the criteria is satisfied, update the User model
            game_data_obj = GameData.objects.get(player=user)
            import ipdb
            ipdb.set_trace()
            game_data_obj.score = game_data_obj.score + float(rule.rule_outcome)
            game_data_obj.save()
