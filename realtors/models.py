from django.db import models

# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=30)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.name