import math
def cakes(recipe, available):
    return min([(math.floor(available[attribute] / value)) if attribute in available else 0 for attribute, value in recipe.items()])
#FIRST VERSION
'''import math
def cakes(recipe, available):
    min_ingredient_recipe = math.inf;
    for attribute, value in recipe.items():
        if attribute in available:
            current = (math.floor(available[attribute] / value))
            if current < min_ingredient_recipe:
               min_ingredient_recipe = current
        else:
            return 0
    return min_ingredient_recipe'''