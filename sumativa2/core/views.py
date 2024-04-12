from django.shortcuts import redirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UsuarioForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import usuario
from django.http import HttpResponse


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
