from django.contrib import admin

from products.models import Basket, Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'description')
    fields = ('name', 'category', 'description', 'image', 'price', 'stripe_products_price_id', 'quantity')
    search_fields = ('name',)
    ordering = ('name',)


class AdminBasket(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
