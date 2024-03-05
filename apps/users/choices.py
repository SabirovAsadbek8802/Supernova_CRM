from django.db.models import IntegerChoices


class GenderChoices(IntegerChoices):
    MALE = 1
    FEMALE = 0