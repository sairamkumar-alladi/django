from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(default='uncategorized', max_length = 100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'categories'

class Product (models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name= 'categories')
    product_name = models.CharField(max_length=120)
    desc = models.TextField()
    created_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.product_name
