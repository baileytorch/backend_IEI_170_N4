from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from rest_framework import viewsets
from .serializer import Nacionalidad_Serializer as nacser, Autor_Serializer as autser, Comuna_Serializer as comser, Direccion_Serializer as dirser, Biblioteca_Serializer as bibser, Lector_Serializer as lecser, TipoCategoria_Serializer as tipser, Categoria_Serializer as catser, Libro_Serializer as libser, Prestamo_Serializer as preser
from .models import Nacionalidad, Autor, Comuna, Direccion, Biblioteca, Lector, TipoCategoria, Categoria, Libro, Prestamo

# Create your views here.


def pagina_inicio(request):
    return render(request, 'biblioteca/inicio.html')


class Nacionalidad_ViewSet(viewsets.ModelViewSet):
    queryset = Nacionalidad.objects.all()
    serializer_class = nacser


class NacionalidadListView(ListView):
    model = Nacionalidad
    template_name = 'biblioteca/nacionalidad_list.html'


class Autor_ViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = autser


class Comuna_ViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = comser


class Direccion_ViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = dirser


class Biblioteca_ViewSet(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    serializer_class = bibser


class Lector_ViewSet(viewsets.ModelViewSet):
    queryset = Lector.objects.all()
    serializer_class = lecser


class TipoCategoria_ViewSet(viewsets.ModelViewSet):
    queryset = TipoCategoria.objects.all()
    serializer_class = tipser


class Categoria_ViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = catser


class Libro_ViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = libser


class Prestamo_ViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = preser
