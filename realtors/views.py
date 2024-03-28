from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .forms import RecordNumberImport
from .models import Realtor
import requests
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
import os

# Create your views here.
def import_realtor_data(request):
    if request.method == "POST":
        number_of_records=request.POST.get('number_of_records')
        data=requests.get('https://randomuser.me/api/?results='+str(number_of_records)).json()
        comments=requests.get('https://jsonplaceholder.typicode.com/comments').json()
        for i in range(0,len(data['results'])):
            name=data['results'][i]['name']
            name=name['title']+' '+name['first']+" "+name['last']
            photo=data['results'][i]['picture']['large']
            


            description=comments[i]['body']
            phone=data['results'][i]['phone']
            email=data['results'][i]['email']
            
            realtor=Realtor(name=name,photo=photo
                            ,description=description,phone=phone,
                            email=email
                            )
            realtor.save(False)
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(photo).read())
            img_temp.flush()
            filename, file_extension = os.path.splitext( photo)
            realtor.photo.save(f"{name}{file_extension}", File(img_temp))
            realtor.save()

        return redirect(request.path+'realtor/')
    form = RecordNumberImport()
    payload = {"form": form}
    return render(
        request, "admin/realtors/import_realtors.html", payload
    )
