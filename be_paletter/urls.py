from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from be_paletter import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('palettes/', views.palettes_list),
    path('palettes/<int:pk>/', views.palettes_detail),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)