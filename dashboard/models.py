from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('Equipment', 'Equipment'),
    ('Materials', 'Materials'),
    ('Apparatus', 'Apparatus'),
    ('Visual Aids', 'Visual Aids'),
)

STATUS = (
    ('Available', 'Available'),
    ('Unavailable', 'Unavailable'),
)



class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    specifications = models.CharField(max_length=10, blank=True, default=" ")
    category =  models.CharField(max_length=20, choices=CATEGORY)
    quantity = models.PositiveIntegerField(null=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS)

    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return f'{self.name} ({self.specifications})'
    
    
class Orders(models.Model):
    products = models.ManyToManyField(Product)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    

    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return f'{self.products} ordered by {self.staff.username}'
    
