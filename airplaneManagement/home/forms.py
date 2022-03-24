from django import forms
from django.forms import ModelForm


from home.models import AirplaneModel, Airplane, Employee, VariousTests
from home.models import Expertise,MedicalTrafficController,TestRecord
    #

#creating forms
class AirplaneModelForm(ModelForm):
    class Meta:
        model=AirplaneModel
        fields=['model_no','company','manufacturer','capacity','weight']


class AirplaneForm(ModelForm):
    class Meta:
        model=Airplane
        fields=['reg_no','model_no']   
    # def __init__(self, user, *args, **kwargs):
    #     super(AirplaneForm, self).__init__(*args, **kwargs)
    #     self.fields['model_no'].queryset = AirplaneModel.objects.filter(user=user)

class EmployeeForm(ModelForm):
    class Meta:
        model=Employee
        fields=['membership_no','salary','phone_no','address','first_name','last_name','role']   


class VariousTestsForm(ModelForm):
    class Meta:
        model=VariousTests
        fields=['faa_number','test_name']         

    

class ExpertiseForm(ModelForm):
    class Meta:
        model=Expertise
        fields=['expertiseid','model_no','membership_no']   

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['membership_no'].queryset = Employee.objects.filter(role="technician")


    

class MedicalTrafficControllerForm(ModelForm):
    class Meta:
        model=MedicalTrafficController
        fields=['membership_no','medical_examination']       

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['membership_no'].queryset = Employee.objects.filter(role="traffic controller")

class TestRecordForm(ModelForm):
    class Meta:
        model=TestRecord
        fields=['test_id','faa_number','expertiseid','hours','score']               