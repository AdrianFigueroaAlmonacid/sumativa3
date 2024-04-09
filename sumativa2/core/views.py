from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'core/index.html')


def estreno(request):
    return render(request, 'core/estreno.html')


def estreno1(request):
    return render(request, '/core/estreno1.html')


def estreno2(request):
    return render(request, 'core/estreno2.html')


def estreno3(request):
    return render(request, 'core/estreno3.html')


def noticia1(request):
    return render(request, 'core/noticia1.html')


def noticia2(request):
    return render(request, 'core/noticia2.html')


def noticia3(request):
    return render(request, 'core/noticia3.html')


def entrevistas(request):
    return render(request, 'core/entrevistas.html')


def entrevista1(request):
    return render(request, 'core/entrevista1.html')


def entrevista2(request):
    return render(request, 'core/entrevista2.html')


def entrevista3(request):
    return render(request, 'core/entrevista3.html')


def series(request):
    return render(request, 'core/series.html')


def streaming(request):
    return render(request, 'core/streaming.html')


def registro(request):
    return render(request, 'core/registro-usuario.html')
