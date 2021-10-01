# Generated by Django 3.2 on 2021-10-01 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='type')),
                ('brand', models.CharField(max_length=50, verbose_name='brand')),
                ('color', models.CharField(max_length=50, verbose_name='color')),
                ('size', models.CharField(choices=[('PP', 'PP'), ('P', 'P'), ('M', 'M'), ('G', 'G'), ('GG', 'GG')], max_length=3, verbose_name='size')),
                ('description', models.CharField(max_length=100, verbose_name='description')),
                ('price', models.DecimalField(decimal_places=2, default=1.99, max_digits=5, verbose_name='price')),
                ('image', models.ImageField(upload_to='loja/', verbose_name='image')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
