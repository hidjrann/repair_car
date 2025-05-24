from django import forms
from .models import Repair
from .models import FixRequest


class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(RepairForm, self).__init__(*args, **kwargs)

        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'



class FixRequestForm(forms.ModelForm):
    class Meta:
        model = FixRequest
        fields = ['full_name', 'phone', 'email', 'car_model', 'issue_description']
        widgets = {
            'issue_description': forms.Textarea(attrs={'rows': 4}),
        }