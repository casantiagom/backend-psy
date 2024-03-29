# Generated by Django 4.1.4 on 2022-12-15 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_alter_answer_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='RankingName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='New RankingName', max_length=255, verbose_name='Ranking Title')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('person', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.person')),
            ],
            options={
                'verbose_name': 'RankingName',
                'verbose_name_plural': 'RankingNames',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=255, verbose_name='Choice')),
                ('rankingName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice', to='api.rankingname')),
            ],
            options={
                'verbose_name': 'Choice',
                'verbose_name_plural': 'Choices',
                'ordering': ['id'],
            },
        ),
    ]
