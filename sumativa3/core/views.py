from .forms import UsuarioForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import usuario, series
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')

        # Buscar el usuario en la base de datos
        try:
            usuario_obj = usuario.objects.get(nombreUsuario=username)
        except usuario.DoesNotExist:
            messages.error(request, 'El usuario no existe.')
            return redirect('login')

        # Verificar la contraseña
        if password == usuario_obj.password:
            # La contraseña es correcta, redirigir al listado de usuarios
            return redirect('listado')
        else:
            # La contraseña es incorrecta
            messages.error(request, 'Contraseña incorrecta.')
            return redirect('login')

    else:
        # Si no es una solicitud POST, renderizar la página de login
        return render(request, 'core/index.html')


def login(request):
    return render(request, 'core/loginUsuario.html')


def index(request):
    return render(request, 'core/index.html')


def posters(request):
    return render(request, 'core/posters-peliculas.html')


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


def seriesPrincipal(request):
    return render(request, 'core/seriesPrincipal.html')


def streaming(request):
    return render(request, 'core/streaming.html')


def registro(request):
    return render(request, 'core/registro-usuario.html')


def agregarSeries(request):
    return render(request, 'core/crud-series.html')


def modificacion(request):
    return render(request, 'core/modificacion-usuario.html')


def listadoUsuarios(request):

    usuarios = usuario.objects.all()
    datos = {

        'usuarios': usuarios
    }
    return render(request, 'core/listado-usuarios.html', datos)


def procesar_formulario(request):
    if request.method == 'POST':

        nombre = request.POST.get('inputName')
        apellido = request.POST.get('inputLastName')
        nombreUsuario = request.POST.get('inputUser')
        email = request.POST.get('inputEmail')
        password = request.POST.get('inputPassword')

        nuevo_registro = usuario(nombre=nombre, apellido=apellido, nombreUsuario=nombreUsuario,
                                 email=email, password=password)
        nuevo_registro.save()

        return redirect('listado')
    else:

        return HttpResponse('Método no permitido', status=405)


def eliminar_usuario(request, usuario_id):
    obj_usuario = get_object_or_404(usuario, pk=usuario_id)

    if request.method == 'POST':
        obj_usuario.delete()
        return redirect('listado')

    return render(request, 'eliminar_usuario.html', {'usuario': obj_usuario})


def modificacion(request, usuario_id):

    usuario_obj = get_object_or_404(usuario, id=usuario_id)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario_obj)
        if form.is_valid():
            form.save()
            return redirect('listado')
    else:
        form = UsuarioForm(instance=usuario_obj)

    return render(request, 'core/modificacion-usuario.html', {'usuario': usuario_obj, 'form': form})


def addSeries(request):
    if request.method == 'POST':
        titulo = request.POST.get('inputTitle')
        origen = request.POST.get('inputOrigin')
        estreno = request.POST.get('inputYear')
        chapters = request.POST.get('inputChapter')

        nuevo_registro = series(
            titulo=titulo, origen=origen, chapters=chapters, estreno=estreno)

        nuevo_registro.save()

        nuevo_registro = series(
            titulo=titulo, origen=origen, chapters=chapters, estreno=estreno)

        return redirect('listadoSeries')
    else:
        return HttpResponse('Método no permitido', status=405)


def listadoSeries(request):

    serie = series.objects.all()
    datos = {

        'series': serie
    }
    return render(request, 'core/listado-series.html', datos)
