from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, viewsets

from .views import create_short_code
from .models import UrlMapping
from .serializers import UrlMappingSerializer
from .utils import generate_qr_code


# API view
# class UrlMappingAPIView(APIView):
#
#     def get(self, request):
#         urls = UrlMapping.objects.all()
#         serializer = UrlMappingSerializer(urls,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#
#     def post(self, request):
#
#         serializer = UrlMappingSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         original_url = serializer.validated_data["original_url"]
#         existing_url = UrlMapping.objects.filter(original_url=original_url).first()
#
#         # URL already exists
#         if existing_url:
#             short_url = request.build_absolute_uri(f"/{existing_url.short_code}/")
#             qr_code = generate_qr_code(short_url)
#
#             return Response({
#                     "short_url": short_url,
#                     # "qr_code": qr_code,
#                     "message": "URL already exists"
#                 },status=status.HTTP_200_OK)
#
#         # Create new short URL
#         url_mapping = serializer.save(short_code=create_short_code())
#         short_url = request.build_absolute_uri(f"/{url_mapping.short_code}/")
#         qr_code = generate_qr_code(short_url)
#
#         return Response({
#                 "short_url": short_url,
#                 # "qr_code": qr_code,
#                 "message": "URL shortened successfully"
#             },status=status.HTTP_201_CREATED)
#
#
# class UrlMappingDetailAPIView(APIView):
#     def get_url_object(self, short_code):
#         try:
#             return UrlMapping.objects.get(short_code=short_code)

#         except UrlMapping.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, short_code):
#         url = self.get_url_object(short_code)
#         serializer = UrlMappingSerializer(url)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#
#     def delete(self, request, short_code):
#         url = self.get_url_object(short_code)
#         url.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# Generic API view
class UrlMappingAPIView(generics.ListCreateAPIView):
    queryset = UrlMapping.objects.all()
    serializer_class = UrlMappingSerializer


class UrlMappingDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UrlMapping.objects.all()
    serializer_class = UrlMappingSerializer
    lookup_field = 'short_code'

# ModelViewSet
class UrlMappingAPIViewSet(viewsets.ModelViewSet):
    queryset = UrlMapping.objects.all()
    serializer_class = UrlMappingSerializer
