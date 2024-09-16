from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from designation.models import Designation

def employee_id_length(value):
    if len(value) != 5:
        raise ValidationError("Employee ID must be exactly 5 characters long.")

class Employee(models.Model):
    employee_id = models.CharField(
        max_length=5, 
        unique=True, 
        validators=[
            employee_id_length, 
            RegexValidator(r'^\d{5}$', "Employee ID should contain only digits.")
        ]
    )
    name = models.CharField(max_length=30)
    address = models.TextField()
    phone_number = models.CharField(
        max_length=12, 
        validators=[
            RegexValidator(r'^\d+$', "Phone numbers should contain only digits.")
        ]
    )
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE) #এটির ডাটা Backend এ (admin panel) এন্ট্রি দিতে হবে। 
    short_description = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
