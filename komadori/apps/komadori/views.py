from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "komadori/index.html"