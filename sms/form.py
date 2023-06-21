from .models import Sutdent_info, Semester1_marks
from django.forms import ModelForm


class Sutdent_info_from(ModelForm):
    class Meta:
        model = Sutdent_info
        fields = "__all__"


class Semester1_marks_form(ModelForm):
    class Meta:
        model = Semester1_marks
        fields = ('math', 'english', 'dbms',)

