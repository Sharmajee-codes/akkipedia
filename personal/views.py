from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'personal/home.html')

def contact(request):
	return render(request, 'personal/contact.html', {'content':['If you would like to contact me, Please email me','sample@sample.com']})

def about(request):
	return render(request, 'personal/about.html')	


