# Generated by Django 5.0.6 on 2024-05-27 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0003_produto_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='data_compra',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]