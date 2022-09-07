from django.db import models
from django.core.exceptions import ValidationError


class Item(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

ATTRIBUTE_TYPE_CHOICES = [
    ('text', 'Text'),
    ('int', 'Integer'),
    ('float', 'Float'),
    ('boolean', 'Boolean'),
    ('date', 'Date'),
    ('time', 'Time'),
    ('datetime', 'Datetime'),
    # ('file', 'File'),
    # ('image', 'Image'),
    ('url', 'URL'),
    ('email', 'Email')
]

class Attribute(models.Model):
    attribute_name = models.CharField(max_length=100)
    attribute_type = models.CharField(max_length=100, choices=ATTRIBUTE_TYPE_CHOICES)

    def __str__(self):
        return self.attribute_name + ' - ' + self.attribute_type


class AttributeValue(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    # item = models.ForeignKey(Item, on_delete=models.CASCADE)
    value_text = models.CharField(max_length=1024, blank=True, null=True)
    value_int = models.IntegerField(blank=True, null=True)
    value_float = models.FloatField(blank=True, null=True)
    value_boolean = models.BooleanField(blank=True, null=True)
    value_date = models.DateField(blank=True, null=True)
    value_time = models.TimeField(blank=True, null=True)
    value_datetime = models.DateTimeField(blank=True, null=True)
    # value_file = models.FileField(blank=True, null=True)
    # value_image = models.ImageField(blank=True, null=True)
    value_url = models.URLField(blank=True, null=True)
    value_email = models.EmailField(blank=True, null=True)


    def __str__(self):
        return self.attribute.attribute_name + ' - ' + self.attribute.attribute_type

    def clean(self):
        dct = {}
        data_dct = {}
        entered_values = []
        data_type = self.attribute.attribute_type

        for field in self._meta.get_fields():
            if field.name.startswith('value_'):
                data_dct[field.name.split('_')[1]] = getattr(self, field.name)

        for key, value in data_dct.items():
            if value is not None:
                entered_values.append(key)

        if len(entered_values) == 0 :
            dct['value_' + data_type] = 'This field is required.'
            raise ValidationError(dct)
        
        # import ipdb; ipdb.set_trace()

        if len(entered_values) > 1:            
            raise ValidationError('Only one value can be entered. Please enter a value in the field "value ' + data_type + '" only. Remove the values from other fields.')

        if data_type not in entered_values:
            raise ValidationError('Value type does not match attribute type. Please enter a value in the field "value ' + data_type + '".')

            
            
