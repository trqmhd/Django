from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import TemplateView, ListView, DetailView
from .models import StockInfo
from django.http import HttpResponse


# Create your views here.



class StockListView(ListView):
    queryset = StockInfo.objects.all()
    template_name = "stock_info/stock_list_view.html"


    def get_context_data(self, *args, **kwargs):
        context = super(StockListView, self).get_context_data(*args, **kwargs)
        print(context)
        return context


def stock_list_view(request):
    queryset = StockInfo.objects.all()
    context = {
        'object_list' : queryset
    }
    return render(request, "stock_info/stock_list_view.html", context)









class StockDetailView(DetailView):
    queryset = StockInfo.objects.all()
    template_name = "stock_info/stock_detail_view.html"


    def get_context_data(self, *args, **kwargs):
        context = super(StockDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context





def stock_detail_view(request, pk= None, *args, **kwargs):

    #instance = get_object_or_404(StockInfo, pk=pk)
    try:
        instance = StockInfo.objects.get (id =pk)
    except StockInfo.DoesNotExist:
        #print("This stock are not available")
        raise Http404("Stock doesn't exist")
    except:
        print("Sorry")

    context = {
        'object': instance
    }

    return render(request, "stock_info/stock_detail_view.html", context)














