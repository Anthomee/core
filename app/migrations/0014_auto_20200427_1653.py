# Generated by Django 3.0.3 on 2020-04-27 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20200427_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='proficiency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.SkillProficiency'),
        ),
    ]