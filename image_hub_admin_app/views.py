import logging
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,DeleteView,DetailView
from .forms import ImageCategoryCreateForm, ImageCreateForm
from image_hub_app.models import Category,ImageHub
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.
logger = logging.getLogger('django')

class HomePage(TemplateView):
    template_name = 'admin/home.html'
    
    def get_context_data(self,**kwargs):
        context        = super(HomePage,self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context
        
class ImageAdminCategoryCreateView(SuccessMessageMixin,CreateView):
    form_class          = ImageCategoryCreateForm
    template_name       = 'admin/image_category_create_from.html'
    success_url         = '/image-hub-admin/'
    success_message     = "sucess fully created"
class ImageAdminCreateView(SuccessMessageMixin,CreateView):
    form_class          = ImageCreateForm
    template_name       = 'admin/image_create_from.html'
    success_url         = '/image-hub-admin/'
    success_message     = "sucess fully created"