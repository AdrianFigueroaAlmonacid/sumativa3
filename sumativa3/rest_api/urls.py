from django.urls import path
from .import views
urlpatterns = [
    path('series/', views.lista_series, name='lista_series'),
    path('series/<id>', views.vista_serie, name='vista_serie'),

]
