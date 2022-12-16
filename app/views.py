from django.shortcuts import render
from django.db.models.functions import Length

# Create your views here.
from django.db.models import Q

from app.models import *
def display_topics(request):
    LTO=Topic.objects.all()
    # LTO=Topic.objects.get(topic_name='cricket11')
    d={'LTO':LTO}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    LWO=Webpage.objects.all()

    # retrieving techniques

    LWO=Webpage.objects.filter(name='ABC')
    LWO=Webpage.objects.filter(name='Ronaldo')
    LWO=Webpage.objects.all()[3:7:]
    LWO=Webpage.objects.all().order_by('name')
    LWO=Webpage.objects.all().order_by('-name')
    LWO=Webpage.objects.filter(topic_name='cricket11').order_by('name')
    LWO=Webpage.objects.filter(topic_name='cricket11').order_by('-name')
    LWO=Webpage.objects.all().order_by('topic_name')
    LWO=Webpage.objects.all().order_by(Length('name'))
    LWO=Webpage.objects.all().order_by(Length('name').desc())
    LWO=Webpage.objects.exclude(topic_name='chess')

    # feild lookups

    LWO=Webpage.objects.filter(name__startswith='r')
    LWO=Webpage.objects.filter(name__endswith='c')
    LWO=Webpage.objects.filter(name__contains='b')
    LWO=Webpage.objects.filter(name__startswith='X')
    LWO=Webpage.objects.filter(name__in=('virat','XYZ','Ronaldo'))
    LWO=Webpage.objects.filter(name__regex='^A\w{2}')
    LWO=Webpage.objects.filter(name__regex='^R\w')

    # to check multiple conditions by using Q(query) objects.

    LWO=Webpage.objects.filter(Q(name__startswith='a') & Q(topic_name='cricket11'))
    LWO=Webpage.objects.filter(Q(name__startswith='a') | Q(topic_name='cricket11'))
    LWO=Webpage.objects.filter(Q(name__contains='y') & Q(name__contains='k'))
    LWO=Webpage.objects.filter(Q(name__contains='y') | Q(name__contains='k'))
    

    d={'LWO':LWO}
    return render(request,'display_webpages.html',d)

def display_accessrecords(request):
    LAO=AccessRecords.objects.all()

    # field lookups for date

    LAO=AccessRecords.objects.filter(date='1983-09-12')
    LAO=AccessRecords.objects.filter(date__month='10')
    LAO=AccessRecords.objects.filter(date__day='12')
    LAO=AccessRecords.objects.filter(date__year='1999')
    LAO=AccessRecords.objects.filter(Q(date__month='10') & Q(date__day='23'))
    LAO=AccessRecords.objects.filter(Q(date__month='10') & Q(date__year='2002'))
    LAO=AccessRecords.objects.filter(Q(date__month='10') | Q(date__year='2002'))
    # LAO=AccessRecords.objects.filter(Q(name='Ronaldo') | Q(date__year='2002')) # error will come
    LAO=AccessRecords.objects.all()

    # comparision feild lookups

    LAO=AccessRecords.objects.filter(date__year__gt='1999')
    LAO=AccessRecords.objects.filter(date__year__gte='1999')
    LAO=AccessRecords.objects.filter(date__year__lt='1999')
    LAO=AccessRecords.objects.filter(date__year__lte='1999')
    LAO=AccessRecords.objects.filter(Q(date__year__lte='1999') & Q(date__day='12'))
    LAO=AccessRecords.objects.filter(Q(date__year__gte='1999') | Q(date__day='23'))
    LAO=AccessRecords.objects.filter(Q(date__year__gte='1999') & Q(date__day='23') & Q(date__month='10'))

    LAO=AccessRecords.objects.filter(Q(id=2) & Q(date__year='2001'))
    LAO=AccessRecords.objects.filter(Q(id=2) | Q(date__year='1999'))
    #LAO=AccessRecords.objects.all()
    
    
    d={'LAO':LAO}
    return render(request,'display_accessrecords.html',d)

