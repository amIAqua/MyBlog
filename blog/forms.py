from django import forms
from django.forms import TextInput
from .models import Comment, City



class LeaveCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            'comment_content',
			]
        widgets = {
            'comment_content': forms.Textarea(attrs = {'class': 'form-control', 'placeholder': 'Комментарий'})
        }


class CityForm(forms.ModelForm):

	class Meta:
		model = City
		fields = [
		    'city_name',
		    ]
		widgets = {
		    'city_name': forms.TextInput(attrs = {
		    	               'class': 'form-control',
		    	               'placeholder': 'Введите город'

		    	                 })
		        }
