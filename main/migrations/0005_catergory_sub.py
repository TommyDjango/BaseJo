# Generated by Django 3.2.9 on 2021-11-15 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211115_0034'),
    ]

    operations = [
        migrations.AddField(
            model_name='catergory',
            name='sub',
            field=models.CharField(default='', max_length=20),
        ),
    ]
