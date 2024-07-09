from django.shortcuts import render
from django.http import HttpResponse

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

def omlet(request):
    servings = int(request.GET.get("servings", 1))
    result = '# Ответ'
    for i, e in DATA['omlet'].items():
        result += f'\n {i} + {e * servings}'
    return HttpResponse(result)

def pasta(request):
    servings = int(request.GET.get("servings", 1))
    result = '# Ответ'
    for i, e in DATA['pasta'].items():
        result += f'\n {i} + {e * servings}'
    return HttpResponse(result)

def buter(request):
    servings = int(request.GET.get("servings", 1))
    result = '# Ответ'
    for i, e in DATA['buter'].items():
        result += f'\n {i} + {e * servings}'
    return HttpResponse(result)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
