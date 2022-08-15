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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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


class Movimientos(models.Model):
    id_movimientos = models.AutoField(primary_key=True, blank=True, null=True)
    identificación_mov = models.IntegerField(blank=True, null=True)
    numero_cuenta = models.IntegerField(blank=True, null=True)
    tp_operacion = models.CharField(blank=True, null=True)
    hora_trans = models.IntegerField(blank=True, null=True)
    new_balance = models.IntegerField(db_column='New_balance', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'movimientos'


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
