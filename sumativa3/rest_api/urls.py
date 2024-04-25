from django.urls import path
from .import views
urlpatterns = [
    path('series/', views.lista_series, name='lista_series'),
]
