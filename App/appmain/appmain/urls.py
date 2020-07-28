from django.urls import path, include

urlpatterns = [
    path('usersapp/', include('usersapp.urls')),
#    path('partners/', include('partnersapp.urls')),
    path('admin/', include('adminapp.urls')),    
]
