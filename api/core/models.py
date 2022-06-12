from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuarios(AbstractUser):
    pass
    #username = models.CharField("usuário", max_length=20)
    #password = models.CharField(max_length=8)
    #email = models.EmailField(max_length=254, unique=True, error_messages={'unique': "O email cadastrado já existe."})
    #is_staff = models.BooleanField(default=False)
    #is_superuser = models.BooleanField(default=False)
    

    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = []


#Usuarios._meta.get_field_by_name('email')[0]._unique=True