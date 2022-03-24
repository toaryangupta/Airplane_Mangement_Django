from django.contrib import admin


from home.models import AirplaneModel, Airplane, Employee, VariousTests
from home.models import Expertise,MedicalTrafficController,TestRecord

# Register your models here.
admin.site.register(AirplaneModel)
admin.site.register(Airplane)
admin.site.register(Employee)
admin.site.register(VariousTests)
admin.site.register(Expertise)
admin.site.register(MedicalTrafficController)
admin.site.register(TestRecord)