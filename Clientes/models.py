from django.db import models

# Create your models here.
class Clientes(models.Model):
    customer_id=models.AutoField(primary_key=True)
    customer_name = models.CharField(null=False,max_length=100)
    customer_surname = models.CharField(null=False,max_length=100)
    customer_DNI = models.CharField(max_length=10,null=False,unique=True)
    dob = models.TextField(null=True)
    # branch_id=models.ForeignKey(Branchs,null=False,on_delete=models.CASCADE)
    class Meta():
        ordering=['-customer_id']
        verbose_name = 'client'
    
    def __str__(self):
        return (f"{self.customer_id} {self.customer_DNI} {self.customer_surname} {self.customer_name}")

