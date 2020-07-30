from django.urls import path
from .views import HomePage,ImageAdminCategoryCreateView,ImageAdminCreateView
app_name = 'image_hub_admin_app'
urlpatterns = [
    path('',HomePage.as_view(),name = 'home_admin'),
    path('image-category-create/',ImageAdminCategoryCreateView.as_view(),name = 'image_category_create_admin'),
    path('image-create/',ImageAdminCreateView.as_view(),name = 'image_create_admin'),
    # path('image-create/',create_image_view,name = 'image_create_admin'),
]
