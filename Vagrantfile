# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure('2') do |config|
  config.vm.box = 'ubuntu/focal64'

    config.vm.hostname = 'valheim'

    config.vm.provider :virtualbox do | vb |
      vb.memory = 2048
      vb.cpus = 2
      vb.gui = false
      vb.linked_clone = true
      vb.customize ['modifyvm', :id, '--vram', '8']
      vb.customize ['modifyvm', :id, '--audio', 'none']
    end

    config.vm.provision 'ansible' do | ansible |
      ansible.playbook = 'main.yaml'
      ansible.verbose = 'v'
      # ansible.galaxy_role_file = 'roles/requirements.yaml'
      ansible.host_key_checking = false
      ansible.host_vars = {
        "default" => {
          "steamcmd_agree_to_license" => true
        }
      }
    end

end
