# Generated by Django 5.0.3 on 2024-08-31 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fertilizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fertilizer_name', models.CharField(max_length=255)),
                ('nitrogen', models.DecimalField(decimal_places=2, max_digits=10)),
                ('phosphorus', models.DecimalField(decimal_places=2, max_digits=10)),
                ('potassium', models.DecimalField(decimal_places=2, max_digits=10)),
                ('poster', models.ImageField(upload_to='')),
            ],
        ),
    ]
