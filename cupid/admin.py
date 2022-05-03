from django.contrib import admin
from .models import person
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
# Register your models here.

class personExport(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(person, personExport)
