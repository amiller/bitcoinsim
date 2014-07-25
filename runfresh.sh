#!/bin/bash -x

# Generate a new bitcoindir
DATADIR=${PWD}/data/bitdir-$(date +%F-%T)

cp -r data/dotbitcoin_template_260k $DATADIR
chmod -R +w $DATADIR

bitcoind -datadir=$DATADIR $@
