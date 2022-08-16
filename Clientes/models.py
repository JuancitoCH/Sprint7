from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()

    def __str__(self):
        return (f"{self.customer_id} {self.customer_dni} {self.customer_surname} {self.customer_name}")
    class Meta:
        managed = False
        db_table = 'cliente'

class TiposCliente(models.Model):
    tcli_id = models.AutoField(db_column='TCLI_id', primary_key=True, blank=True)  # Field name made lowercase.
    tcli_tipo = models.TextField(db_column='TCLI_tipo', unique=True)  # Field name made lowercase.
    tcli_limites_tranf = models.FloatField(db_column='TCLI_limites_tranf', blank=True, null=True)  # Field name made lowercase.
    tcli_comision_tranf = models.FloatField(db_column='TCLI_comision_tranf', blank=True, null=True)  # Field name made lowercase.
    tcli_tarjeta_limit = models.IntegerField(db_column='TCLI_Tarjeta_limit', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tipos_Cliente'

class RelationClienteTipo(models.Model):
    id_relation_cliente_tipo = models.AutoField(db_column='id_Relation_Cliente_Tipo', primary_key=True, blank=True)  # Field name made lowercase.
    fk_tipos_cliente = models.OneToOneField(TiposCliente,db_column='fk_Tipos_cliente',on_delete=models.CASCADE,unique=True)  # Field name made lowercase.
    fk_cliente = models.OneToOneField(Cliente,db_column='fk_cliente',on_delete=models.CASCADE,unique=True)

    class Meta:
        managed = False
        db_table = 'Relation_Cliente_Tipo'

