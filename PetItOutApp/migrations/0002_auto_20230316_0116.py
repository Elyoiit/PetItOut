# Generated by Django 2.2.26 on 2023-03-16 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PetItOutApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
        migrations.CreateModel(
            name='PetProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.TextField()),
                ('pet_type', models.TextField()),
                ('pet_age', models.TextField()),
                ('pet_description', models.TextField()),
                ('pet_picture', models.ImageField(upload_to='pet_images')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PetItOutApp.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='EditProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_description', models.TextField()),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PetItOutApp.UserProfile')),
            ],
        ),
    ]
