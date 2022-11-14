from django.contrib import admin
from tudoapp import models

# Register your models here.
admin.site.register(models.Retailer)
admin.site.register(models.Commodity)
admin.site.register(models.Order)
