from django.db import models
import re
from django.core.validators import EmailValidator, RegexValidator
from django.db.models import CharField
from rest_framework.exceptions import ValidationError

USER_LEVELS = (
    ('intern', 'Intern'),
    ('junior', 'Junior'),
    ('junior++', 'Junior++'),
    ('middle', 'Middle'),
    ('middle++', 'Middle++'),
    ('senior', 'Senior')
)

GENDERS = (
    ('male', 'Male'),
    ('female', 'Female')
)

def validate_password(value):
        password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,}$'

        # noinspection PyTypeChecker
        if not re.match(password_regex, value):
            raise ValidationError('Password must contain at least one uppercase letter, one lowercase letter, '
                                  'one digit and be at least 8 characters long.')

class User(models.Model):
    is_boss = models.BooleanField(default=False)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    password = models.CharField(max_length=255, validators = [validate_password,])
    gender = models.CharField(choices = GENDERS, max_length = 50)
    age = models.IntegerField()
    position = models.CharField(max_length=255)
    location = models.CharField(max_length=255)  # there should be worked with GPS-system
    birth_date = models.DateField()
    email = models.CharField(validators=[
        RegexValidator(regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
                       message="Enter a valid email address matching the format example@example.com")], max_length=255 ,blank=True)
    phone_number = models.CharField(max_length=15,
                                    validators=[
                                        RegexValidator(
                                            regex=r'^\+?1?\d{9,15}$',
                                            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
                                        )
                                    ])
    skype = models.CharField(max_length=255)
    level = models.CharField(choices=USER_LEVELS, max_length=255)
    avatar = models.ImageField(upload_to='media.avatars')

    def __str__(self):
        return '%s - %s -%s' % (self.firstname, self.lastname, self.phone_number)


class Verification(models.Model):
    code = models.CharField(max_length=4)
    is_verified = models.BooleanField(default=False)
