from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,DeleteView,DetailView,RedirectView,FormView
import logging
from image_hub_app.models import ImageHub
from django.shortcuts import  get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .mixins import FindMethodMixin,SerializeMixin
import json
from django.http import JsonResponse
from django.core import serializers
# Create your views here.

logger = logging.getLogger('django')

class HomePageView(TemplateView,FindMethodMixin,SerializeMixin):
   
    template_name = "image_hub_app/home.html"
    model = ImageHub

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(HomePageView, self).dispatch(request, *args, **kwargs)

    def post(self,request,*args,**kwargs):
        context             = super(HomePageView,self).get_context_data(**kwargs)
        context['obj_list'] = self.model.objects.all()
        print(request.body)
        qs_json             = self.serialize(request,*args,**kwargs)
        return JsonResponse(qs_json,safe=False)


    # def get(self, request, *args, **kwargs):
    #     context = self.get_context_data(**kwargs)
    #     return self.render_to_response(context)
   

    def get_context_data(self,**kwargs):
        context = super(HomePageView,self).get_context_data(**kwargs)
        if self.request.body:

            print(self.request.body)
            json_data = json.loads(request.body)
        
            return context
        else:
            context['obj_list'] = ImageHub.objects.all()[0:3]
            return context  
    

class ImageDetailView(DetailView):
    model               = ImageHub
    template_name       = 'image_hub_app/image_details.html'
    context_object_name = 'obj'
    
    
    def get_object(self):
        try:
            obj = get_object_or_404(ImageHub,pk=self.kwargs.get('pk'))
        except ObjectDoesNotExist:
            return obj
        obj.number_of_views +=1
        obj.save()
        return obj

class ImageRedirectView(RedirectView):
    pattern_name        = 'image_hub_app:image-details'
    permanent           = False
    query_string        = True

    def get_redirect_url(self, *args, **kwargs):
        image = get_object_or_404(ImageHub, pk=kwargs['pk'])
        print("Get redirect has been called",image)
        image.number_of_downloads+= 1
        image.save()
        
        return super().get_redirect_url(*args, **kwargs)


        