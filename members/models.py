from django.db import models

# Create your models here.

ROLE_CHOICES = (
    ('admin', 'admin'),
    ('regular', 'regular')
)


class TeamMember(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
