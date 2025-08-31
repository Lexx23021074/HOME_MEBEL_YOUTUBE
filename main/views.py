from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):

    categories = Categories.objects.all()

    context : dict[str,Any] = {
        'title' : "Home - Головна",
        'content' : "Магазин меблів HOME",
        'categories' : categories

    }

    return render(request, 'main/index.html', context )

def about(request):
    context : dict[str,Any] = {
        'title' : "Home - Про нас",
        'content' : "Про нас",
        'text_on_page' : " Текст про те який офігенний цей магазин, які вони красиві і який в них якісний товар"

    }

    return render(request, 'main/about.html', context )

