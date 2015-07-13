# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "centos65-x86_64"

  config.vm.define "ansible", primary: true do |ansible|
    ansible.vm.network "private_network", ip: "192.168.33.10"
    ansible.vm.hostname = "ansible"
  end

  config.vm.define "host1" do |host1|
    host1.vm.network "private_network", ip: "192.168.33.11"
    host1.vm.hostname = "host1"
  end

  config.vm.define "host2" do |host2|
    host2.vm.network "private_network", ip: "192.168.33.12"
    host2.vm.hostname = "host2"
  end

  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--memory", "256"]
  end
end
