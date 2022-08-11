from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('dolar',views.dolar,name='dolar'),
    # path('message/',views.message,name='message'),
]