from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from django.http import Http404

#The manager class defines what and how the user and superuser should be created.

class UserManager(BaseUserManager):
    def get_User_object_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist,ValueError, TypeError):
            return Http404
        
    def create_user(self, username, email, password=None, **extra_fields):
        """
            Create and return user with a username, email, password, and **extra_fields
        """
        try:
            if username is None:
                raise TypeError("User must have a username")
            if email is None:
                raise TypeError("User must have an email")
            if password is None:
                raise TypeError("User must have a password")
        except (TypeError,ObjectDoesNotExist,ValueError) as e:
            raise e
        except Exception as e:
            print(f"{e} was the Error I caught")

        user = self.model(username=username, email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user
    
    def create_superuser(self, username, password, email, **extra_fields):
        """
            creates user as a superuser  with admin prividges
        """

        if email is None:
            raise TypeError("superuser must have an email")
        if username is None:
            raise TypeError("superuser must have username")
        if password is None:
            raise TypeError("superuser must have password")
        
        user = self.create_user(username, email, password, **extra_fields)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)

        return user





        
        
