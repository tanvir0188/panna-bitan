from django.db import models
# load user for the Item table
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    # changing the table name
    class Meta:
        # rearranging the list according to alphabets
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    # gets the names
    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(
        Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    # in case user doesn't want to provide info, use blank and null true
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    # 'upload_to' means django will store the images in the following file, or create a new file in that name
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User, related_name='items', on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
