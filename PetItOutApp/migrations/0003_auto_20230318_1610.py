# Generated by Django 2.2.26 on 2023-03-18 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PetItOutApp', '0002_auto_20230318_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battle',
            name='petprofileBlue',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='petprofileBlue', to='PetItOutApp.PetProfile'),
        ),
        migrations.AlterField(
            model_name='battle',
            name='petprofileRed',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='petprofileRed', to='PetItOutApp.PetProfile'),
        ),
    ]
