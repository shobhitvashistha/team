from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField

ROLE_CHOICES = (
    ('admin', 'admin'),
    ('regular', 'regular')
)


class TeamMember(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField(unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
