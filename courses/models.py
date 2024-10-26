from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name    


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(Category, related_name='courses')
    author_name = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class CartItem(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    courses=models.ForeignKey(Course, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)


