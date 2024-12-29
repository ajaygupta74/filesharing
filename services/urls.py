from django.urls import path

from services.apis import download_file

urlpatterns = [
    path('files/download/<int:user_id>/<int:file_id>/',
         download_file,
         name="download_file"),
]
