from django.db import models

# Create your models here.
# class Clientes(models.Model):
#     customer_id=models.AutoField(primary_key=True)
#     customer_name = models.CharField(null=False,max_length=100)
#     customer_surname = models.CharField(null=False,max_length=100)
#     customer_DNI = models.CharField(max_length=10,null=False,unique=True)
#     dob = models.TextField(null=True)
#     # branch_id=models.ForeignKey(Branchs,null=False,on_delete=models.CASCADE)
#     class Meta():
#         ordering=['-customer_id']
#         verbose_name = 'client'
    
#     def __str__(self):
#         return (f"{self.customer_id} {self.customer_DNI} {self.customer_surname} {self.customer_name}")

class Cliente(models.Model):
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

