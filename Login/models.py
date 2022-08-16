from django.db import models
from Clientes.models import Cliente
from django.contrib.auth.models import User
# Create your models here.

class client_auth_relation(models.Model):
    client_auth_relation_id = models.AutoField(primary_key=True)
    client = models.OneToOneField(
        Cliente,
        on_delete=models.CASCADE,
        unique=True,
    )
    auth = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        unique=True,
    )