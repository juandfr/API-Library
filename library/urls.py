from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework import routers

from books.api import viewsets as booksviewsets

route = routers.DefaultRouter()

route.register(r'books', booksviewsets.BooksViewSet, basename="Library")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('', include(route.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)