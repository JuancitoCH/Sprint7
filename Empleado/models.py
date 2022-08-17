from django.db import models

class Empleado(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()  # This field type is a guess.
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    employee_hire_date = models.TextField(db_column='employee_hire_date') 
    branch_id = models.IntegerField()

    def __str__(self):
        return (f"{self.employee_id} {self.employee_dni} {self.employee_surname} {self.employee_name} {self.employee_hire_date}")
    class Meta:
        managed = False
        db_table = 'empleado'
# Create your models here.
