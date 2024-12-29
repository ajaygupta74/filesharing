from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import FileResponse
from django.conf import settings
import base64

from services.models import File


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def download_file(request, user_id, file_id):
    if request.user.id != user_id:
        return Response({"status": False, "message": "Not Authorized"})
    file_obj = File.objects.filter(pk=file_id, is_active=True).first()
    if not file_obj or not file_obj.file:
        return Response({"status": False, "message": "Link Expired"})
    file_path = file_obj.file.path
    encoded_file = ""
    with open(file_path, 'rb') as f:
        file_data = f.read()
        encoded_file = base64.b64encode(file_data).decode('utf-8')
    return Response({
        "status": True,
        "file_name": file_obj.title,
        "file_data": encoded_file
    })
