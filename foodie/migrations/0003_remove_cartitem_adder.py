# Generated by Django 4.0.2 on 2022-03-02 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0002_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='adder',
        ),
    ]
