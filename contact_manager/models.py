

from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    picture = models.ImageField(upload_to='contact_pictures', blank=True, null=True)
    relationship = models.CharField(max_length=100, blank=True)
    alternative_mobile_number = models.CharField(max_length=15, blank=True)
    present_address = models.TextField(blank=True)
    permanent_address = models.TextField(blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profession = models.CharField(max_length=100, blank=True)
    about = models.TextField(blank=True)
    facebook = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    personal_website = models.URLField(blank=True)
    other_field = models.FileField(upload_to='contact_files', blank=True, null=True)

