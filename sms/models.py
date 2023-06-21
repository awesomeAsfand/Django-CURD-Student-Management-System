from django.db import models
from django.core.validators import MinValueValidator

CHOICE = [
    ('MBA', "MBA"), ("CS", "CS"), ("BS", "BS")
]
SEMESTER_CHOICE = [
    ('Semester-1', 'Semester-1'), ('Semester-1', 'Semester-1'), ('Semester-1', 'Semester-1')
]


class Sutdent_info(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    education = models.CharField(max_length=50, choices=CHOICE)
    Image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Semester1_marks(models.Model):
    student = models.ForeignKey(Sutdent_info, on_delete=models.CASCADE, related_name='marks')
    math = models.IntegerField(default=0)
    english = models.IntegerField(default=0)
    dbms = models.IntegerField(default=0)

    def __str__(self):
        return self.student
