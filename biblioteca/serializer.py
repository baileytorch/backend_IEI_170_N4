from rest_framework import serializers
from .models import Nacionalidad, Autor, Comuna, Direccion, Biblioteca, Lector, TipoCategoria, Categoria, Libro, Prestamo, TipoParametro, Parametro


class NacionalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nacionalidad
        fields = '__all__'


class AutorSerializer(serializers.ModelSerializer):
    nacionalidad = NacionalidadSerializer()

    class Meta:
        model = Autor
        fields = '__all__'


class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = '__all__'


class DireccionSerializer(serializers.ModelSerializer):
    comuna = ComunaSerializer()

    class Meta:
        model = Direccion
        fields = '__all__'


class BibliotecaSerializer(serializers.ModelSerializer):
    direccion = DireccionSerializer()

    class Meta:
        model = Biblioteca
        fields = '__all__'


class LectorSerializer(serializers.ModelSerializer):
    biblioteca = BibliotecaSerializer()
    direccion = DireccionSerializer()

    class Meta:
        model = Lector
        fields = '__all__'


class TipoCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCategoria
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    tipo_categoria = TipoCategoriaSerializer()

    class Meta:
        model = Categoria
        fields = '__all__'


class LibroSerializer(serializers.ModelSerializer):
    biblioteca = BibliotecaSerializer()
    categoria = CategoriaSerializer()

    class Meta:
        model = Libro
        fields = '__all__'


class PrestamoSerializer(serializers.ModelSerializer):
    libro = LibroSerializer()
    lector = LectorSerializer()

    class Meta:
        model = Prestamo
        fields = '__all__'


class TipoParametroSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoParametro
        fields = '__all__'


class ParametroSerializer(serializers.ModelSerializer):
    tipo_parametro = TipoParametroSerializer()

    class Meta:
        model = Parametro
        fields = '__all__'
