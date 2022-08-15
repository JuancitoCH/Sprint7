from django.db import models

# Create your models here.
class MarcasTarjeta(models.Model):
    mt_id = models.AutoField(db_column='MT_id', primary_key=True, blank=True)  # Field name made lowercase.
    mt_nombre = models.TextField(db_column='MT_nombre', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Marcas_Tarjeta'
        
class TipoTarjeta(models.Model):
    tipo_tarjeta_id = models.AutoField(db_column='Tipo_tarjeta_id', primary_key=True, blank=True)  # Field name made lowercase.
    tipo = models.TextField(db_column='Tipo', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tipo_tarjeta'
        
class Tarjeta(models.Model):
    numero = models.CharField(db_column='Numero', primary_key=True, max_length=16)  # Field name made lowercase.
    cvv = models.IntegerField(db_column='CVV')  # Field name made lowercase.
    f_otorgamiento = models.DateTimeField(db_column='F_Otorgamiento')  # Field name made lowercase.
    f_vencimiento = models.DateTimeField(db_column='F_Vencimiento')  # Field name made lowercase.
    fk_tipo = models.ForeignKey(TipoTarjeta, models.DO_NOTHING, db_column='fk_Tipo')  # Field name made lowercase.
    fk_marca = models.ForeignKey(MarcasTarjeta, models.DO_NOTHING, db_column='fk_Marca')  # Field name made lowercase.
    fk_cliente = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tarjeta'