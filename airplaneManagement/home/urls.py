from django.urls import path,include
from home import views



urlpatterns = [
    
    path("", views.homepage, name="homepage"),
    path("create/AirplaneModelForm",views.createAirplaneModelForm,name="createAirplaneModelForm"),
    path("create/AirplaneForm",views.createAirplaneForm,name="createAirplaneForm"),
    path("create/EmployeeForm",views.createEmployeeForm,name="createEmployeeForm"),
    path("create/VariousTestsForm",views.createVariousTestsForm,name="createVariousTestsForm"),
    path("create/ExpertiseForm",views.createExpertiseForm,name="createExpertiseForm"),
    path("create/MedicalTrafficControllerForm",views.createMedicalTrafficControllerForm,name="createMedicalTrafficControllerForm"),
    path("create/TestRecordForm",views.createTestRecordForm,name="createTestRecordForm"),

    path("display/AirplaneModel",views.displayAirplaneModel,name="displayAirplaneModel"),
    path("display/Airplane",views.displayAirplane,name="displayAirplane"),
    path("display/Employee",views.displayEmployee,name="displayEmployee"),
    path("display/VariousTests",views.displayVariousTests,name="displayVariousTests"),
    path("display/Expertise",views.displayExpertise,name="displayExpertise"),
    path("display/MedicalTrafficController",views.displayMedicalTrafficController,name="displayMedicalTrafficController"),
    path("display/TestRecord",views.displayTestRecord,name="displayTestRecord"),


    path("update/AirplaneModel",views.updateAirplaneModel,name="updateAirplaneModel"),
    path("update/Airplane",views.updateAirplane,name="updateAirplane"),
    path("update/Employee",views.updateEmployee,name="updateEmployee"),
    path("update/VariousTests",views.updateVariousTests,name="updateVariousTests"),
    path("update/Expertise",views.updateExpertise,name="updateExpertise"),
    path("update/MedicalTrafficController",views.updateMedicalTrafficController,name="updateMedicalTrafficController"),
    path("update/TestRecord",views.updateTestRecord,name="updateTestRecord"),
   
    path("update/AirplaneModel/<str:pk>",views.do_updateAirplaneModel,name="do_updateAirplaneModel"),
    path('update/Airplane/<str:pk>',views.do_updateAirplane,name="do_updateAirplane"),
    path("update/Employee/<str:pk>",views.do_updateEmployee,name="do_updateEmployee"),
    path("update/VariousTests/<str:pk>",views.do_updateVariousTests,name="do_updateVariousTests"),
    path("update/Expertise/<str:pk>",views.do_updateExpertise,name="do_updateExpertise"),
    path("update/MedicalTrafficController/<str:pk>",views.do_updateMedicalTrafficController,name="do_updateMedicalTrafficController"),
    path("update/TestRecord/<str:pk>",views.do_updateTestRecord,name="do_updateTestRecord"),



    path("delete/AirplaneModel",views.deleteAirplaneModel,name="deleteAirplaneModel"),
    path("delete/Airplane",views.deleteAirplane,name="deleteAirplane"),
    path("delete/Employee",views.deleteEmployee,name="deleteEmployee"),
    path("delete/VariousTests",views.deleteVariousTests,name="deleteVariousTests"),
    path("delete/Expertise",views.deleteExpertise,name="deleteExpertise"),
    path("delete/MedicalTrafficController",views.deleteMedicalTrafficController,name="deleteMedicalTrafficController"),
    path("delete/TestRecord",views.deleteTestRecord,name="deleteTestRecord"),

    path("delete/AirplaneModel/<str:pk>",views.do_deleteAirplaneModel,name="do_deleteAirplaneModel"),
    path('delete/Airplane/<str:pk>',views.do_deleteAirplane,name="do_deleteAirplane"),
    path("delete/Employee/<str:pk>",views.do_deleteEmployee,name="do_deleteEmployee"),
    path("delete/VariousTests/<str:pk>",views.do_deleteVariousTests,name="do_deleteVariousTests"),
    path("delete/Expertise/<str:pk>",views.do_deleteExpertise,name="do_deleteExpertise"),
    path("delete/MedicalTrafficController/<str:pk>",views.do_deleteMedicalTrafficController,name="do_deleteMedicalTrafficController"),
    path("delete/TestRecord/<str:pk>",views.do_deleteTestRecord,name="do_deleteTestRecord"),





]
