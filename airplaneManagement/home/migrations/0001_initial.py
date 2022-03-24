# Generated by Django 2.2.10 on 2021-04-21 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirplaneModel',
            fields=[
                ('model_no', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=30)),
                ('manufacturer', models.CharField(blank=True, db_column='Manufacturer', max_length=25, null=True)),
                ('capacity', models.IntegerField()),
                ('weight', models.IntegerField()),
            ],
            options={
                'db_table': 'model',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('membership_no', models.CharField(db_column='Membership_no', max_length=10, primary_key=True, serialize=False)),
                ('salary', models.IntegerField(db_column='Salary')),
                ('phone_no', models.IntegerField(blank=True, db_column='Phone_no', null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=30, null=True)),
                ('first_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('role', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'employee',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('expertiseid', models.CharField(db_column='expertiseId', max_length=15, primary_key=True, serialize=False)),
                ('membership_no', models.ForeignKey(blank=True, db_column='Membership_no', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Employee')),
                ('model_no', models.ForeignKey(blank=True, db_column='model_no', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.AirplaneModel')),
            ],
            options={
                'db_table': 'expertise',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='VariousTests',
            fields=[
                ('faa_number', models.CharField(db_column='FAA_Number', max_length=10, primary_key=True, serialize=False)),
                ('test_name', models.CharField(db_column='TEST_NAME', max_length=45)),
            ],
            options={
                'db_table': 'various_tests',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TestRecord',
            fields=[
                ('test_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('hours', models.IntegerField()),
                ('score', models.IntegerField()),
                ('expertiseid', models.ForeignKey(db_column='expertiseId', on_delete=django.db.models.deletion.DO_NOTHING, to='home.Expertise')),
                ('faa_number', models.ForeignKey(db_column='FAA_Number', on_delete=django.db.models.deletion.DO_NOTHING, to='home.VariousTests')),
            ],
            options={
                'db_table': 'test_record',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MedicalTrafficController',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medical_examination', models.DateField()),
                ('membership_no', models.ForeignKey(db_column='Membership_no', on_delete=django.db.models.deletion.DO_NOTHING, to='home.Employee')),
            ],
            options={
                'db_table': 'medical_traffic_controller',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('reg_no', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('model_no', models.ForeignKey(db_column='model_no', on_delete=django.db.models.deletion.DO_NOTHING, to='home.AirplaneModel')),
            ],
            options={
                'db_table': 'airplane',
                'managed': True,
            },
        ),
    ]
