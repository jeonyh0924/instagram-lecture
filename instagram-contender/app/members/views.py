import os

from django.http import FileResponse
from django.shortcuts import render

from config import settings


def media_serve(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT.path),
    return FileResponse(open(file_path, 'rb'), content_type='image/jpeg')
