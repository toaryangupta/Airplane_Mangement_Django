from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


from home.models import AirplaneModel, Airplane, Employee, VariousTests
from home.models import Expertise, MedicalTrafficController, TestRecord

from .forms import AirplaneModelForm, AirplaneForm, EmployeeForm
from .forms import VariousTestsForm, ExpertiseForm, MedicalTrafficControllerForm, TestRecordForm


# Create your views here.
def homepage(request):
    return render(request=request, template_name="main/homepage.html", context={"title": "Home Page", })


def createAirplaneModelForm(request):
    # form=AirplaneModelForm()
    # return render(request=request, template_name="main/createForm.html", context={"form":form,"title":" "})
    if request.method == "POST":
        form = AirplaneModelForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect(request.path)
    else:
        form = AirplaneModelForm
        return render(request=request, template_name="main/createForm.html", context={"form": form, "title": "Airplane Model Form " ,"formHeading": "Airplane Model Registration",'buttonDetail':"Insert" })


def createAirplaneForm(request):
    if request.method == "POST":
        form = AirplaneForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
          #  print("saved")
            return redirect(request.path)
            # try:
            #     form.save()
            #     return redirect()
            # except:
            #     pass
    else:
        form = AirplaneForm
    return render(request=request, template_name="main/createForm.html", context={"form": form, "title": "Airplane Registraion Form ","formHeading": "Airplane Registraion  ",'buttonDetail':"Insert"})


def createEmployeeForm(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("saved")
            return redirect(request.path)

    else:
        form = EmployeeForm
    return render(request=request, template_name="main/createForm.html", context={"form": form, "title": "Employee Form " ,"formHeading":" Employee Registration ",'buttonDetail':"Insert"})


def createVariousTestsForm(request):
    if request.method == "POST":
        form = VariousTestsForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("saved")
            return redirect(request.path)

    else:
        form = VariousTestsForm
      
    return render(request=request, template_name="main/createForm.html",   context={"form": form, "title": "Various Test Form ", "formHeading": "Test Registration",'buttonDetail':"Insert"})


def createExpertiseForm(request):
    if request.method == "POST":
        form = ExpertiseForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("saved")
            return redirect(request.path)

    else:
        form = ExpertiseForm
    return render(request=request, template_name="main/createForm.html", context={"form": form, "title": " Expertise Linking ","formHeading":" Expertise Linking",'buttonDetail':"Insert"})


def createMedicalTrafficControllerForm(request):
    if request.method == "POST":
        form = MedicalTrafficControllerForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("saved")
            return redirect(request.path)

    else:
        form = MedicalTrafficControllerForm
    return render(request=request, template_name="main/createForm.html", context={"form": form, "title": "Medical Record Form ","formHeading": "Medical Record",'buttonDetail':"Insert"})


def createTestRecordForm(request):
    if request.method == "POST":
        form = TestRecordForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("saved")
            return redirect(request.path)

    else:
        form = TestRecordForm
    return render(request=request, template_name="main/createForm.html", context={"form": form, "title": " Test Record Form ","formHeading":"Test Record Insertion",'buttonDetail':"Insert"})


def displayAirplaneModel(request):
    airplanemodels = AirplaneModel.objects.all()
    my_model_fields = [
        field.name for field in AirplaneModel._meta.get_fields()]
    my_model_fields = my_model_fields[2:]
    capitalisedFields = [field.capitalize() for field in my_model_fields]

    context = {'ourtable': airplanemodels,
               'title': "Display Airplane Models ",
               'caption': "Airplane Models",
               'capitalisedFields': capitalisedFields,

               }
    return render(request, 'main/display/displayAirplaneModel.html', context)


def displayAirplane(request):
    tableData = Airplane.objects.all()
    # User._meta.get_fields()
    my_model_fields = [field.name for field in Airplane._meta.get_fields()]
    my_model_fields = my_model_fields[:]
    capitalisedFields = [field.capitalize() for field in my_model_fields]
    firstField = capitalisedFields[0]

    context = {'ourtable': tableData,
               'title': "Registered Airplanes ",
               'caption': "Registered Airplanes",
               'capitalisedFields': capitalisedFields,

               }
    return render(request, 'main/display/displayAirplane.html', context)


def displayEmployee(request):
    tableData = Employee.objects.all()
    my_model_fields = [field.name for field in Employee._meta.get_fields()]
    my_model_fields = my_model_fields[2:]
    capitalisedFields = [field.capitalize() for field in my_model_fields]

    context = {'ourtable': tableData,
               'title': "Employee Data ",
               'caption': "Employee Data",
               'capitalisedFields': capitalisedFields,

               }
    return render(request, 'main/display/displayEmployee.html', context)


def displayVariousTests(request):
    tableData = VariousTests.objects.all()

    my_model_fields = [field.name for field in VariousTests._meta.get_fields()]
    my_model_fields = my_model_fields[1:]
    capitalisedFields = [field.capitalize() for field in my_model_fields]

    context = {'ourtable': tableData,
               'title': "Test FAA Number ",
               'caption': "Various Tests",
               'capitalisedFields': capitalisedFields,

               }
    return render(request, 'main/display/displayVariousTests.html', context)


def displayExpertise(request):
    tableData = Expertise.objects.all()
    my_model_fields = [field.name for field in Expertise._meta.get_fields()]
    my_model_fields = my_model_fields[1:]
    capitalisedFields = [field.capitalize() for field in my_model_fields]

    context = {'ourtable': tableData,
               'title': "Expertise Data ",
               'caption': "Expertise Data",
               'capitalisedFields': capitalisedFields,

               }
    return render(request, 'main/display/displayExpertise.html', context)


def displayMedicalTrafficController(request):
    tableData = MedicalTrafficController.objects.all()

    my_model_fields = [field.name for field in MedicalTrafficController._meta.get_fields()]
    my_model_fields = my_model_fields[1:]
    capitalisedFields = [field.capitalize() for field in my_model_fields]

    context = {'ourtable': tableData,
               'title': "Medical Record ",
               'caption': "Medical Record",

               'capitalisedFields': capitalisedFields,



               }
    return render(request, 'main/display/displayMedicalTrafficController.html', context)


def displayTestRecord(request):
    tableData = TestRecord.objects.all()
    my_model_fields = [field.name for field in TestRecord._meta.get_fields()]
    my_model_fields = my_model_fields[:]
    capitalisedFields = [field.capitalize() for field in my_model_fields]
    firstField = capitalisedFields[0]

    context = {'ourtable': tableData,
               'title': "Airplane Test Records ",
               'caption': "Airplane Test Records",
               'capitalisedFields': capitalisedFields,
             


               }
    return render(request, 'main/display/displayTestRecord.html', context)

def updateAirplaneModel(request):
    airplanemodels = AirplaneModel.objects.all()
    my_model_fields = [
        field.name for field in AirplaneModel._meta.get_fields()]
    my_model_fields = my_model_fields[2:]
    capitalisedFields = [field.capitalize() for field in my_model_fields]

    context = {'ourtable': airplanemodels,
               'title': "update Airplane Models ",
               'caption': "Airplane Models",
               'capitalisedFields': capitalisedFields,

               }
    return render(request, 'main/update/updateAirplaneModel.html', context)

def do_updateAirplaneModel(request , pk):
    airplaneModelObject=AirplaneModel.objects.get(model_no=pk)
    form = AirplaneModelForm(instance=airplaneModelObject)
    if request.method == "POST":
            form = AirplaneModelForm(request.POST,instance=airplaneModelObject)
            if form.is_valid():
                form.save(commit=True)
                return redirect('/update/AirplaneModel')
   

   
    return render(request=request, template_name="main/createForm.html", context={"form": form, "title": "Airplane Registraion Form ","formHeading": "Airplane Registraion  ",'buttonDetail':"Update"})


def updateAirplane(request):
    tableData = Airplane.objects.all()
    # User._meta.get_fields()
    my_model_fields = [field.name for field in Airplane._meta.get_fields()]
    my_model_fields = my_model_fields[:]
    capitalisedFields = [field.capitalize() for field in my_model_fields]
    firstField = capitalisedFields[0]

    context = {'ourtable': tableData,
               'title': "Registered Airplanes ",
               'caption': "Registered Airplanes",
               'capitalisedFields': capitalisedFields,

               }
    return render(request, 'main/update/updateAirplane.html', context)

def do_updateAirplane(request , pk):
    airplaneObject=Airplane.objects.get(reg_no=pk)
    form = AirplaneForm(instance=airplaneObject)
    if request.method == "POST":
        form = AirplaneForm(request.POST,instance=airplaneObject)
        if form.is_valid():
            form.save(commit=True)
            #  print("saved")
            return redirect('/update/Airplane')
    return render(request=request, template_name="main/createForm.html", context={"form": form, "title": "Airplane Registraion Form ","formHeading": "Airplane Registraion  ",'buttonDetail':"Update"})



def updateEmployee(request):
    tableData = Employee.objects.all()
    my_model_fields = [field.name for field in Employee._meta.get_fields()]
    my_model_fields = my_model_fields[2:]
    capitalisedFields = [field.capitalize() for field in my_model_fields]

    context = {'ourtable': tableData,
               'title': "Employee Data ",
               'caption': "Employee Data",
               'capitalisedFields': capitalisedFields,

               }
    return render(request, 'main/update/updateEmployee.html', context)

def do_updateEmployee(request , pk):
    employeeObject=Employee.objects.get(membership_no=pk)
    form = EmployeeForm(instance=employeeObject)
    if request.method == "POST":
            form = EmployeeForm(request.POST,instance=employeeObject)
            if form.is_valid():
                form.save(commit=True)
                print("saved")
                return redirect('/update/Employee')
   
   
   
    return render(request=request, template_name="main/createForm.html", context={"form": form, "title": "Airplane Registraion Form ","formHeading": "Airplane Registraion  ",'buttonDetail':"Update"})



def updateVariousTests(request):
    tableData = VariousTests.objects.all()

    my_model_fields = [field.name for field in VariousTests._meta.get_fields()]
    my_model_fields = my_model_fields[1:]
    capitalisedFields = [field.capitalize() for field in my_model_fields]

    context = {'ourtable': tableData,
               'title': "Test FAA Number ",
               'caption': "Various Tests",
               'capitalisedFields': capitalisedFields,

               }
    return render(request, 'main/update/updateVariousTests.html', context)

def do_updateVariousTests(request , pk):
    obj=VariousTests.objects.get(faa_number=pk)
    form = VariousTestsForm(instance=obj)
    if request.method == "POST":
        form = VariousTestsForm(request.POST,instance=obj)
        if form.is_valid():
            form.save(commit=True)
            print("saved")
            return redirect('/update/VariousTests')
    
    
    return render(request=request, template_name="main/createForm.html", context={"form": form, "title": "Airplane Registraion Form ","formHeading": "Airplane Registraion  ",'buttonDetail':"Update"})


def updateExpertise(request):
    tableData = Expertise.objects.all()
    my_model_fields = [field.name for field in Expertise._meta.get_fields()]
    my_model_fields = my_model_fields[1:]
    capitalisedFields = [field.capitalize() for field in my_model_fields]

    context = {'ourtable': tableData,
               'title': "Expertise Data ",
               'caption': "Expertise Data",
               'capitalisedFields': capitalisedFields,

               }
    return render(request, 'main/update/updateExpertise.html', context)

def do_updateExpertise(request , pk):
    obj=Expertise.objects.get(expertiseid=pk)
    form = ExpertiseForm(instance=obj)
    if request.method == "POST":
        form = ExpertiseForm(request.POST,instance=obj)
        if form.is_valid():
            form.save(commit=True)
            print("saved")
            return redirect('/update/Expertise')
    
    
    
    return render(request=request, template_name="main/createForm.html", context={"form": form, "title": "Airplane Registraion Form ","formHeading": "Airplane Registraion  ",'buttonDetail':"Update"})


def updateMedicalTrafficController(request):
    tableData = MedicalTrafficController.objects.all()

    my_model_fields = [field.name for field in MedicalTrafficController._meta.get_fields()]
    my_model_fields = my_model_fields[1:]
    capitalisedFields = [field.capitalize() for field in my_model_fields]

    context = {'ourtable': tableData,
               'title': "Medical Record ",
               'caption': "Medical Record",

               'capitalisedFields': capitalisedFields,



               }
    return render(request, 'main/update/updateMedicalTrafficController.html', context)

def do_updateMedicalTrafficController(request , pk):
    obj=MedicalTrafficController.objects.get(id=pk)
    form = MedicalTrafficControllerForm(instance=obj)
    if request.method == "POST":
        form = MedicalTrafficControllerForm(request.POST,instance=obj)
        if form.is_valid():
            form.save(commit=True)
            print("saved")
            return redirect('/update/MedicalTrafficController',views.updateMedicalTrafficController,name="updateMedicalTrafficController")
    
    return render(request=request, template_name="main/createForm.html", context={"form": form, "title": "Airplane Registraion Form ","formHeading": "Airplane Registraion  ",'buttonDetail':"Update"})


def updateTestRecord(request):
    tableData = TestRecord.objects.all()
    my_model_fields = [field.name for field in TestRecord._meta.get_fields()]
    my_model_fields = my_model_fields[:]
    capitalisedFields = [field.capitalize() for field in my_model_fields]
    firstField = capitalisedFields[0]

    context = {'ourtable': tableData,
               'title': "Airplane Test Records ",
               'caption': "Airplane Test Records",
               'capitalisedFields': capitalisedFields,
             


               }
    return render(request, 'main/update/updateTestRecord.html', context)

def do_updateTestRecord(request , pk):
    obj=TestRecord.objects.get(test_id=pk)
    form = TestRecordForm(instance=obj)
    if request.method == "POST":
        form = TestRecordForm(request.POST,instance=obj)
        if form.is_valid():
            form.save(commit=True)
            print("saved")
            return redirect('/update/TestRecord')
    return render(request=request, template_name="main/createForm.html", context={"form": form, "title": "Airplane Registraion Form ","formHeading": "Airplane Registraion  ",'buttonDetail':"Update"})

def deleteAirplaneModel(request):
    airplanemodels = AirplaneModel.objects.all()
    my_model_fields = [
        field.name for field in AirplaneModel._meta.get_fields()]
    my_model_fields = my_model_fields[2:]
    capitalisedFields = [field.capitalize() for field in my_model_fields]

    context = {'ourtable': airplanemodels,
               'title': "delete Airplane Models ",
               'caption': "Airplane Models",
               'capitalisedFields': capitalisedFields,
               

               }
    return render(request, 'main/delete/deleteAirplaneModel.html', context)

def do_deleteAirplaneModel(request , pk):
    airplaneModelObject=AirplaneModel.objects.get(model_no=pk)
    
    if request.method == "POST":
           airplaneModelObject.delete()
           return redirect('/delete/AirplaneModel')
   

   
    return render(request=request, template_name="main/createForm.html", context={"form": form, "title": "Airplane Registraion Form ","formHeading": "Airplane Registraion  "})


def deleteAirplane(request):
    tableData = Airplane.objects.all()
    # User._meta.get_fields()
    my_model_fields = [field.name for field in Airplane._meta.get_fields()]
    my_model_fields = my_model_fields[:]
    capitalisedFields = [field.capitalize() for field in my_model_fields]
    firstField = capitalisedFields[0]

    context = {'ourtable': tableData,
               'title': "Registered Airplanes ",
               'caption': "Registered Airplanes",
               'capitalisedFields': capitalisedFields,

               }
    return render(request, 'main/delete/deleteAirplane.html', context)

def do_deleteAirplane(request , pk):
    airplaneObject=Airplane.objects.get(reg_no=pk)
    if request.method == "POST":
           airplaneObject.delete()
           return redirect('/delete/Airplane')
   
    return render(request=request, template_name="main/createForm.html", context={"form": form, "title": "Airplane Registraion Form ","formHeading": "Airplane Registraion  "})



def deleteEmployee(request):
    tableData = Employee.objects.all()
    my_model_fields = [field.name for field in Employee._meta.get_fields()]
    my_model_fields = my_model_fields[2:]
    capitalisedFields = [field.capitalize() for field in my_model_fields]

    context = {'ourtable': tableData,
               'title': "Employee Data ",
               'caption': "Employee Data",
               'capitalisedFields': capitalisedFields,

               }
    return render(request, 'main/delete/deleteEmployee.html', context)

def do_deleteEmployee(request , pk):
    employeeObject=Employee.objects.get(membership_no=pk)
    if request.method == "POST":
           employeeObject.delete()
           return redirect('/delete/Employee')
   
   
   
    return render(request=request, template_name="main/createForm.html", context={"form": form, "title": "Airplane Registraion Form ","formHeading": "Airplane Registraion  "})



def deleteVariousTests(request):
    tableData = VariousTests.objects.all()

    my_model_fields = [field.name for field in VariousTests._meta.get_fields()]
    my_model_fields = my_model_fields[1:]
    capitalisedFields = [field.capitalize() for field in my_model_fields]

    context = {'ourtable': tableData,
               'title': "Test FAA Number ",
               'caption': "Various Tests",
               'capitalisedFields': capitalisedFields,

               }
    return render(request, 'main/delete/deleteVariousTests.html', context)

def do_deleteVariousTests(request , pk):
    obj=VariousTests.objects.get(faa_number=pk)
    if request.method == "POST":
           obj.delete()
           return redirect('/delete/VariousTests')
    
    
    return render(request=request, template_name="main/createForm.html", context={"form": form, "title": "Airplane Registraion Form ","formHeading": "Airplane Registraion  "})


def deleteExpertise(request):
    tableData = Expertise.objects.all()
    my_model_fields = [field.name for field in Expertise._meta.get_fields()]
    my_model_fields = my_model_fields[1:]
    capitalisedFields = [field.capitalize() for field in my_model_fields]

    context = {'ourtable': tableData,
               'title': "Expertise Data ",
               'caption': "Expertise Data",
               'capitalisedFields': capitalisedFields,

               }
    return render(request, 'main/delete/deleteExpertise.html', context)

def do_deleteExpertise(request , pk):
    obj=Expertise.objects.get(expertiseid=pk)
   
    if request.method == "POST":
           obj.delete()
           return redirect('/delete/Expertise')
    
    
    
    
    return render(request=request, template_name="main/createForm.html", context={"form": form, "title": "Airplane Registraion Form ","formHeading": "Airplane Registraion  "})


def deleteMedicalTrafficController(request):
    tableData = MedicalTrafficController.objects.all()

    my_model_fields = [field.name for field in MedicalTrafficController._meta.get_fields()]
    my_model_fields = my_model_fields[1:]
    capitalisedFields = [field.capitalize() for field in my_model_fields]

    context = {'ourtable': tableData,
               'title': "Medical Record ",
               'caption': "Medical Record",

               'capitalisedFields': capitalisedFields,



               }
    return render(request, 'main/delete/deleteMedicalTrafficController.html', context)

def do_deleteMedicalTrafficController(request , pk):
    obj=MedicalTrafficController.objects.get(id=pk)
    if request.method == "POST":
           obj.delete()
           return redirect('/delete/MedicalTrafficController')
    
    return render(request=request, template_name="main/createForm.html", context={"form": form, "title": "Airplane Registraion Form ","formHeading": "Airplane Registraion  "})


def deleteTestRecord(request):
    tableData = TestRecord.objects.all()
    my_model_fields = [field.name for field in TestRecord._meta.get_fields()]
    my_model_fields = my_model_fields[:]
    capitalisedFields = [field.capitalize() for field in my_model_fields]
    firstField = capitalisedFields[0]

    context = {'ourtable': tableData,
               'title': "Airplane Test Records ",
               'caption': "Airplane Test Records",
               'capitalisedFields': capitalisedFields,
             


               }
    return render(request, 'main/delete/deleteTestRecord.html', context)

def do_deleteTestRecord(request , pk):
    obj=TestRecord.objects.get(test_id=pk)
    if request.method == "POST":
           obj.delete()
           return redirect('/delete/TestRecord')
    return render(request=request, template_name="main/createForm.html", context={"form": form, "title": "Airplane Registraion Form ","formHeading": "Airplane Registraion  "})