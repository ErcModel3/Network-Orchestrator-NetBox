I needed somewhere to build a custom netbox image outside of my docker-compose file in my main [Network Orchestrator Platform repo](https://github.com/ErcModel3/Network-Orchestrator-Platform).

This repo just pulls from NetBox, allows me to add my plugins (NetBox branching and Custom Objects) and bulid an image, while de-coupling versions of each of them here.

The repo tracks the upstream netbox docker image, starting at 4.1.3 with additional releases appended with -r1/2/3...  and additional changes that I add with plugins.

Citations:
* [NetBox Docs](https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins)
* [NetBox Docker](https://hub.docker.com/r/netboxcommunity/netbox/tags)
* [NetBox Branching](https://github.com/netboxlabs/netbox-branching)
    * [NetBox Docker Branching](https://github.com/netboxlabs/netbox-branching/blob/main/docs/netbox-docker.md)
* [NetBox Custom Objects](https://github.com/netboxlabs/netbox-custom-objects)