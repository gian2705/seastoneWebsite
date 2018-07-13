from django.db import models

# Create your models here.


class Request(models.Model):
    name = models.CharField(max_length=64, verbose_name='Message from')
    phoneNo = models.CharField(max_length=20, verbose_name="Phone Number")
    email = models.EmailField(verbose_name='Email')
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Messages'
        verbose_name = 'Customer Message'
