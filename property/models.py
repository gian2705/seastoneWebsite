from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save

# Properties.
from django.urls import reverse
from django.utils.text import slugify


class Property(models.Model):
    STATUS_CHOICES = (
        ('AVAILABLE', 'Available'),
        ('UNAVAILABLE', 'Unavailable')
    )

    TYPE_CHOICES = (
        ('SALE', 'For sale'),
        ('RENT', 'For rent')
    )
    FEATURED = (
        ('YES', 'Featured'),
        ('NO', 'Not Featured')
    )
    CITIES = (
        ('DAR ES SALAAM', 'Dar'),
        ('DODOMA', 'Dodoma')
    )

    uploader = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=64, default='title')
    slug = models.SlugField(unique=True, default="title-slug")
    size = models.DecimalField("Size of Property(Sq M)", decimal_places=2, max_digits=10)
    bedNo = models.IntegerField("Number of Bedrooms")
    bathNo = models.IntegerField("Number of Bathrooms")
    features = models.TextField("Property Features")
    description = models.TextField("Property Description")
    type_of_property = models.CharField(max_length=25, choices=TYPE_CHOICES, default='SALE')
    status_of_property = models.CharField(max_length=25, choices=STATUS_CHOICES, default='AVAILABLE')
    location = models.CharField(max_length=128, default='location')
    city = models.CharField(max_length=64, default='Dar es salaam')
    price = models.DecimalField("Price(in $)", decimal_places=2, default="0.00", max_digits=10)
    featured = models.CharField(choices=FEATURED, default='YES', max_length=5)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home:property", kwargs={"slug": self.slug})

    class Meta:
        verbose_name_plural="Properties"


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(default='media_cdn/commercial_farming.jpeg')


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Property.objects.filter(slug=slug).order_by("-id")
    exsists = qs.exists()
    if exsists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Property)
