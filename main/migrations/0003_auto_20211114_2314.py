# Generated by Django 3.2.9 on 2021-11-14 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20211114_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catergory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catergory', models.CharField(choices=[('Mens', 'Men'), ('Woman', 'Woman'), ('Kids', 'Kids')], default='Mens', max_length=6)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='catergory',
            field=models.ForeignKey(default='Mens', on_delete=django.db.models.deletion.CASCADE, to='main.catergory'),
        ),
    ]
