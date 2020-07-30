from django import forms
from image_hub_app.models import Category,ImageHub
import logging
logger = logging.getLogger('django')
class ImageCategoryCreateForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'category_name': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'cols': 1, 'rows': 3}),
            # 'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

        
class ImageCreateForm(forms.ModelForm):
    
    class Meta:
        model = ImageHub
        fields = ['image','title','number_of_people','description','category']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'cols': 1, 'rows': 3}),
            # 'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
    def __init__(self, *args, **kwargs):
        super(ImageCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            logger.info(field)
        # self.fields['image'].widget.attrs['class'] = ['form-file-input','form-control']
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['number_of_people'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['category'].widget.attrs['class'] = 'form-control'