from django.views.generic import TemplateView
from .models import MenuItem

class MenuView(TemplateView):
    template_name = 'menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu'] = MenuItem.objects.filter(name='main_menu').first()
        return context
