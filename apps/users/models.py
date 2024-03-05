from django.db import models
import re
from django.core.validators import EmailValidator, RegexValidator
from django.db.models import CharField
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from .choices import GenderChoices
from .managers import CustomUserManager


USER_LEVELS = (
    ('intern', 'Intern'),
    ('junior', 'Junior'),
    ('junior++', 'Junior++'),
    ('middle', 'Middle'),
    ('middle++', 'Middle++'),
    ('senior', 'Senior')
)

class CustomUser(AbstractUser):
    gender = models.SmallIntegerField(choices=GenderChoices.choices)   
    age = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255, null=True)  # there should be worked with GPS-system
    birth_date = models.DateField(null=True)
    phone_number = models.CharField(max_length=15,
                                    validators=[
                                        RegexValidator(
                                            regex=r'^\+?1?\d{9,15}$',
                                            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
                                        )
                                    ], null=True)
    skype = models.CharField(max_length=255, null=True)
    level = models.CharField(choices=USER_LEVELS, max_length=255, null=True)
    avatar = models.ImageField(upload_to='media.avatars', null=True)
    objects = CustomUserManager()


class Verification(models.Model):
    code = models.CharField(max_length=4)
    is_verified = models.BooleanField(default=False)











