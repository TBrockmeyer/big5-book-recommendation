from django.db import models

class Employee(models.Model):
    employee_id = models.AutoField(unique=True, primary_key=True)
    employee_firstname = models.CharField(max_length=100, blank=True, default='')
    employee_lastname = models.CharField(max_length=100, blank=True, default='')
    employee_selfperception_text = models.CharField(max_length=1000, blank=True, default='')

    def save(self, *args, **kwargs):
        super(Employee, self).save(*args, **kwargs)
