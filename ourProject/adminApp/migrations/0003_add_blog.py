# Generated by Django 5.0.1 on 2024-01-10 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0002_alter_admin_panel_admin_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=200)),
                ('blog_article', models.TextField(max_length=20000)),
                ('blog_image', models.ImageField(default='media/blog_pic/dflt_blog_image.jpg', upload_to='media/blog_pic/')),
            ],
        ),
    ]
