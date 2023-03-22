from django.db import models

# Create your models here.
class Employee_Attendance(models.Model):
    emp_id = models.IntegerField()
    name = models.CharField(max_length=50)
    date = models.DateField()
    check_in = models.TimeField()
    check_out = models.TimeField()

    def __str__(self):
        return self.name

