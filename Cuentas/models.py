from django.db import models

# Create your models here.
class TiposCuenta(models.Model):
    tcu_id = models.AutoField(db_column='TCU_id', primary_key=True, blank=True)  # Field name made lowercase.
    tcu_tipo = models.TextField(db_column='TCU_tipo', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tipos_Cuenta'


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField(blank=True, null=True)
    tipo = models.ForeignKey(TiposCuenta, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuenta'

class Movimientos(models.Model):
    id_movimientos = models.AutoField(primary_key=True, blank=True)
    identificacion_mov = models.IntegerField(blank=True, null=True)
    numero_cuenta = models.IntegerField(blank=True, null=True)
    tp_operacion = models.CharField(blank=True, null=True, max_length = 200)
    hora_trans = models.IntegerField(blank=True, null=True)
    new_balance = models.IntegerField(db_column='New_balance', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'movimientos'
