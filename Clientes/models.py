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

