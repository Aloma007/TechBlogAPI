from django.contrib import admin
from django.urls import path, include # Make sure include is imported!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')), # This routes traffic to your blog app
    # Added line to enable the Login/Logout button in the Browsable API
    path('api-auth/', include('rest_framework.urls')),
]