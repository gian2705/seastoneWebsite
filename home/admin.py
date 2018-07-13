from django.contrib import admin
from .models import Client, Company, Service, Careers

admin.site.register(Company)
admin.site.register(Client)
admin.site.register(Service)
admin.site.register(Careers)