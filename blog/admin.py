from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title","updateddate","date"]
	list_display_link = ["updateddate"]
	list_filter = ["updateddate","date"]
	search_fields = ["title","content"]

	class Meta:
			model = Post
admin.site.register(Post, PostModelAdmin)
