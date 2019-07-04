from django.views.generic import View, TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'