from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    nome = models.CharField(max_length = 100, blank = False, null = False);
    #foto aqui

    def __str__(self):
        return self.email
