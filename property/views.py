from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from home.models import Company
from .models import Property
from urllib.parse import quote_plus
# Create your views here.


class PropertyView:

    def property_view(request, id):
        propert = get_object_or_404(Property, id=id)
        image_list = propert.images.all()
        share_string = quote_plus(propert.description)
        company = Company.objects.all()
        context = {
            "property": propert,
            "images": image_list,
            "share_string": share_string,
            "company_details": company
        }
        return render(request, "single-listings.html", context)

    def property_list(request):
        properties = Property.objects.all()
        company = Company.objects.all()

        paginator = Paginator(properties, 6)     #showing 9 properties
        page = page_get(request)
        properties = paginator.get_page(page)
        context = {
            "properties": properties,
            "company_details": company,
        }
        return render(request, "listings.html", context)


def search(request):
    return request.GET.get('keywordq')


def page_get(request):
    return request.GET.get('page')
