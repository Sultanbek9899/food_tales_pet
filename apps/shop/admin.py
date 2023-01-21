from django.contrib import admin

# Register your models here.

from apps.shop.models import ShopCategory, Product, ProductImage


@admin.register(ShopCategory)
class ShopCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug":("name",)}


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 4



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = [
            "name",
            "price", 
            "category",
            "is_available",
            "created",
            ]
    list_filter = [
        "category",
        "is_available",
        "created",
    ]
    search_fields = [
        "name", 
    ]
    list_editable = [
        "is_available",
    ]