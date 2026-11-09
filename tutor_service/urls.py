from django.contrib import admin
from django.urls import path
from core.views import index_page, tutors_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('api/tutors/', tutors_api),
]
