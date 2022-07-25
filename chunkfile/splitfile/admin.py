from django.contrib import admin
from splitfile.models import CSVFile, JSONFile

# Register your models here.
admin.site.register(CSVFile)
admin.site.register(JSONFile)
