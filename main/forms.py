from collections.abc import Iterator
from typing import Any
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


# register user form 
class registeruser(UserCreationForm):
    class Meta:
       model=User
       fields=['username','email','password1','password2']