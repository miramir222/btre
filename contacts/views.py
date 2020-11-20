from django.shortcuts import render,redirect
from . models import Contact
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.
def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        if request.user.is_authenticated:
            hasContacted = Contact.objects.filter(listing_id=listing_id,user_id=request.user.id)
            if hasContacted:
                messages.error(request, "Your request Is Already submitted !!!")
                return redirect('/listings/' + listing_id)
        contact =Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)
        contact.save()
        send_mail(
            'Property Listing Enquiry',
            'There has been An Enquery For '+listing+" Sign Into The Admin Panel For Info",
            "worldhk@gmail.com",
            [realtor_email,],
            fail_silently=False
        )
        messages.success(request,"Your request has been submitted, a realtor will get back to you soon")
    return redirect('/listings/'+listing_id)