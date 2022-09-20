from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields = ['text']
		#the label is for the field, for example, if we wanted to take a users name, 
		#we could put 'Name' in the empty string below.
		labels = {'text': ''}

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text': ''}
		#A widget is an HTML form element, such as a single line text box, multi
		#line text box or drop-down list. The forms.Textarea element customizes
		#the area that the user has to type, making it larger and better suited 
		#for a larger user entry.
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}