from django.contrib import admin
from .models import Cuenta, TiposCuenta, Movimientos
# Register your models here.

admin.site.register(Cuenta)
admin.site.register(TiposCuenta)
admin.site.register(Movimientos)