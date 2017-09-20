from django import forms
from .models import NewsletterUser

class ContactForm(forms.Form):
	full_name = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField()
	

class NewsletterUserSignUpForm(forms.ModelForm):
	class Meta:
		model = NewsletterUser
		fields = ['email']


		def clean_email(self):
			email = self.cleaned_date.get('email')
			return email

