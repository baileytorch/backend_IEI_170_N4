from django.urls import path, include
from rest_framework import routers
from biblioteca import views

router = routers.DefaultRouter()
# router.register(r'nacionalidades', views.NacionalidadViewSet,basename='nacionalidades')    
router.register(r'autores', views.AutorViewSet, basename='autores')
router.register(r'comunas', views.ComunaViewSet, basename='comunas')
router.register(r'direcciones', views.DireccionViewSet, basename='direcciones')
router.register(r'bibliotecas', views.BibliotecaViewSet,basename='bibliotecas')
router.register(r'lectores', views.LectorViewSet, basename='lectores')
router.register(r'tipos-categorias', views.TipoCategoriaViewSet,basename='tipos-categorias')
router.register(r'categorias', views.CategoriaViewSet, basename='categorias')
router.register(r'libros', views.LibroViewSet, basename='libros')
router.register(r'prestamos', views.PrestamoViewSet, basename='prestamos')
router.register(r'reservas',views.ReservaViewSet,basename='reservas')
router.register(r'tipos-parametros', views.TipoParametroViewSet,basename='tipos-parametros')
router.register(r'parametros', views.ParametroViewSet, basename='parametros')

urlpatterns = [
    path('', include(router.urls))
]
