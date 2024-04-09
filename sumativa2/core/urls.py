from django.urls import path
from .views import index, estreno, estreno1, estreno2, estreno3, noticia1, noticia2, noticia3, entrevistas, entrevista1, entrevista2, entrevista3, streaming, series, registro

urlpatterns = [
    path('', index, name="index"),
    path('registro/', registro, name="registro"),
    path('estreno/', estreno, name="estreno"),
    path('estreno1/', estreno1, name="estreno1"),
    path('estreno2/', estreno2, name="estreno2"),
    path('estreno3/', estreno3, name="estreno3"),
    path('noticia1/', noticia1, name="noticia1"),
    path('noticia2/', noticia2, name="noticia2"),
    path('noticia3/', noticia3, name="noticia3"),
    path('entrevistas/', entrevistas, name="entrevistas"),
    path('entrevista1/', entrevista1, name="entrevista1"),
    path('entrevista2/', entrevista2, name="entrevista2"),
    path('entrevista3/', entrevista3, name="entrevista3"),
    path('streaming/', streaming, name="streaming"),
    path('series/', series, name="series"),
]
