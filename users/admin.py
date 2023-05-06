from django.contrib import admin

from products.admin import AdminBasket
from users.models import EmailVerification, User


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('username',)
    inlines = (AdminBasket,)


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'expiration')
    fields = ('code', 'user', 'expiration', 'created')
    readonly_fields = ('created',)
