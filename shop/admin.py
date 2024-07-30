from django.contrib import admin
from .models import Category, Product, Module, Size_product, Info, Info_module
from parler.admin import TranslatableAdmin

class ModuleInline(admin.StackedInline):
    model = Info_module

@admin.register(Info)
class InfoAdmin(TranslatableAdmin):
    list_display = ['name']
    inlines = [ModuleInline]

@admin.register(Size_product)
class SizeAdmin(TranslatableAdmin):
    list_display = ['name', 'slug']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}

@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ['name', 'slug']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}
    
class ModuleInline(admin.StackedInline):
    model = Module

@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated'
                ]
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    inlines = [ModuleInline]

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}