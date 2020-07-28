from django.forms import ModelForm
from .models import Company

class CreateCompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = [
                'memberName', 
                'description', 
                'contacts', 
                'address', 
                'idOfActivity',
                'idOFLocation',
                'workingShedule',
                ]
