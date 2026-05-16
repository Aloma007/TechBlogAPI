from django.contrib import admin
from django.urls import path, include # Make sure include is imported!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')), # This routes traffic to your blog app
]