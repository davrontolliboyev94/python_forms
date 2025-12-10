from django.db import models


class NewsModel (models.Model):
    title=models .CharField(max_length=200)
    text=models .TextField()
    rasm = models.ImageField(upload_to='news/',blank=True, null=True)

    def __str__(self):
        return self.title
# Create your models here.
