PLUGINS = [
    'netbox_custom_objects',
    'netbox_branching' # must always come last
]

PLUGINS_CONFIG = {
    'netbox_branching': {
        'exempt_models': [
            'netbox_custom_objects.customobjecttype',
            'netbox_custom_objects.customobjecttypefield',
        ],
    },
}
