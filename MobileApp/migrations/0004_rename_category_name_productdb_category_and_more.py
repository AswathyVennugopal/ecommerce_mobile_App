# Generated by Django 4.2.7 on 2024-01-16 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MobileApp', '0003_rename_category_productdb_category_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productdb',
            old_name='Category_Name',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='productdb',
            old_name='Price',
            new_name='Deal_Price',
        ),
        migrations.RenameField(
            model_name='productdb',
            old_name='Product_Name',
            new_name='Delivery_Status',
        ),
        migrations.RemoveField(
            model_name='categorydb',
            name='Phone_Image',
        ),
        migrations.RemoveField(
            model_name='productdb',
            name='Description',
        ),
        migrations.RemoveField(
            model_name='productdb',
            name='Product_Image1',
        ),
        migrations.RemoveField(
            model_name='productdb',
            name='Product_Image2',
        ),
        migrations.RemoveField(
            model_name='productdb',
            name='Product_Image3',
        ),
        migrations.AddField(
            model_name='categorydb',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='Category Images'),
        ),
        migrations.AddField(
            model_name='productdb',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='Product Images'),
        ),
        migrations.AddField(
            model_name='productdb',
            name='MRP_Price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productdb',
            name='Name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='productdb',
            name='Rating',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='productdb',
            name='Specification',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='categorydb',
            name='Description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]