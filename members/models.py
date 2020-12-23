from django.core.validators import RegexValidator
from django.db import models

# Create your models here.

ROLE_CHOICES = (
    ('admin', 'admin'),
    ('regular', 'regular')
)

PHONE_VALIDATOR = RegexValidator(
    regex=r'^\+?\d{8,15}$',
    message="Phone number must be entered in the format: '+999999999'. 8-15 digits allowed.")


class TeamMember(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=16, unique=True, validators=[PHONE_VALIDATOR])
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
