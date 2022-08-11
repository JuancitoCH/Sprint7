# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MarcasTarjeta(models.Model):
    mt_id = models.AutoField(db_column='MT_id', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    mt_nombre = models.TextField(db_column='MT_nombre', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Marcas_Tarjeta'


class TipoTarjeta(models.Model):
    tipo_tarjeta_id = models.AutoField(db_column='Tipo_tarjeta_id', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    tipo = models.TextField(db_column='Tipo', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tipo_tarjeta'


class TiposCliente(models.Model):
    tcli_id = models.AutoField(db_column='TCLI_id', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    tcli_tipo = models.TextField(db_column='TCLI_tipo', unique=True)  # Field name made lowercase.
    tcli_limites_tranf = models.FloatField(db_column='TCLI_limites_tranf', blank=True, null=True)  # Field name made lowercase.
    tcli_comision_tranf = models.FloatField(db_column='TCLI_comision_tranf', blank=True, null=True)  # Field name made lowercase.
    tcli_tarjeta_limit = models.IntegerField(db_column='TCLI_Tarjeta_limit', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tipos_Cliente'


class TiposCuenta(models.Model):
    tcu_id = models.AutoField(db_column='TCU_id', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    tcu_tipo = models.TextField(db_column='TCU_tipo', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tipos_Cuenta'


class Cliente(models.Model):
    customer_id = models.AutoField()
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cliente'


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField(blank=True, null=True)
    tipo = models.ForeignKey(TiposCuenta, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuenta'


class Direcciones(models.Model):
    direccion_id = models.AutoField(primary_key=True, blank=True, null=True)
    calle = models.TextField()
    ciudad = models.TextField()
    provincia = models.TextField()
    pais = models.TextField()
    fk_client_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direcciones'


class Empleado(models.Model):
    employee_id = models.AutoField()
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'empleado'


class Prestamo(models.Model):
    loan_id = models.AutoField()
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamo'


class Sucursal(models.Model):
    branch_id = models.AutoField()
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal'


class Tarjeta(models.Model):
    numero = models.CharField(db_column='Numero', primary_key=True)  # Field name made lowercase.
    cvv = models.IntegerField(db_column='CVV')  # Field name made lowercase.
    f_otorgamiento = models.DateTimeField(db_column='F_Otorgamiento')  # Field name made lowercase.
    f_vencimiento = models.DateTimeField(db_column='F_Vencimiento')  # Field name made lowercase.
    fk_tipo = models.ForeignKey(TipoTarjeta, models.DO_NOTHING, db_column='fk_Tipo')  # Field name made lowercase.
    fk_marca = models.ForeignKey(MarcasTarjeta, models.DO_NOTHING, db_column='fk_Marca')  # Field name made lowercase.
    fk_cliente = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tarjeta'
