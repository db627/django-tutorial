from django.db import models #import django models

class User(models.Model): #create a User model
    first_name = models.CharField(max_length=100) #Create a first Name field
    last_name = models.CharField(max_length=100) #Create a last name field
    email = models.EmailField(default='example@example.com', max_length=100) #Create an email field
    
    def __str__(self):
        return self.first_name