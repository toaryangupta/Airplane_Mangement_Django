from django.db import models
from django.forms import ModelForm

# Create your models here.

class AirplaneModel(models.Model):
    model_no = models.CharField(primary_key=True, max_length=20)
    company = models.CharField(max_length=30)
    manufacturer = models.CharField(db_column='Manufacturer', max_length=25, blank=True, null=True)  # Field name made lowercase.
    capacity = models.IntegerField()
    weight = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'model'

    def __str__(self):
        return (self.model_no+" ( "+self.company+" "+str(self.capacity)+" "+(self.manufacturer)+" )")
    


class Airplane(models.Model):
    reg_no = models.CharField(primary_key=True, max_length=15)
    model_no = models.ForeignKey('AirplaneModel', models.DO_NOTHING, db_column='model_no')

    class Meta:
        managed = True
        db_table = 'airplane'

class Employee(models.Model):
    membership_no = models.CharField(db_column='Membership_no', primary_key=True, max_length=10)  # Field name made lowercase.
    salary = models.IntegerField(db_column='Salary')  # Field name made lowercase.
    phone_no = models.IntegerField(db_column='Phone_no', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=30, blank=True, null=True)  # Field name made lowercase.
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'employee'

    def __str__(self):
        return (str(self.membership_no)+" ( "+self.first_name+" "+self.last_name+"_"+self.role+" )")
    


class VariousTests(models.Model):
    faa_number = models.CharField(db_column='FAA_Number', primary_key=True, max_length=10)  # Field name made lowercase.
    test_name = models.CharField(db_column='TEST_NAME', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'various_tests'

    def __str__(self):
        return (self.faa_number+" : "+self.test_name)
    

class Expertise(models.Model):
    expertiseid = models.CharField(db_column='expertiseId', primary_key=True, max_length=15)  # Field name made lowercase.
    model_no = models.ForeignKey(AirplaneModel, models.DO_NOTHING, db_column='model_no', blank=True, null=True)
    membership_no = models.ForeignKey(Employee, models.DO_NOTHING, db_column='Membership_no', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'expertise'

    def __str__(self):
        return (str(self.expertiseid)+" { "+str(self.model_no)+" "+str(self.membership_no)+" }")
    


class MedicalTrafficController(models.Model):
    membership_no = models.ForeignKey(Employee, models.DO_NOTHING, db_column='Membership_no')  # Field name made lowercase.
    medical_examination = models.DateField()

    class Meta:
        managed = True
        db_table = 'medical_traffic_controller'


class TestRecord(models.Model):
    test_id = models.CharField(primary_key=True, max_length=15)
    faa_number = models.ForeignKey('VariousTests', models.DO_NOTHING, db_column='FAA_Number')  # Field name made lowercase.
    expertiseid = models.ForeignKey(Expertise, models.DO_NOTHING, db_column='expertiseId')  # Field name made lowercase.
    hours = models.IntegerField()
    score = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'test_record'

