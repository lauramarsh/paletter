from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from be_paletter import views

urlpatterns = [
    path('palettes/', views.palettes_list),
    path('palettes/<int:pk>/', views.palettes_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)