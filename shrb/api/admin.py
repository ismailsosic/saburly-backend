from django.contrib import admin

from .models import Card

# Register your models here.
class CardAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_from', 'date_to', 'is_processed',)
    list_display_links = ('user',)
    list_filter = ('user', 'is_processed')


admin.site.register(Card, CardAdmin)
