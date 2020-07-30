from django.urls import path
from .views import HomePageView,ImageDetailView,ImageRedirectView

app_name = "image_hub_app"
urlpatterns = [
    path('home/', HomePageView.as_view() ,name="home"),
    path('detail/<int:pk>', ImageDetailView.as_view() ,name="image-details"),
    path('redirect/<int:pk>', ImageRedirectView.as_view() ,name="image-redirect"),
    
]
