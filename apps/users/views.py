from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from .models import File
from .serializers import FileSerializer


class FileUploadView(generics.CreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FileSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FileListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FileSerializer

    def get_queryset(self):
        return File.objects.filter(user=self.request.user)
