from django.contrib import admin
from users.models import User
from products.admin import AdminBasket

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('username',)
    inlines = (AdminBasket,)

