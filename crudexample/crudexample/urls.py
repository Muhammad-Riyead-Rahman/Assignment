from django.contrib import admin  
from django.urls import path 

from django.conf.urls.static import static
from employee import views  


urlpatterns = [
    # Your existing URL patterns
    
    path('emp', views.emp),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),

    # Add a URL pattern for the empty path
    path('', views.show),  # Replace 'home_view' with the view you want to use for your homepage
]  


