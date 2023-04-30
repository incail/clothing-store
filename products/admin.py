from django.contrib import admin
from products.models import ProductCategory, Product, Basket

admin.site.register(ProductCategory)

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'description')
    fields = ('name', 'description', 'image', 'price', 'quantity')
    readonly_fields = ('description',)
    search_fields = ('name',)
    ordering = ('name',)


class AdminBasket(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
