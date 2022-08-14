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

