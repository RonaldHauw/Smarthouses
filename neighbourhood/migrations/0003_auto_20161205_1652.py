# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-05 15:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0002_auto_20161121_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fridges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ref_id', models.CharField(max_length=100)),
                ('power', models.CharField(default=0, max_length=100)),
                ('status', models.CharField(default=0, max_length=100)),
                ('planned_status', models.CharField(default=0, max_length=100)),
                ('optimal_status', models.CharField(default=0, max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Heating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ref_id', models.CharField(max_length=100)),
                ('power', models.CharField(default=0, max_length=100)),
                ('status', models.CharField(default=0, max_length=100)),
                ('planned_status', models.CharField(default=0, max_length=100)),
                ('optimal_status', models.CharField(default=0, max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Optimal_Status_Fridges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.CharField(default=0, max_length=100)),
                ('status', models.CharField(default=0, max_length=100)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.Fridges')),
            ],
        ),
        migrations.CreateModel(
            name='Optimal_Status_Heating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.CharField(default=0, max_length=100)),
                ('status', models.CharField(default=0, max_length=100)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.Fridges')),
            ],
        ),
        migrations.CreateModel(
            name='Optimal_Status_Smart_Devices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.CharField(default=0, max_length=100)),
                ('status', models.CharField(default=0, max_length=100)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.Fridges')),
            ],
        ),
        migrations.CreateModel(
            name='Plan_Status_Battery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.CharField(default=0, max_length=100)),
                ('status', models.CharField(default=0, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Plan_Status_Fridges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.CharField(default=0, max_length=100)),
                ('status', models.CharField(default=0, max_length=100)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.Fridges')),
            ],
        ),
        migrations.CreateModel(
            name='Plan_Status_Heating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.CharField(default=0, max_length=100)),
                ('status', models.CharField(default=0, max_length=100)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.Heating')),
            ],
        ),
        migrations.CreateModel(
            name='Plan_Status_Stupid_devices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.CharField(default=0, max_length=100)),
                ('status', models.CharField(default=0, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Stupid_Devices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ref_id', models.CharField(max_length=100)),
                ('power', models.CharField(default=0, max_length=100)),
                ('status', models.CharField(default=0, max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='boiler',
            name='smart_devices_ptr',
        ),
        migrations.RemoveField(
            model_name='dishwasher',
            name='smart_devices_ptr',
        ),
        migrations.RemoveField(
            model_name='dryer',
            name='smart_devices_ptr',
        ),
        migrations.RemoveField(
            model_name='electric_car',
            name='smart_devices_ptr',
        ),
        migrations.RemoveField(
            model_name='energy_efficient_devices',
            name='room',
        ),
        migrations.RemoveField(
            model_name='energy_non_efficient_devices',
            name='room',
        ),
        migrations.RemoveField(
            model_name='energy_sources',
            name='neighbourhood',
        ),
        migrations.RemoveField(
            model_name='energy_sources',
            name='room_energy_sources',
        ),
        migrations.RemoveField(
            model_name='fridge',
            name='smart_devices_ptr',
        ),
        migrations.RemoveField(
            model_name='oven',
            name='energy_non_efficient_devices_ptr',
        ),
        migrations.RemoveField(
            model_name='sensors',
            name='room',
        ),
        migrations.RemoveField(
            model_name='solar_boiler',
            name='smart_devices_ptr',
        ),
        migrations.RemoveField(
            model_name='solar_pannels',
            name='energy_sources_ptr',
        ),
        migrations.DeleteModel(
            name='Total_Power',
        ),
        migrations.RemoveField(
            model_name='washing_machine',
            name='smart_devices_ptr',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='neighbourhood',
        ),
        migrations.RemoveField(
            model_name='wind_turbine',
            name='energy_sources_ptr',
        ),
        migrations.RenameField(
            model_name='battery',
            old_name='available_power_battery',
            new_name='charged_status',
        ),
        migrations.RenameField(
            model_name='battery',
            old_name='used_power_battery',
            new_name='optimal_status',
        ),
        migrations.AddField(
            model_name='battery',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='battery',
            name='planned_status',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='battery',
            name='power',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='battery',
            name='ref_id',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='battery',
            name='status',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='house',
            name='ref_id',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='ref_id',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='ref_id',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='smart_devices',
            name='house',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.House'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='smart_devices',
            name='optimal_status',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='smart_devices',
            name='ref_id',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='smart_devices',
            name='status',
            field=models.CharField(default=0, max_length=3),
        ),
        migrations.AddField(
            model_name='smart_devices',
            name='status_function',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.DeleteModel(
            name='Boiler',
        ),
        migrations.DeleteModel(
            name='Dishwasher',
        ),
        migrations.DeleteModel(
            name='Dryer',
        ),
        migrations.DeleteModel(
            name='Electric_Car',
        ),
        migrations.DeleteModel(
            name='Energy_Efficient_Devices',
        ),
        migrations.DeleteModel(
            name='Energy_Non_Efficient_Devices',
        ),
        migrations.DeleteModel(
            name='Energy_Sources',
        ),
        migrations.DeleteModel(
            name='Fridge',
        ),
        migrations.DeleteModel(
            name='oven',
        ),
        migrations.DeleteModel(
            name='Sensors',
        ),
        migrations.DeleteModel(
            name='Solar_BoIler',
        ),
        migrations.DeleteModel(
            name='Solar_Pannels',
        ),
        migrations.DeleteModel(
            name='Washing_Machine',
        ),
        migrations.DeleteModel(
            name='Weather',
        ),
        migrations.DeleteModel(
            name='wind_turbine',
        ),
        migrations.AddField(
            model_name='stupid_devices',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.Room'),
        ),
        migrations.AddField(
            model_name='plan_status_stupid_devices',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.Stupid_Devices'),
        ),
        migrations.AddField(
            model_name='plan_status_battery',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.Battery'),
        ),
        migrations.AddField(
            model_name='heating',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.Room'),
        ),
        migrations.AddField(
            model_name='fridges',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.Room'),
        ),
    ]