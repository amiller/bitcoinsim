from fabric.api import env, local, run
from fabric.api import run, cd, sudo, put, get, env, settings
from fabric.contrib.files import append
 
def vagrant():
    # change from the default user to 'vagrant'
    env.user = 'vagrant'
    # connect to the port-forwarded ssh
    env.hosts = ['127.0.0.1:2222']
 
    # use vagrant ssh key
    result = local('vagrant ssh-config | grep IdentityFile', capture=True)
    env.key_filename = result.split()[1][1:-1] # strip ""
    print 'key: [%s]' % env.key_filename

def setup():
    # Builds/installs bitcoin
    sudo('apt-get update')
    sudo('apt-get install -y build-essential git libdb++-dev libboost-all-dev libminiupnpc-dev')
    sudo('apt-get install -y automake emacs24-nox libssl-dev pkg-config')
    run('mkdir -p installing')
    with cd('installing'):
        run('git pull origin master')
        run('if ! [ -a configure.sh ]; then ./autogen.sh; fi')
        run('./configure --with-incompatible-bdb --enable-tests=no')
        run('make')

    run('echo "rpcuser=nothing\nrpcpassword=0932jf0j9sdjf" > ~/.bitcoin/bitcoin.conf')
    run('mkdir -p ~/bin')
    run('if ! [ -a ~/bin/bitcoind ]; then ln -s $HOME/installing/src/bitcoind $HOME/bin/bitcoind')

def start():
    run('bitcoind -daemon -debug')

def getinfo():
    run('bitcoind getinfo')

def uname():
    run('uname -a')
