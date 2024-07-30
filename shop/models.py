from django.db import models
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields
from django.contrib.auth.models import User
from accounts.models import Profile

# Create your models here.

class Size_product(TranslatableModel):
    
    translations = TranslatedFields(
        name = models.CharField(max_length=200),
        slug = models.SlugField(max_length=200, unique=True),
    )
        
    def __str__(self):
        return self.name


class Category(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=200),
        slug = models.SlugField(max_length=200, unique=True),
    )
    
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    
class Product(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=200),
        slug = models.SlugField(max_length=200),
        description = models.TextField(blank=True),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    is_released = models.BooleanField(default=False)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    Size = models.ForeignKey(Size_product, on_delete=models.CASCADE, null=True, blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id,
                                                    self.slug])

    class Meta:
        indexes = [
            models.Index(fields=['-created']),
        ]
        
    def __str__(self):
        return self.name
    

class Module(models.Model):
    product = models.ForeignKey(Product,
                               related_name='modules',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f'{self.title}'