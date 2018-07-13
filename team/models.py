from django.db import models

# Team model and its characteristics.


class Team(models.Model):
    name = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    picture = models.FileField()
    phoneNo = models.CharField(max_length=20, default='+255 687 340 202')
    linkedin = models.URLField()
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Team members"
