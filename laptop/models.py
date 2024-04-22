from django.db import models

# Create your models here.


class Product(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    rate = models.FloatField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ноутбук'
        verbose_name_plural = 'Ноутбуки'
        db_table = 'products'

