from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Hartal(models.Model):
    title=models.CharField(max_length=264)
    type=models.CharField(max_length=264,default="")
    description=models.TextField(blank=True)
    published_date=models.DateTimeField(default=timezone.now())

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("hartal_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title
