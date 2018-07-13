from django.db import models

# Models for the home .


class Client(models.Model):
    name = models.CharField(max_length=128)
    title = models.CharField(max_length=128, default='Customer')
    testimony = models.TextField(default="Seastone is a great real estate company.")
    logo = models.FileField()
    link = models.URLField()

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    phoneno = models.CharField(max_length=128)
    faxno = models.CharField(max_length=128)
    email = models.EmailField()
    plot = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    facebook = models.CharField(max_length=128)
    twitter = models.CharField(max_length=128)
    linkedin = models.CharField(max_length=128)
    pinterest = models.CharField(max_length=128)
    googleplus = models.CharField(max_length=128)
    instagram = models.CharField(max_length=128)
    mission = models.TextField()
    vision = models.TextField()
    motto = models.TextField()
    objective = models.TextField()
    values = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural="Company details"


class Service(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.name


class Careers(models.Model):

    departments = [('agency', 'Agency'), ('management', 'Property Management'), ('valuation', 'Valuation'), ('devt', 'Property development'),
    ('survey', 'Architecture and Quantity survey'),('landscaping', 'Landscaping and Lawn-care'), ('facilities', 'Facilities management'),
                   ('analysis', 'Investment analysis'), ('furniture', 'Furniture, Fixture and Fitting'), ('planning', 'Urban and Rural planning'),
                   ('assesment', 'Environmental and Social Impact assessment'), ('land-survey', 'Land Survey')]
    full_name = models.CharField(max_length=128)
    email = models.EmailField()
    facebook = models.CharField(max_length=256)
    twitter = models.CharField(max_length=256)
    linkedin = models.CharField(max_length=256)
    instagram = models.CharField(max_length=256)
    interests = models.CharField(max_length=256)
    extracurriculars = models.CharField(max_length=256)
    department = models.CharField(choices=departments, max_length=64)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'Internship Requests'
        verbose_name = 'Internship Request'


