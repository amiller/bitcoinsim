A simulated Bitcoin network in a box
--

Requirements:
    virtualbox
    vagrant
    fabric (python-fabric)

Use the following code to add a vagrant box:

    vagrant box add precise32 http://files.vagrantup.com/precise32.box

Follow the steps here to set up the virtual machine:

    http://code.tutsplus.com/tutorials/vagrant-what-why-and-how--net-26500

Use fabric to setup the environment

    fab vagrant setup_apt
    fab vagrant setup_shadow
    fab vagrant setup_plugin_deps    
    fab vagrant setup
    fab vagrant setup_plugin
    fab vagrant run_plugin
