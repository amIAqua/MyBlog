from django import forms 
from .models import Comment



"""
class LeaveCommentForm(forms.ModelForm):

	class Meta:
	    model = Comment
	    fields = (
	        'user',  
	    	'comment_content'
	    	)
	    widgets = {
	        'user': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Ваш ник'}),
	        'comment_content': forms.Textarea(attrs = {'class': 'form-control', 'placeholder': 'Комментарий'})
	    } 

"""

class LeaveCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            'comment_content',
			]
        widgets = {
            'comment_content': forms.Textarea(attrs = {'class': 'form-control', 'placeholder': 'Комментарий'})
        }
			
