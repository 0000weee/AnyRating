# Generated by Django 4.2.11 on 2024-05-28 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anyrating', '0012_alter_comment_category_alter_comment_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='category',
            field=models.CharField(choices=[('Movie', 'Movie'), ('Restaurant', 'Restaurant'), ('Book', 'Book')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
