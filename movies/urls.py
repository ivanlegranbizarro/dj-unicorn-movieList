from django.urls import path, include
from . import views

urlpatterns = [
    path('unicorn/', include('django_unicorn.urls')),
    path("", views.MovieListView.as_view(), name="movie_list"),
]
