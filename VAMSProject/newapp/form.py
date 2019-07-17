from django import forms
from newapp.models import Employee12

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee12
        fields = "__all__"
