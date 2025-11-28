from netbox.plugins import PluginConfig

class Config(PluginConfig):
    name = 'netbox_ping'
    verbose_name = 'NetBox Ping'
    description = 'Ping IPs and subnets'
    version = '0.50'
    author = 'Christian Rose'
    base_url = 'netbox-ping'
    min_version = '4.0.0'
    default_settings = {
        'exclude_virtual_interfaces': True,
    }

config = Config