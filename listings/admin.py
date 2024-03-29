from django.contrib import admin
from .models import Listing
# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','address','city','state','price','realtor','is_published')
    list_display_links = ('id','title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title','city','state')
    list_per_page = 25

admin.site.register(Listing,ListingAdmin)
