from django.db import models
# from django.shortcuts import reverse
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    category_name           = models.CharField(max_length=100,unique=True)
    title                   = models.CharField(max_length=100)
    description             = models.TextField()

    def __str__(self):
        return self.category_name

class ImageHub(models.Model):
    image                   = models.ImageField()
    title                   = models.CharField(max_length=100)
    number_of_people        = models.IntegerField(null=True,blank=False)
    description             = models.TextField()
    category                = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='cat')
    number_of_views         = models.IntegerField(verbose_name="view",default=0)
    number_of_downloads     = models.IntegerField(verbose_name="downloads",default=0)
    created_date            = models.DateField(auto_now_add=True,null=True,blank=True)
    
    class Meta:
        pass
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        
        return reverse('image-details',kwargs={id:self.id})    