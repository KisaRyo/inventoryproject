# Generated by Django 5.0.2 on 2024-03-02 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='subject',
            field=models.CharField(choices=[('Elementary', 'Elementary'), ('Junior HS', 'Junior HS'), ('Senior HS', 'Senior HS')], default='Science Teacher', max_length=20),
        ),
    ]