from django import forms
from django.forms import Textarea, TextInput

from .models import Question

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['question','user_email']
		widgets = {
			'question':Textarea(attrs={'placeholder': 'Go ahead...Ask me anything.'}),
			'user_email':TextInput(attrs={'placeholder': 'Enter your email address.'}),
			}
		labels = {'question': '','user_email': ''}
