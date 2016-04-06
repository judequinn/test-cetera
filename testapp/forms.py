from django import forms
from .models import Response, Type

class AddResponseForm(forms.ModelForm):

    full_name = forms.CharField(             label = 'ФИО:', 
                                             error_messages={'required': 'Представьтесь, пожалуйста'}, )

    text = forms.CharField(                  label = 'Отзыв:', 
                                             widget=forms.Textarea(), 
                                             error_messages={'required': 'Напишите отзыв'}, )

    email = forms.EmailField(                label = 'Электронная почта:', 
                                             error_messages={'required': 'Введите адрес электронной почты'}, )

    of_type = forms.ModelMultipleChoiceField(label='Выберите категории:', 
                                             widget=forms.SelectMultiple(), 
                                             queryset = Type.objects.all(), 
                                             error_messages={'required': 'Выберите тэги'}, )

    class Meta:
        model = Response
        fields = ('full_name', 'text', 'email', 'of_type')