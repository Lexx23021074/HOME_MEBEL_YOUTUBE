from django.http import HttpResponse
from django.shortcuts import render
from django.template import context
from django.views.generic import TemplateView

from goods.models import Categories


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - _Головна'
        context['content'] = "Магазин меблів HOME"
        return context
    

class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Про нас'
        context['content'] = "Про нас"
        context['text_on_page']= " Текст про те який офігенний цей магазин, які вони красиві і який в них якісний товар"
        return context



# def index(request):
  
    
#     context : dict[str,Any] = {
#         'title' : "Home - Головна",
#         'content' : "Магазин меблів HOME",
#     }

#     return render(request, 'main/index.html', context )

# def about(request):
#     context : dict[str,Any] = {
#         'title' : "Home - Про нас",
#         'content' : "Про нас",
#         'text_on_page' : " Текст про те який офігенний цей магазин, які вони красиві і який в них якісний товар"

#     }

#     return render(request, 'main/about.html', context )

