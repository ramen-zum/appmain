from django.urls import path, include

urlpatterns = [
#    path('usersapp/', include('usersapp.urls')),
#    path('admin/', include('adminapp.urls')),
    path('', include('frontendapp.urls')),  
    path('', include('yapi_app.urls')),
      
]
