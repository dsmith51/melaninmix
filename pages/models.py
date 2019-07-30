from django.db import models


# Create your models here.
class HomePage(models.Model):
    picture = models.ImageField(upload_to='static/main/%Y/%m/%d')
    blurb = models.TextField(max_length=255)
    introduction = models.TextField(max_length=20000)

    def __str__(self):
        return self.blurb[:50]


class About(models.Model):
    picture = models.ImageField(upload_to='static/images/hosts/%Y/%m/%d')
    title = models.CharField(max_length=75, blank=True)
    text = models.TextField(max_length=10000)

    def __str__(self):
        return self.title


class Bio(models.Model):
    name = models.CharField(max_length=50)
    profile = models.ImageField(upload_to='static/images/karly/%Y/%m/%d')
    bio = models.TextField(max_length=10000)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(blank=False, max_length=50)
    email = models.EmailField(blank=False, unique=True)
    phone = models.IntegerField(blank=False)
    information = models.TextField(max_length=5000)

    def __str__(self):
        return self.name


def generate_filename(self, filename):
    url = "files/episodes/%s/%s" % (self, filename)
    return url


class Episode(models.Model):
    season = models.IntegerField(blank=False, default=1)
    number = models.IntegerField(blank=False, default=0)
    episode = models.FileField(upload_to=generate_filename)
    name = models.CharField(max_length=50)
    details = models.TextField(max_length=4000)
