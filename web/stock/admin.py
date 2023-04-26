from django.contrib import admin
from .models import Item

# Register your models here.
# class ItemAdmin(admin.ModelAdmin):
#     list_display = ('category', 'state')
#     list_filter = ('category',)

admin.site.register(Item)
# admin.site.register(Item, ItemAdmin)