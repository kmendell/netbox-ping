from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='PluginSettingsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, null=True)),
                ('update_tags', models.BooleanField(default=True, help_text='Whether to update tags when scanning IPs', verbose_name='Update Tags')),
            ],
            options={
                'verbose_name': 'Plugin Settings',
                'verbose_name_plural': 'Plugin Settings',
                'ordering': ['pk'],
            },
        ),
    ] 