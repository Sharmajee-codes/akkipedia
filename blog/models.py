from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
class Post(models.Model):
    title = models.CharField(max_length = 140)
    slug = models.SlugField(unique=True) 
    image = models.ImageField( 
            null=True, 
            blank=True, 
            upload_to='post/%Y/%m',)
    body =models.TextField()
    date =models.DateTimeField(db_index=True, auto_now=True )
    updateddate =models.DateTimeField(db_index=True, auto_now=True)
    author = models.CharField(max_length=50, default='Admin')
    

    def __unicode__(self):
    	return self.title

    def __str__(self):
    	return self.title 

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug":self.slug})

    class Meta:
        ordering = ["-id","date","-updateddate"]
def create_slug(instance,new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender,instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
pre_save.connect(pre_save_post_receiver,sender=Post)