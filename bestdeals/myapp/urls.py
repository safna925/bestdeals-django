from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from . import views  # Ensure this import is correct

urlpatterns = [
    # Public Pages
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),

    # User Authentication
    path('user/login/', views.login_view, name='user_login'),
    path('user/signup/', views.signup_view, name='user_signup'),
    path('user/logout/', views.logout_view, name='user_logout'),

    
    path('compare/', views.comparison_view, name='comparison'),
    # Product Comparison & Data Fetching
    #path('comparison/', views.comparison_view, name='comparison'),  # No need for login_required here
    #path('fetch-product-data/', views.get_product, name='fetch_product_data'),

    # Admin Authentication & Dashboard
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),  # Fixed function name
    path('admin/logout/', views.admin_logout, name='admin_logout'),
    
]

# Serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
