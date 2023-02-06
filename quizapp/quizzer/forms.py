from django.forms import ModelForm
from .models import Questions

class CreateQuestionForm(ModelForm):
    class Meta:
        model=Questions
        fields='__all__'