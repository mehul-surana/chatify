from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("chat.urls")),
    path("rooms/", include("room.urls")),
    path("admin/", admin.site.urls),
]
