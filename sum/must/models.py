from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator



class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    


class Product(models.Model):
    name = models.CharField(max_length=200, null= False)
    description = models.TextField(blank=True)
    price = models.FloatField(default=1)

    def __str__(self):
        return self.name
    
class User(models.Model):
    name = models.CharField(max_length=200, null=False)
    surname = models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return f'{self.name} {self.surname}'
    
class Review(BaseModel):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    content = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
