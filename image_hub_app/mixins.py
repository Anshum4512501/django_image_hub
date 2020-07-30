from django.views.generic import View
from django.shortcuts import render
import json
from django.core.serializers import serialize
from .models import ImageHub
class FindMethodMixin(View):
    template_name   = None
    result          = None
    model           = None
    extra_rows      = None

    
    def get(self,request,*args,**kwargs):
        context = self.get_context_data(**kwargs)    
        context['obj_list'] = self.model.objects.all()[self.result:self.result+self.extra_rows]
        print("result from server",self.result)
        return render(request,self.template_name,context=context) 

    def post(self,request,*args,**kwargs):
        pass


class SerializeMixin(object):
    def serialize(self,request,*args,**kwargs):
        json_data           = json.loads(request.body)
        extra_rows          = int(json_data['result'])
        obj_list            = ImageHub.objects.all()[extra_rows:extra_rows+3]
        qs_json             = serialize('json', obj_list)
        json_data           = json.loads(qs_json)
        json_list           = []
        for item in json_data:
            data = item['fields']
            json_list.append(data)
        json_data = json.dumps(json_list)
        return json_data