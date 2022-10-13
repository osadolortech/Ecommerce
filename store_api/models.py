from django.db import models
from user.models import User

# Create your models here.

def upload_to(instance, filename):
    return 'image/{filename}'.format(filename=filename)

class Category(models.Model):
    title = models.CharField(max_length=50)
    category_image = models.ImageField(upload_to=upload_to,default='image/default.jpg')
    description =  models.CharField(max_length=150)

    def __str__(self):
        return self.title


def upload_to(instance, filename):
    return 'image/{filename}'.format(filename=filename)

class Product(models.Model):
    product_name = models.CharField(max_length=150)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name="product", blank=True,null=True)
    product_iamge = models.ImageField(upload_to=upload_to,default='image/default.jpg')
    old_price = models.FloatField(default=0.0)
    discount = models.BooleanField(default=False)
    inventory = models.IntegerField(default=0)
    flash_sale = models.BooleanField(default=False)

    @property
    def price(self):
        if self.discount:
            new_price = self.old_price - ((30/100) * self.old_price)
        else:
            new_price = self.old_price
        return new_price

    def __str__(self):
        return self.product_name 




class Chart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="chart_items")
    product= models.ForeignKey(Product, on_delete=models.CASCADE,related_name="product_in_chart")



class Checkout(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="checkout_items")
    payment_on_delivery = models.BooleanField(default=False)
    card_payment = models.BooleanField(default=False)

   

















    