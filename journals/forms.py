from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields = ['text']
		# Not to generate a label for the text field
		labels = {'text':''}


class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text':''}
		# Overwrite the default widget choice
		widgets = {'text': forms.Textarea(attrs={'cols':80})}
