from django.urls import path, include
from rest_framework.views import APIView
from rest_framework.routers import DefaultRouter
from url_shortener import views
from .apis import UrlMappingAPIView, UrlMappingDetailAPIView, UrlMappingAPIViewSet

router = DefaultRouter()
router.register('api/v1/urls', UrlMappingAPIViewSet)

urlpatterns = [
    path("", views.url_shortener, name="url_shortener"),
    path("<str:short_code>/", views.redirect_url, name="redirect_url"),
    # path("api/v1/urls/", UrlMappingAPIView.as_view(), name="apis"),
    # path("api/v1/urls/<str:short_code>/", UrlMappingDetailAPIView.as_view(), name="apis-details"),
    path('',include(router.urls)),
]