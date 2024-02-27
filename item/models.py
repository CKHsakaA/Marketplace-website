from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to="category_imagesScalae", null=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"    
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name="items", on_delete=models.CASCADE)
    itemname = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    manufacturer = models.CharField(max_length = 64)
    price = models.IntegerField()
    image = models.ImageField(upload_to="item_images", null=True)
    is_sold = models.BooleanField(default = False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category}|{self.itemname} by {self.manufacturer} : Rs. {self.price} "