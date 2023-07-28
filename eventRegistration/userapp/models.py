from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    )

    # user = models.ForeignKey()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='user_photo/',default='test.png', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.username

    
    def save(self, *args, **kwargs):
        # import pdb
        # pdb.set_trace()
        if self.gender == "male":
            self.photo = "male.png"
        
        elif self.gender == "female":
            self.photo = "female.png"
        
        else:
            self.photo = "test.png"
        
        super().save(*args, **kwargs)