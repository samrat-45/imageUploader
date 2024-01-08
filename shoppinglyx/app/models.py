from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.

STATE_CHOICES=(
    ("Dhaka","Dhaka"),
    ("Chittagong","Chittagong"),
    ("Dinajpur","Dinajpur"),
    ("Cumilla","Cumilla"),
    ("Faridpur","Faridpur"),
    ("Feni","Feni"),
    ("Habigang","Habigang"),
    ("Jamalpur","Jamalpur"),
    ("Jessore","Jessore"),
    ("Jhalakati","Jhalakati"), 
    ("Khulna","Khulna"),
    ("Pabna","Pabna"),
    ("Panchagarh","Panchagarh"),
    ("Noakhali","Noakhali"),
    ("Dinajpur","Dinajpur"),
    ("Rangpur","Rangpur"),
    ("Sylhet","Sylhet"),
    ("Tangail","Tangail"),
)
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city =models.CharField(max_length=50)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=51)
     
    def __str__(self):
        return str(self.id)
    

CATAGORY_CHOICES=(
    ( "M","Mobile"),
    ("L","Laptop"),
    ("TW","Top Wear"),
    ("BW","Bottom Wear")
)
class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    brand=models.CharField(max_length=100)
    catagory=models.CharField(choices=CATAGORY_CHOICES,max_length=2)
    Product_image=models.ImageField(upload_to="Productimg")
    
    def __str__(self):
        return str(self.id)
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    

STATUS_CHOICES=(
(  "Accepted","Accepted" ),
("Packed","Packed"),
("On The Way","On The Way"),
('delivered','delivered'),
('Cancel','Cancel'),
)

class Orderplaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(choices=STATUS_CHOICES,max_length=50,default="pending")