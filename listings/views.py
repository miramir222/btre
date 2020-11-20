from django.shortcuts import render,get_object_or_404
from .models import Listing
from realtors.models import Realtor
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from listings.choices import state_choices,price_choices,bedroom_choices
# Create your views here.

def index(request):
    listings = Listing.objects.order_by("-list_date").filter(is_published=True)
    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings' : paged_listings
    }
    return render(request,'listing/listings.html', context)

def listing(request,listing_id):
    requestedListing =get_object_or_404(Listing,pk=listing_id)
    context={
        "listing":requestedListing
    }
    return render(request,'listing/listing.html',context)
def search(request):
    queryset_list = Listing.objects.order_by("-list_date")
    print(request.GET['keywords'])
    if "keywords" in request.GET  and request.GET.get("keywords"):
        print(">>>>>>>>>>>>>>> testings1")
        keywords = request.GET['keywords']
        queryset_list = queryset_list.filter(description__icontains=keywords)
    if "city" in request.GET and request.GET.get("city"):
        city = request.GET['city']
        queryset_list = queryset_list.filter(city__iexact=city)
    if "state" in request.GET and request.GET.get("state"):
        state = request.GET['state']
        queryset_list = queryset_list.filter(state__iexact=state)
    if "bedrooms" in request.GET and request.GET.get("bedrooms"):
        bedrooms = request.GET['bedrooms']
        queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
    if "price" in request.GET and request.GET.get("price"):
        price = request.GET['price']
        queryset_list = queryset_list.filter(price__lte=price)
    context = {
        'price_choices' : price_choices,
        'bedroom_choices' : bedroom_choices,
        'state_choices' : state_choices,
        'listings' : queryset_list,
        "values": request.GET
    }
    return render(request,'listing/search.html',context)
