from django.db import migrations
from extras.choices import CustomFieldTypeChoices

def create_dns_name_field(apps, schema_editor):
    CustomField = apps.get_model('extras', 'CustomField')
    ObjectType = apps.get_model('core', 'ObjectType')
    
    # Create Up_Down custom field
    custom_field, created = CustomField.objects.get_or_create(
        name='Up_Down',
        defaults={
            'type': CustomFieldTypeChoices.TYPE_BOOLEAN,
            'label': 'Up/Down Status',
            'description': 'Current up/down status of the IP',
            'required': False,
        }
    )
    
    # Get the ObjectType for IPAddress
    try:
        ipaddress_object_type = ObjectType.objects.get(
            app_label='ipam',
            model='ipaddress'
        )
        
        # Add the ObjectType to the custom field
        if not custom_field.object_types.filter(id=ipaddress_object_type.id).exists():
            custom_field.object_types.add(ipaddress_object_type)
    except ObjectType.DoesNotExist:
        pass  # ObjectType not found, skip

class Migration(migrations.Migration):
    dependencies = [
        ('netbox_ping', '0002_add_dns_fields'),
    ]

    operations = [
        migrations.RunPython(
            create_dns_name_field,
            reverse_code=migrations.RunPython.noop
        ),
    ] 