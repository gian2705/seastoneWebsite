from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Company, Client, Service
from django.http import HttpResponseRedirect,Http404,HttpResponse
from property.models import Property
from team.models import Team
from customerMessages.models import Request
from customerMessages.forms import MessageForm
from django.contrib import messages
from home.forms import InternshipForm
from property import views
# The home view


def home(request):
    company = Company.objects.all()
    clients = Client.objects.all()
    propert = Property.objects.all()
    ceo = get_object_or_404(Team, title='CEO')
    # include the Search voodoo here

    keywordq = request.GET.get('inputKeyword')
    cityq = request.GET.get('inputCity')
    bednoq = request.GET.get('inputBedNo')
    bathnoq = request.GET.get('inputBathNo')

    if keywordq:
        propert = Property.objects.filter(Q(title__icontains=keywordq) | Q(description__icontains=keywordq)).distinct()

    if not propert:
        messages.error(request, "No properties with such characteristics. ")

    context = {
        "company_details": company,
        "properties": propert,
        "clients": clients,
        "ceo": ceo
    }

    return render(request, "index.html", context)


def about_us_view(request):
    team = Team.objects.all()
    company = Company.objects.all()
    properties = Property.objects.all()

    context = {
        "team": team,
        "company_details": company,
        "properties": properties
    }
    return render(request, "about-us.html", context)


def contact_view(request):
    company = Company.objects.all()

    #customer contact form - Saved to the database or emailed. or both

    form = MessageForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Message Sent Successfully!")
        return HttpResponseRedirect(redirect_to='contact-us')
    # saving to the database
    return render(request, 'contact.html', context={"company_details": company, 'form': form})


def career_view(request):
    company = Company.objects.all()
    form = InternshipForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Thank you for registering for Internship. We will get back to u as soon as we can")
        return HttpResponseRedirect(redirect_to='career')

    context = {
        "company_details": company,
        'internship_form': form
    }
    return render(request, 'Careers.html', context)
