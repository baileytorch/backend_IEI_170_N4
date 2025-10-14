"""
URL configuration for drf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from biblioteca import views
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.auth import views as auth_views

schema_view = get_schema_view(
    openapi.Info(
        title="Documentación API Gestión de Biblioteca",
        default_version='v1',
        description="Aplicación de Gestión de Biblioteca",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="mi_correo@test.test"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina_inicio, name='pagina_inicio'),
    path('biblioteca/', include('biblioteca.urls')),

    # URL's para documentación de API
    path('apidocs/', schema_view.with_ui('swagger',
                                         cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc',
                                        cache_timeout=0), name='schema-redoc'),

    # URL's de autenticación
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(),
         name='logout'),
    path('registro/', views.registro, name='registro'),
]
