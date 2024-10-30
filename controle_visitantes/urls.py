from django.contrib import admin
from django.urls import path
from apps.dashboard.views import index
from apps.visitantes.views import informacoes_visitante, registrar_visitante, finalizar_visita
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path("admin/", admin.site.urls),

    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login.html"
        ),
        name="login"
    ),

    path('logout/', views.custom_logout, name='logout'),
    path('logout_page/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout_page'),


    path(
        "",
        index,
        name="index",
    ),

    path(
        "registrar-visitante/", #url da rota
        registrar_visitante, #funcao da view
        name="registrar_visitante" #nome da rota, 
    ),

    path(
        "visitantes/<int:id>/",
        informacoes_visitante,
        name="informacoes_visitante"
    ),

    path(
        "visitantes/<int:id>/finalizar-visita/",
        finalizar_visita,
        name="finalizar_visita"
    )

]

