# Generated by Django 2.0 on 2018-01-10 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0026_auto_20180110_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='create_host_model',
            name='select_compute',
            field=models.CharField(choices=[('compute1', 'compute1'), ('compute2', 'compute2'), ('compute3', 'compute3'), ('compute4', 'compute4'), ('compute5', 'compute5'), ('testpc', 'testpc'), ('we', 'we'), ('qwerr', 'qwerr'), ('poiuy', 'poiuy'), ('hjt', 'hjt'), ('vgt', 'vgt')], default=None, max_length=10),
        ),
    ]