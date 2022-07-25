from django.contrib import admin
from splitfile.models import User, CSVFile, JSONFile

# Register your models here.
admin.site.register(User)
admin.site.register(CSVFile)
admin.site.register(JSONFile)
