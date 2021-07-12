from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Snack (models.Model):
    # add name as a CharField with maximum length of 64 characters.
    # add purchaser ForeignKey related to Django’s built in user model with CASCADE delete option.
    # add description TextField
    name =models.CharField(max_length=64)
    purchaser = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    description =models.TextField()

    def __str__(self):
        return self.name


