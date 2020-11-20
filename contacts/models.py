from django.db import models

# Create your models here.
class Contact(models.Model):
    listing_id = models.IntegerField()
    name = models.CharField(max_length=30)
    listing = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name