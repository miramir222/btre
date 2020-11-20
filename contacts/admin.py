from django.contrib import admin
from .models import Contact
# Register your models here.
class contactAdmin(admin.ModelAdmin):
    list_display = ("id","name","listing","email","phone")
    list_display_links = ('id','name')
    search_fields = ('name','listing')

admin.site.register(Contact,contactAdmin)