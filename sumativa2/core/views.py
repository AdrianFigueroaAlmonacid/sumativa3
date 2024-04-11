
from django.shortcuts import render, get_object_or_404, redirect
from .models import usuario
from django.http import HttpResponse, JsonResponse

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
        # Obtener los datos del formulario desde la solicitud POST
        nombre = request.POST.get('inputName')
        apellido = request.POST.get('inputLastName')
        nombreUsuario = request.POST.get('inputUser')
        email = request.POST.get('inputEmail')
        password = request.POST.get('inputPassword')

        # Aquí puedes validar los datos si es necesario

        # Crear una instancia de tu modelo y guardar los datos en la base de datos
        nuevo_registro = usuario(nombre=nombre, apellido=apellido, nombreUsuario=nombreUsuario,
                                 email=email, password=password)
        nuevo_registro.save()

        # Puedes enviar una respuesta de éxito si es necesario
        return redirect('listado')
    else:
        # Manejar otros casos como GET u otros métodos HTTP
        return HttpResponse('Método no permitido', status=405)


# def editar_usuario(request, usuario_id):
#     usuario = get_object_or_404(usuario, pk=usuario_id)

#     if request.method == 'POST':
#         # Procesar los datos del formulario de edición
#         usuario.nombre = request.POST.get('nombre')
#         usuario.apellido = request.POST.get('apellido')
#         usuario.nombreUsuario = request.POST.get('nombreUsuario')
#         usuario.email = request.POST.get('email')
#         usuario.password = request.POST.get('password')
#         usuario.save()
#         # Redirigir a la vista principal de modificación de usuarios
#         return redirect('modificacion')

#     return render(request, 'modificacion_usuario.html', {'usuario': usuario})


def eliminar_usuario(request, usuario_id):
    obj_usuario = get_object_or_404(usuario, pk=usuario_id)

    if request.method == 'POST':
        # Eliminar el usuario de la base de datos
        obj_usuario.delete()
        # Redirigir a la vista principal de modificación de usuarios
        return redirect('listado')

    return render(request, 'eliminar_usuario.html', {'usuario': obj_usuario})
