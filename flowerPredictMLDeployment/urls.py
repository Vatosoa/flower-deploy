from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('irisApp.urls')),
    #path('',include('basicConcepts.urls')),
    path("admin/", admin.site.urls),
]
