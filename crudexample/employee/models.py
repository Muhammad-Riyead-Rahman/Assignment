from django.db import models  
from django.core.validators import RegexValidator

class Employee(models.Model):
    ename = models.CharField(max_length=100)
    
    # Add a RegexValidator to ensure the econtact is a Bangladeshi mobile number
    mobile_regex = RegexValidator(
        regex=r'^\+?8801[3-9]\d{8}$',
        message="Phone number must be a valid Bangladeshi mobile number in the format: '+8801XXXXXXXXX'."
    )
    econtact = models.CharField(validators=[mobile_regex], max_length=15)

    class Meta:
        db_table = "employee"
