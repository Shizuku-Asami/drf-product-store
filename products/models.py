from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()



class ProductBill(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sold_at = models.DateTimeField()
    quantity = models.PositiveIntegerField()
    bill = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.name} | {self.bill}"
