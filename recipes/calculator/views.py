from django.shortcuts import render
from django.http import Http404


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def recipe_view(request, dish):
    recipe = DATA.get(dish)
    if recipe is None:
        raise Http404("Рецепт не найден")

    servings = int(request.GET.get('servings', 1))
    adjusted_recipe = {ingredient: amount * servings for ingredient, amount in recipe.items()}
    context = {'recipe': adjusted_recipe, 'dish_name': dish, 'servings': servings}
    return render(request, 'calculator/index.html', context)
