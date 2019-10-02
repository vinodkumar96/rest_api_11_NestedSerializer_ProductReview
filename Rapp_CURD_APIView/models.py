from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product (models.Model):
    p_id = models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=50)
    p_cost = models.DecimalField(max_digits=10,decimal_places=2)
    p_mfd = models.DateField()
    p_exd = models.DateField()

class Review(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='reviews')
    title = models.CharField(max_length=50)
    review = models.TextField()
    ratings = models.IntegerField()
    created_by = models.ForeignKey(User,null=True,on_delete=models.CASCADE)


