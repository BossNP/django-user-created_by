from django.db import models
from user.models import User

class Gender(models.Model):
    gender_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    definition = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        to=User, 
        on_delete=models.CASCADE, 
        related_name='gender_created_by',
        blank=True, 
        null=True
        )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        to=User, 
        on_delete=models.CASCADE, 
        related_name='gender_updated_by',
        blank=True, 
        null=True
        )
    updated_on = models.DateTimeField(auto_now=True)

    def delete(self):
        self.is_active = False
        self.save()

    def __str__(self):
        gender_id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=50)
        definition = models.CharField(max_length=250)
        is_active = models.BooleanField(default=True)
        string = f"{gender_id}, {name}, {definition}, {is_active}"
        return string


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    gender_id = models.ForeignKey(
        to=Gender, 
        on_delete=models.CASCADE, 
        related_name='customer_gender'
        )
    created_by = models.ForeignKey(
        to=User, 
        on_delete=models.CASCADE, 
        related_name='customer_created_by',
        blank=True, 
        null=True
        )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        to=User, 
        on_delete=models.CASCADE, 
        related_name='customer_updated_by',
        blank=True, 
        null=True
        )
    updated_on = models.DateTimeField(auto_now=True)