# Generated by Django 4.2 on 2023-05-05 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_delete_homeinfo_delete_mainimg_homereference_img_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Product name')),
                ('price', models.PositiveIntegerField(verbose_name='Product price')),
                ('img', models.ImageField(upload_to='Photo', verbose_name='Image')),
            ],
        ),
    ]
