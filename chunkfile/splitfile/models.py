from django.db import models
from django.contrib.auth.models import User
# from chunkscripts import splitcsv_script, zipfile_script

# Create your models here.

class CSVFile(models.Model):
    # fields of the model
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False, blank=False) # Reference/link file to the user
    csv_file_upload = models.FileField(upload_to="uploads_for_csv/",null=False, blank=False) # file will be uploaded to MEDIA_ROOT / uploads_for_csv
    rows = models.PositiveIntegerField(default=100,null=False, blank=False)
    uploaded_at = models.DateTimeField(auto_now_add=True) # save date and time the uploaded csv file was created
    # split_csv_file = models.FilePathField() # Come back later to reference properfly


class JSONFile(models.Model):
    # fields of the model
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False, blank=False) # Reference/link file to the user
    json_file_upload = models.FileField(upload_to="uploads_for_csv/",null=False, blank=False) # file will be uploaded to MEDIA_ROOT / uploads_for_csv
    rows = models.PositiveIntegerField(default=100,null=False, blank=False)
    uploaded_at = models.DateTimeField(auto_now_add=True) # save date and time the uploaded csv file was created
    # split_json_file = models.FilePathField() # Come back later to reference properfly