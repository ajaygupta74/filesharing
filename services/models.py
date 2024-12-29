import os
from django.db import models
from users.models import User
from django.core.exceptions import ValidationError



def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # Get the file extension
    valid_extensions = ['.pptx', '.docx', '.xlsx']
    if ext.lower() not in valid_extensions:
        raise ValidationError(f'Unsupported file extension. Allowed extensions are: {", ".join(valid_extensions)}.')


class File(models.Model):
    user = models.ForeignKey(User, related_name="files", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='uploads/files/', validators=[validate_file_extension])
    is_active = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
