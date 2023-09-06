from django.contrib.auth.models import AbstractUser,Group,Permission
from django.db import models



class Bnb (models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(null=True, upload_to='bnb/rental/bnb_images')
    rate = models.DecimalField(max_digits=8, decimal_places=2)



#this is the default login django

class User (AbstractUser):
    #provides a diferentiation between django used name user and my custom user

    def __str__(self):
        return self.username

    def get_full_name(self):
        return f"{self.first_name}  {self.last_name}"






class Booking (models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    bnb =models.ForeignKey (Bnb, on_delete =models.CASCADE)
    check_in_date= models.DateField()
    check_out_date = models.DateField()
    total_price= models.DecimalField(max_digits=8, decimal_places= 2)

#saving the calculations as well as getting total pice

    def save(self,*args,**kwargs):
        price_per_day= self.Bnb.rate
        num_of_days =(self.check_out_date - self.check_in_date).days
        self.total_price = price_per_day * num_of_days
        super().save(*args, **kwargs)

class Review(models.Model):
    user = models.ForeignKey(User ,on_delete =models.CASCADE)
    bnb = models.ForeignKey(Bnb, on_delete=models.CASCADE)
    #user gets to rate the bnbs between 1 and 6 so 1,2,3,4,5
    rating = models.IntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))

    comment = models.TextField()

#prevents the user rating the same bnb twice

    class Meta:
        unique_together = ('user', 'bnb')










# Create your models here.
