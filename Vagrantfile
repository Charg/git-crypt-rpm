$build_script = <<SCRIPT

#sudo yum install -y @development-tools
sudo yum install -y yum-utils rpmdevtools git
rpmdev-setuptree
git clone https://github.com/Charg/git-crypt-rpm ~/rpmbuild/SPECS/

# Download RPM sources
spectool -g -R ~/rpmbuild/SPECS/git-crypt.spec

# Build RPM dependencies
sudo yum-builddep -y ~/rpmbuild/SPECS/git-crypt.spec

# Build RPM
rpmbuild -ba ~/rpmbuild/SPECS/git-crypt.spec

# Install RPM
sudo yum install -y ~/rpmbuild/RPMS/x86_64/git-crypt-0.5.0-1.*.x86_64.rpm

SCRIPT


Vagrant.configure("2") do |config|
  config.vm.provision "shell", inline: $build_script, privileged: false
  config.vm.synced_folder '.', '/vagrant', disabled: true
  config.vm.provider "virtualbox"

  config.vm.define "f21" do |f21|
    f21.vm.box = "chef/fedora-21"
  end

  config.vm.define "f20" do |f20|
    f20.vm.box = "chef/fedora-20"
  end

  config.vm.define "rhel7" do |rhel7|
    rhel7.vm.box = "chef/centos-7.0"
  end

  #config.vm.define "rhel6" do |rhel6|
  #  rhel6.vm.box = "chef/centos-6.6"
  #end

end
