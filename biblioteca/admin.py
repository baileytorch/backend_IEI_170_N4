from django.contrib import admin
from .models import Comuna, Nacionalidad, Direccion, Autor, Biblioteca, Categoria, Libro, Lector, Prestamo

# Register your models here.
admin.site.register(Comuna)
admin.site.register(Nacionalidad)
admin.site.register(Direccion)
admin.site.register(Autor)
admin.site.register(Biblioteca)
admin.site.register(Categoria)
admin.site.register(Libro)
admin.site.register(Lector)
admin.site.register(Prestamo)
