from django.db import models

class Employee12(models.Model):
    eid= models.CharField(max_length=15)
    ecard= models.IntegerField()
    efname = models.CharField(max_length=64)
    elname = models.CharField(max_length=64)
    eagency = models.CharField(max_length=64)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)

    class Meta:
        db_table = "Employee12"
