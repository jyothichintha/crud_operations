from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length


# Create your views here.

def insert_topic(request):
    lot=Topic.objects.all()
    d={'topics':lot}
    return render(request,'insert_topic.html',d)


def display_webpage(request):
    low=Webpage.objects.all()
    low=Webpage.objects.order_by('name')
    low=Webpage.objects.order_by('-name')
    low=Webpage.objects.order_by(Length('name'))
    low=Webpage.objects.order_by(Length('name').desc())
    low=Webpage.objects.filter(name__startswith='r')
    low=Webpage.objects.filter(name__endswith='i')
    low=Webpage.objects.filter(name__in=('vijji','Raji'))  
    low=Webpage.objects.filter(name__contains='a')
    low=Webpage.objects.filter(name__regex='/w{4}')
    #low=Webpage.objects.all()  
    d={'webpage':low}
    return render(request,'display_webpage.html',d)

def display_access(request):
    loa=Accessrecord.objects.all()
    loa=Accessrecord.objects.filter(date__gt='2022-10-23')
    loa=Accessrecord.objects.filter(date__lt='2022-10-23')
    loa=Accessrecord.objects.filter(date__gte='2022-10-23')  
    loa=Accessrecord.objects.filter(date__lte='2022-10-23')
    loa=Accessrecord.objects.all()
    loa=Accessrecord.objects.filter(date__month='5')
    loa=Accessrecord.objects.filter(date__year='2022')
    loa=Accessrecord.objects.filter(date__day='13')




    d={'access':loa}
    return render(request,'display_access.html',d)