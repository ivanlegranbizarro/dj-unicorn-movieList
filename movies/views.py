from django.views.generic import TemplateView


class MovieListView(TemplateView):
    template_name = "index.html"
