# Direct copies of both the config files from the github pages

from netbox_branching.utilities import DynamicSchemaDict

DATABASE_ROUTERS = [
    'netbox_branching.database.BranchAwareRouter',
]
