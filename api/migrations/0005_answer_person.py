# Generated by Django 4.1.1 on 2022-10-12 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_quizzes_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='person',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='api.person'),
        ),
    ]
