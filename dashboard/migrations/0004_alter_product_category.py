# Generated by Django 5.0.2 on 2024-03-07 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_delete_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Equipment', 'Equipment'), ('Materials', 'Materials'), ('Apparatus', 'Apparatus'), ('Visual Aids', 'Visual Aids')], max_length=20),
        ),
    ]