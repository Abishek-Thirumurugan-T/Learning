from django.contrib import admin
from .models import Veggie #always shows error when ran independently
#to import .json into mysql table through admin pannel
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class ProductResource(resources.ModelResource):
   class Meta:
      model = Veggie
class ProductAdmin(ImportExportModelAdmin):
   resource_class = ProductResource

admin.site.register(Veggie, ProductAdmin)