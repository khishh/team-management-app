from django.db import models

from .validators import phone_number_validator, email_validator

# Create your models here.
class TeamMember(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, validators=[email_validator])
    phone_number = models.CharField(max_length=12, validators=[phone_number_validator])
    is_admin = models.BooleanField(default=False)

    def __str__(self) -> str:
        return  self.first_name + self.last_name


