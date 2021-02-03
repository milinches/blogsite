from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
STATUS = (
    (0, "Drafts"),
    (1, "publish")
)


class Articles(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

