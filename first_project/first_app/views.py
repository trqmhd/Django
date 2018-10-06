from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Webpage, Topic, AccessRecord


# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render (request, 'first_app/index.html', context= date_dict)


'''

def AppTwo(request):
    output = " <html> <em> My Second App </em> </html> "
    return HttpResponse(output)

'''
