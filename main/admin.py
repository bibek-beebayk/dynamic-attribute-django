from django.contrib import admin
from .models import Item, Attribute, AttributeValue 


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('attribute_name', 'attribute_type')
    search_fields = ('attribute_name',)


@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ('attribute', 'value_text', 'value_int', 'value_float', 'value_boolean', 'value_date', 'value_time', 'value_datetime', 'value_url', 'value_email')
    search_fields = ('attribute',)
