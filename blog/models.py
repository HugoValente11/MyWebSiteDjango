from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique= True)
    published = models.BooleanField(default= True)
    content = models.TextField(default="")
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='img')

    class Meta:
        ordering = ['-created']

        def __unicode__(self):
            return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('blogs.views.post', args=[self.slug])