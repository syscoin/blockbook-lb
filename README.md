# blockbook-lb
network of privately deployed Blockbooks

## Build
To build the blockbook charm, clone the project and build the charm using charmcraft.
```bash

# make sure build-charm is executable
chmod +x scripts/build-charm.sh

make build
```
This should produce a charm file, `blockbook-lb.charm`.


## Deploy
Use juju to deploy the charm and relate it to the desired infrastructure in the model.
```bash
juju deploy ./blockbook-lb.charm
```