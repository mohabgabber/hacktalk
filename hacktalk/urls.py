from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # * Apps
    path("", include("land.urls")),
    path("chat/", include("chat.urls")),
    path("notifications/", include("notifications.urls")),
    path("post/", include("posts.urls")),
    path("paper/", include("research.urls")),
    path("auth/", include("users.urls")),
]
