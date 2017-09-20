from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.conf.urls import url
from django.contrib import admin,messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

def post_create(request):
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"<strong>Ohh Yeah !!</strong> Your post was successfully created", extra_tags='alert alert-success html_safe')
	context = {
		"form":form,
	}
	return render(request, "blog/form.html", context)
def post_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	context = {
		"title":instance.title,
		"instance":instance,
	}
	return render(request, "blog/post.html", context)


def post_list(request):
	queryset_list = Post.objects.all()
	paginator = Paginator(queryset_list, 2) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
	"object_list": queryset,
	"title":"Akkipedia|blog"
	}

	return render(request, "blog/blog.html", context)

def post_update(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"<strong>Ohh Yeah!!</strong> Your post was successfully saved", extra_tags='alert alert-success html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title":instance.title,
		"instance":instance,
		"form":form,
	}
	return render(request, "blog/form.html", context)

def post_delete(request, slug=None):
	instance = get_object_or_404(Post, slug=None)
	instance.delete()
	messages.success(request,"<strong>Hmm!!</strong> Your post was deleted", extra_tags='alert alert-danger html_safe')
	return redirect("blog:list")
