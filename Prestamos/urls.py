from django.urls import path
from . import views

urlpatterns = [
  path('', views.render_prestamos, name='prestamos_page'),
  path('solicitud/', views.formulario_prestamos_preaprobados, name='form_preap_prestamos'),
  path('solicitud/send/', views.formulario_prestamos_preaprobados_POST, name='form_preap_prestamos_POST'),
]