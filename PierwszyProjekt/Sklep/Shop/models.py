from django.db import models


class ShopCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Product(models.Model):
    NameOfProduct = models.CharField(max_length=255)
    Production_Date = models.DateField()
    Manufacturer = models.CharField(max_length=300)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    shop_category = models.ForeignKey(ShopCategory, related_name='products', on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey('auth.User',related_name='products', on_delete=models.CASCADE)

    class Meta:
        ordering = ('NameOfProduct',)

    def __str__(self):
        return self.NameOfProduct + ' ' + self.Manufacturer
