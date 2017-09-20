from django.shortcuts import render
from django.template import RequestContext

# Create your views here.
from .models import NewsletterUser
from .forms import NewsletterUserSignUpForm, ContactForm
def newsletter_signup(request):
	form = NewsletterUserSignUpForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		if NewsletterUser.objects.filter(email = instance.email).exists():
			print('Email already exists')

		else:
			instance.save()

	context = {
	'form':form,

	}
	template = "newsletters/sign_up.html"

	return render(request, template, context)


def newsletter_unsubscribe(request):
	form = NewsletterUserSignUpForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		if NewsletterUser.objects.filter(email = instance.email).exists():
			NewsletterUser.objects.filter(email = instance.email).delete()
		else:
			print('Sorry, email address not found')

	context = {
	'form':form,

	}
	
	template = "newsletters/unsubscribe.html"
	return render(request, template, context)


def contact(request):
	form = ContactForm(request.POST or None)
	context = {

		"form" : form,


	}
	template = "personal/contact.html"
	return render(request, template, context)
