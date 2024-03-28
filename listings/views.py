from django.core.paginator import Paginator
from listings.choices import price_choices, bedroom_choices, state_choices
from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.shortcuts import render, get_object_or_404,redirect
from .models import Listing
from random import randrange,randint,random,uniform
import requests
from .forms import RecordNumberImport
from realtors.models import Realtor
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
import os
from django.core.files import File


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    # keyword
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(descreption__icontains=keywords)

    # city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

        # price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    # state_choices=[{i['state']:i['state']} for i in Listing.objects.all().values('state')] 

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)



def import_listing_data(request):
    first=Realtor.objects.first()
    last=Realtor.objects.last()
    if request.method == "POST":
        number_of_records=request.POST.get('number_of_records')
        random_user=requests.get('https://random-data-api.com/api/v2/users?size='+str(number_of_records)).json()
        comments=requests.get('https://jsonplaceholder.typicode.com/comments').json()
        for i in range(0,len(random_user)):
            title=random_user[i]['first_name']+" "+"Villa"
            address=random_user[i]['address']['street_name']+" "+random_user[0]['address']['street_address']
            city=random_user[i]['address']['city']
            state=random_user[i]['address']['state']
            zipcode=random_user[i]['address']['zip_code']
            descreption=comments[i]['body']
            price=randint(99999,1000001)
            bedrooms=randint(1,11)
            bathrooms=uniform(1,3)
            garage=randint(0,2)
            sqft=uniform(500,1000)
            lot_size=uniform(100,150)
            image=requests.get('https://source.unsplash.com/collection/2403558/480x480')
            image_1=requests.get('https://source.unsplash.com/collection/874077/480x480')
            image_2=requests.get('https://source.unsplash.com/collection/874077/480x480')
            image_3=requests.get('https://source.unsplash.com/collection/874077/480x480')
            image_4=requests.get('https://source.unsplash.com/collection/874077/480x480')
            image_5=requests.get('https://source.unsplash.com/collection/874077/480x480')
            image_6=requests.get('https://source.unsplash.com/collection/874077/480x480')
            
           
            listing=Listing(title=title,address=address,city=city,state=state,zipcode=zipcode,
            descreption=descreption,price=price,bedrooms=bedrooms,bathrooms=bathrooms,
            garage=garage,sqft=sqft,lot_size=lot_size
            )

            listing.realtor_id=randint(first.id,last.id)
            
            # img_temp = NamedTemporaryFile(delete=True)
            # img_temp.write(urlopen(image.url).read())
            # img_temp.flush()
            # filename, file_extension = os.path.splitext(image.url)
            # listing.photo_main.save(f"{name}{file_extension}", File(img_temp))

            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(image.url).read())
            img_temp.flush()
            listing.photo_main.save(f"{title}_main_.jpg", File(img_temp))

            photo_1 = NamedTemporaryFile(delete=True)
            photo_1.write(urlopen(image_1.url).read())
            photo_1.flush()
            listing.photo_1.save(f"{title}_1.jpg", File(photo_1))

            photo_2 = NamedTemporaryFile(delete=True)
            photo_2.write(urlopen(image_2.url).read())
            photo_2.flush()
            listing.photo_2.save(f"{title}_2.jpg", File(photo_2))

            photo_3 = NamedTemporaryFile(delete=True)
            photo_3.write(urlopen(image_3.url).read())
            photo_3.flush()
            listing.photo_3.save(f"{title}_3.jpg", File(photo_3))

            photo_4 = NamedTemporaryFile(delete=True)
            photo_4.write(urlopen(image_4.url).read())
            photo_4.flush()
            listing.photo_4.save(f"{title}_4.jpg", File(photo_4))
           
            photo_5 = NamedTemporaryFile(delete=True)
            photo_5.write(urlopen(image_5.url).read())
            photo_5.flush()
            listing.photo_5.save(f"{title}_5.jpg", File(photo_5))
           
            photo_6 = NamedTemporaryFile(delete=True)
            photo_6.write(urlopen(image_6.url).read())
            photo_6.flush()
            listing.photo_6.save(f"{title}_6.jpg", File(photo_6))
           
    
            listing.save()
        return redirect(request.path+'listing/')
    form = RecordNumberImport()
    payload = {"form": form}
    return render(
        request, "admin/listings/import_listing.html", payload
    )
