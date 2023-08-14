from django.contrib.auth import get_user_model
from django.contrib.auth.context_processors import auth
from django.db import models

from registration.models import student

# Create your models here.

class book_types(models.Model):
    type = models.CharField(max_length=300, blank=False)

    def __str__(self):
        return self.type

class book(models.Model):
    book_type = models.OneToOneField(book_types, blank=False, on_delete=models.CASCADE)
    # level = models.CharField(choices=Level, max_length=100, blank=False)
    name_of_book = models.CharField(max_length=300, blank=False)
    user = models.ForeignKey(student,  blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.user