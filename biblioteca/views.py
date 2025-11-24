from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
import django_filters
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializer import NacionalidadSerializer, AutorSerializer, ComunaSerializer, DireccionSerializer, BibliotecaSerializer, LectorSerializer, TipoCategoriaSerializer, CategoriaSerializer, LibroSerializer, PrestamoSerializer, ReservaSerializer, TipoParametroSerializer, ParametroSerializer
from .models import Nacionalidad, Autor, Comuna, Direccion, Biblioteca, Lector, TipoCategoria, Categoria, Libro, Prestamo, Reserva, TipoParametro, Parametro
# Create your views here.


def logout_view(request):
    # Cierra la sesión del usuario y limpia la data de SESSION
    logout(request)
    # Redirige a la página de inicio de sesión
    return redirect('login')


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro Exitoso. ¡Bienvenido!")
            return redirect('/')
        else:
            messages.error(
                request, "No ha sido posible Registrarlo. Por favor revise el formulario por errores.")
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})


@login_required
def pagina_inicio(request):
    user = User()
    permisos = user.get_all_permissions()
    return render(request, 'biblioteca/inicio.html',{'permisos':permisos})


class NacionalidadViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Nacionalidad.objects.all()
    serializer_class = NacionalidadSerializer


def listado_autores(request):
    autores = Autor.objects.all()
    return render(request, 'biblioteca/lista_autores.html', {'autores': autores})


class AutorViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


def listado_comunas(request):
    comunas = Comuna.objects.all()
    return render(request, 'biblioteca/lista_comunas.html', {'comunas': comunas})


class ComunaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer


class DireccionViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer


class BibliotecaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializer


def listado_lectores(request):
    return render(request, 'biblioteca/lista_lectores.html')


class LectorViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Lector.objects.all()
    serializer_class = LectorSerializer


class TipoCategoriaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = TipoCategoria.objects.all()
    serializer_class = TipoCategoriaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class LibroFilter(django_filters.FilterSet):
    id_categoria = django_filters.ModelChoiceFilter(
        queryset=Categoria.objects.all(), label='Categoría')
    id_autor = django_filters.ModelChoiceFilter(
        queryset=Autor.objects.all(), label='Autor')

    class Meta:
        model = Libro
        fields = ['id_categoria', 'id_autor']


def listado_libros(request):
    f = LibroFilter(request.GET, queryset=Libro.objects.all())
    return render(request, 'biblioteca/lista_libros.html', {'filter': f})


class LibroViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer


class PrestamoViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer


class ReservaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer


class TipoParametroViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = TipoParametro.objects.all()
    serializer_class = TipoParametroSerializer


class ParametroViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Parametro.objects.all()
    serializer_class = ParametroSerializer
