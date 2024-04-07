from django.db.models import IntegerChoices


class GenderChoices(IntegerChoices):
    MALE = 1
    FEMALE = 0
    
class LevelChoices(IntegerChoices):
    INTERN = 0
    JUNIOR = 1
    STRONG_JUNIOR = 2
    MIDDLE = 3
    STRONG_MIDDLE = 4
    SENIOR = 5