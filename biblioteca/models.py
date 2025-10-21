from django.db import models
import datetime
from django.forms import ValidationError
from rut_chile import rut_chile

ahora = datetime.datetime.now

# Create your models here.


def validar_rut(rut):
    valido = rut_chile.is_valid_rut(rut)
    if valido == False:
        raise ValidationError('RUT inválido.')


def validar_mayoria_edad(fecha_nacimiento):
    # fecha_nacimiento = datetime.datetime.strptime(fecha_nac, "%d/%m/%Y")
    fecha_actual = datetime.datetime.now()
    edad = fecha_actual.year - fecha_nacimiento.year
    if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1
    if edad < 18:
        raise ValidationError('El lector debe ser mayor de edad.')


class Nacionalidad(models.Model):
    pais = models.CharField(max_length=50, blank=False)
    nacionalidad = models.CharField(max_length=50, blank=False)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)


class Autor(models.Model):
    nacionalidad = models.ForeignKey(
        Nacionalidad, on_delete=models.CASCADE, blank=True)
    nombre = models.CharField(max_length=250, blank=False)
    pseudonimo = models.CharField(max_length=50, blank=True)
    biografia = models.TextField(blank=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)


class Comuna(models.Model):
    codigo_comuna = models.CharField(max_length=5, blank=False)
    nombre_comuna = models.CharField(max_length=50, blank=False)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)


class Direccion(models.Model):
    comuna = models.ForeignKey(
        Comuna, on_delete=models.CASCADE, blank=False)
    calle = models.CharField(max_length=50, blank=False, default='')
    numero = models.CharField(max_length=10, blank=False, default='')
    departamento = models.CharField(max_length=10, blank=True)
    detalles = models.TextField(blank=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)


class Biblioteca(models.Model):
    direccion = models.ForeignKey(
        Direccion, on_delete=models.CASCADE, blank=True)
    nombre_biblioteca = models.CharField(max_length=100, blank=False)
    web = models.CharField(max_length=255, blank=True)
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)


class Lector(models.Model):
    biblioteca = models.ForeignKey(
        Biblioteca, on_delete=models.CASCADE, blank=False)
    direccion = models.ForeignKey(
        Direccion, on_delete=models.CASCADE, blank=True)
    rut_lector = models.CharField(
        max_length=12, blank=False, unique=True, validators=[validar_rut])
    nombre_lector = models.CharField(max_length=255, blank=False)
    correo_lector = models.CharField(max_length=255, blank=True)
    fecha_nacimiento = models.DateField(
        blank=True, default=None, validators=[validar_mayoria_edad])
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)


class TipoCategoria(models.Model):
    tipo_categoria = models.CharField(max_length=50, blank=False)
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)


class Categoria(models.Model):
    tipo_categoria = models.ForeignKey(
        TipoCategoria, on_delete=models.CASCADE, blank=False)
    categoria = models.CharField(max_length=100, blank=False)
    descripcion = models.CharField(max_length=255, blank=True)
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)


class Libro(models.Model):
    biblioteca = models.ForeignKey(
        Biblioteca, on_delete=models.CASCADE, blank=False)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, blank=True)
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE, blank=False)
    titulo = models.CharField(max_length=255, blank=False)
    paginas = models.IntegerField(blank=False)
    copias = models.IntegerField(blank=False)
    ubicacion = models.CharField(max_length=255, blank=False)
    fisico = models.BooleanField(default=True)
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)


class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, blank=False)
    lector = models.ForeignKey(
        Lector, on_delete=models.CASCADE, blank=False)
    fecha_prestamo = models.DateTimeField(auto_now_add=True)
    fecha_devolucion = models.DateField(blank=True)
    fecha_retorno = models.DateTimeField(blank=True)


class TipoParametro(models.Model):
    tipo_parametro = models.CharField(max_length=50, blank=False)
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)


class Parametro(models.Model):
    tipo_parametro = models.ForeignKey(
        TipoParametro, on_delete=models.CASCADE, blank=False)
    clave_parametro = models.CharField(max_length=100, blank=False)
    valor_parametro = models.CharField(max_length=255, blank=True)
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)
