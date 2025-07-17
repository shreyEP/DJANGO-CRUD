from django import forms
from .models import Clients,Departments
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column, Field

class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['name', 'age', 'account_type', 'photo','department']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.enctype = 'multipart/form-data'
        self.helper.form_class = 'needs-validation'  

        self.helper.layout = Layout(
            Row(
                Column(Field('name', wrapper_class='mb-3'), css_class='col-md-3 width:10px'),
                Column(Field('age', wrapper_class='mb-3'), css_class='col-md-6'),
                css_class='row'
            ),
            Row(
                Column(Field('account_type', wrapper_class='mb-3'), css_class='col-md-6'),
                Column(Field('photo', wrapper_class='mb-3'), css_class='col-md-6'),
                css_class='row'
            ),
            Submit('submit', 'Submit', css_class='btn btn-primary w-100 mt-3')
        )

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Departments
        fields = ['department_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.enctype = 'multipart/form-data'
        self.helper.form_class = 'needs-validation' 
        self.helper.layout = Layout(
            Row(
                Column(Field('department_name', wrapper_class='mb-3'), css_class='col-md-6'), 
                css_class='row'
            ),
            Submit('submit', 'Submit', css_class='btn btn-primary w-100 mt-3')
        )  
