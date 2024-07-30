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
    image_1 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image_2 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image_3 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image_4 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image_5 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image_6 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image_7 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    unit_price = models.CharField(max_length=25)
    price = models.CharField(max_length=25)
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
    
class Info(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=200),
    )

    def __str__(self) -> str:
        return self.name
    
class Info_module(models.Model):
    info = models.OneToOneField(Info, related_name='info', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/info/%Y/%m/%d', blank=True)
    image_1 = models.ImageField(upload_to='products/info/%Y/%m/%d', blank=True)
    image_2 = models.ImageField(upload_to='products/info/%Y/%m/%d', blank=True)
    image_3 = models.ImageField(upload_to='products/info/%Y/%m/%d', blank=True)
    image_4 = models.ImageField(upload_to='products/info/%Y/%m/%d', blank=True)
    image_5 = models.ImageField(upload_to='products/info/%Y/%m/%d', blank=True)
    image_6 = models.ImageField(upload_to='products/info/%Y/%m/%d', blank=True)
    image_7 = models.ImageField(upload_to='products/info/%Y/%m/%d', blank=True)
    image_9 = models.ImageField(upload_to='products/info/%Y/%m/%d', blank=True)
    image_10 = models.ImageField(upload_to='products/info/%Y/%m/%d', blank=True)
    image_11 = models.ImageField(upload_to='products/info/%Y/%m/%d', blank=True)
    image_12 = models.ImageField(upload_to='products/info/%Y/%m/%d', blank=True)
    image_13 = models.ImageField(upload_to='products/info/%Y/%m/%d', blank=True)
    image_14 = models.ImageField(upload_to='products/info/%Y/%m/%d', blank=True)
    image_15 = models.ImageField(upload_to='products/info/%Y/%m/%d', blank=True)
    image_16 = models.ImageField(upload_to='products/info/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f'{self.title}'
        

class Module(models.Model):
    product = models.ForeignKey(Product,
                               related_name='modules',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f'{self.title}'