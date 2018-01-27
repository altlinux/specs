
%define oneadmin_home /var/lib/one

%add_findreq_skiplist /var/lib/one/*

%add_ruby_lib_path /usr/lib/one/ruby/cli
%add_ruby_lib_path /usr/lib/one/ruby/vendors/rbvmomi/lib
%add_ruby_lib_path /usr/lib/one/ruby/vcenter_driver
%add_ruby_lib_path /usr/lib/one/ruby/cloud/econe
%add_ruby_lib_path /usr/lib/one/ruby/cloud
%add_ruby_lib_path /usr/lib/one/ruby/onedb
%add_ruby_lib_path /usr/lib/one/ruby
%add_ruby_lib_path /usr/lib/one/mads
%add_ruby_lib_path /usr/lib/one/oneflow/lib
%add_ruby_lib_path /usr/lib/one/sunstone/models

%filter_from_requires /^ruby(win32\/sspi)/d
%filter_from_requires /^ruby(zurb-foundation)/d
%filter_from_requires /^ruby(xmlparser)/d

Name: opennebula
Summary: Cloud computing solution for Data Center Virtualization
Version: 5.4.6
Release: alt1%ubt
License: Apache
Group: System/Servers
Url: https://opennebula.org

Source0: %name-%version.tar

################################################################################
# Build Requires
################################################################################

BuildRequires(pre): rpm-build-ubt rpm-build-ruby
BuildRequires: gcc-c++
BuildRequires: libcurl-devel
BuildRequires: libxml2-devel libxmlrpc-devel liblzma-devel
BuildRequires: libssl-devel
BuildRequires: libmysqlclient-devel
BuildRequires: libsqlite3-devel
BuildRequires: openssh
BuildRequires: ruby
BuildRequires: scons
BuildRequires: java-1.8.0-openjdk-devel rpm-build-java ws-commons-util xmlrpc-common xmlrpc-client
BuildRequires: zlib-devel
BuildRequires: npm

################################################################################
# Main Package
################################################################################

%description
OpenNebula.org is an open-source project aimed at building the industry
standard open source cloud computing tool to manage the complexity and
heterogeneity of distributed data center infrastructures.

The OpenNebula.org Project is maintained and driven by the community. The
OpenNebula.org community has thousands of users, contributors, and supporters,
who interact through various online email lists, blogs and innovative projects
to support each other.

OpenNebula is free software released under the Apache License.


################################################################################
# Package opennebula-tools
################################################################################

%package tools
Summary: Cloud computing solution for Data Center Virtualization
Group: Emulators
BuildArch: noarch
Provides: ruby-%name-cli = %EVR
#fix provides
Provides: ruby(cli/cli_helper)
Provides: ruby(cli/command_parser)

Requires: openssl
Requires: openssh
Requires: sqlite3
Requires: openssh-clients

Requires: %name-common = %EVR
Requires: %name-ruby = %EVR

%description tools
OpenNebula.org is an open-source project aimed at building the industry
standard open source cloud computing tool to manage the complexity and
heterogeneity of distributed data center infrastructures.

The OpenNebula.org Project is maintained and driven by the community. The
OpenNebula.org community has thousands of users, contributors, and supporters,
who interact through various online email lists, blogs and innovative projects
to support each other.

OpenNebula is free software released under the Apache License.

This package provides the CLI interface.

################################################################################
# Package opennebula-server
################################################################################

%package server
Summary: Provides the OpenNebula servers
Group: System/Servers
Requires: %name-tools = %EVR
Requires: openssh-server
Requires: genisoimage
Requires: qemu-img
Requires: xmlrpc-c
Requires: nfs-utils
Requires: wget
Requires: curl
Requires: iputils
Obsoletes: %name-ozones
#TODO: Requires http://rubygems.org/gems/net-ldap

%description server
This package provides the OpenNebula servers: oned (main daemon) and mm_sched
(scheduler).

################################################################################
# Package common
################################################################################

%package common
Summary: Provides the OpenNebula user
Group: System/Servers
BuildArch: noarch

%description common
This package creates the oneadmin user and group.

################################################################################
# Package ruby
################################################################################

%package ruby
Summary: Provides the OpenNebula Ruby libraries
Group: Development/Ruby
BuildArch: noarch
Provides: ruby-%name = %EVR
#fix provides
Provides: ruby(cloud/CloudClient)

#Requires: ruby
#Requires: rubygems
#Requires: rubygem-sqlite3-ruby
#Requires: rubygem-json
#Requires: rubygem-rack
#Requires: rubygem-sinatra
#Requires: rubygem-thin
#Requires: rubygem-uuidtools
#Requires: rubygem-nokogiri
#Requires: rubygem-sequel
#Requires: ruby-mysql

# curb       => For EC2 and OCCI uploads (OPTIONAL: falls back to multipart)

# Missing gems
# aws-sdk    => EC2 hybrid driver (EPEL)
# mysql      => Required to handle MySQL DB upgrades (EPEL)
# treetop    => OneFlow (EPEL)

# amazon-ec2 => used for ec2 server (expose OpenNebula with an EC2 interface)
# net-ldap   => Ldap authentication
# parse-cron => OneFlow

%description ruby
Ruby interface for OpenNebula.

################################################################################
# Package sunstone
################################################################################

%package sunstone
Summary: Browser based UI and public cloud interfaces
Group: System/Servers
BuildArch: noarch
#fix provides
Provides: ruby(econe/EC2QueryClient)

Requires: %name-common = %EVR
Requires: %name-ruby = %EVR
Requires: ruby-rack-handler-webrick

%description sunstone
Browser based UI for administrating a OpenNebula cloud. Also includes
the public cloud interface econe-server (AWS cloud
API).

################################################################################
# Package gate
################################################################################

%package gate
Summary: Transfer information from Virtual Machines to OpenNebula
Group: System/Servers
BuildArch: noarch

Requires: %name-common = %EVR
Requires: %name-ruby = %EVR

%description gate
Transfer information from Virtual Machines to OpenNebula

################################################################################
# Package flow
################################################################################

%package flow
Summary: Manage OpenNebula Services
Group: System/Servers
BuildArch: noarch

Requires: %name-common = %EVR
Requires: %name-ruby = %EVR

%description flow
Manage OpenNebula Services

################################################################################
# Package java
################################################################################

%package java
Summary: Java interface to OpenNebula Cloud API
Group: Development/Java
BuildArch: noarch
Requires: ws-commons-util
Requires: xmlrpc-common
Requires: xmlrpc-client

%description java
Java interface to OpenNebula Cloud API.

################################################################################
# Package node-kvm
################################################################################

%package node-kvm
Summary: Configures an OpenNebula node providing kvm
Group: System/Servers
BuildArch: noarch

Conflicts: %name-node-xen
Requires: ruby ruby-stdlibs
Requires: openssh-server
Requires: openssh-clients
Requires: libvirt-kvm
Requires: qemu-kvm
Requires: qemu-img
Requires: nfs-utils
Requires: bridge-utils
Requires: ipset
Requires: pciutils
Requires: %name-common = %EVR

%description node-kvm
Configures an OpenNebula node providing kvm.

################################################################################
# Package node-xen
################################################################################

# %package node-xen
# Summary: Configures an OpenNebula node providing xen
# Group: System/Servers
# BuildArch: noarch
# Conflicts: %name-node-kvm
# Requires: centos-release-xen
# Requires: ruby
# Requires: openssh-server
# Requires: openssh-clients
# Requires: xen
# Requires: nfs-utils
# Requires: bridge-utils
# Requires: %name-common = %version
#
# %description node-xen
# Configures an OpenNebula node providing xen.

################################################################################
# Build and install
################################################################################

%prep
%setup

%build
export PATH="$PATH:$PWD/src/sunstone/public/node_modules/grunt/bin"

pushd src/sunstone/public
npm rebuild
popd

# Compile OpenNebula
scons -j2 mysql=yes new_xmlrpc=yes sunstone=yes

#../build_opennebula.sh
cd src/oca/java
./build.sh -d

%install
export DESTDIR=%buildroot
./install.sh -p

# systemd units
install -p -D -m 644 share/pkgs/ALTLinux/opennebula.service %buildroot%_unitdir/opennebula.service
install -p -D -m 644 share/pkgs/ALTLinux/opennebula-scheduler.service %buildroot%_unitdir/opennebula-scheduler.service
install -p -D -m 644 share/pkgs/ALTLinux/opennebula-sunstone.service %buildroot%_unitdir/opennebula-sunstone.service
install -p -D -m 644 share/pkgs/ALTLinux/opennebula-gate.service  %buildroot%_unitdir/opennebula-gate.service
install -p -D -m 644 share/pkgs/ALTLinux/opennebula-econe.service %buildroot%_unitdir/opennebula-econe.service
install -p -D -m 644 share/pkgs/ALTLinux/opennebula-flow.service  %buildroot%_unitdir/opennebula-flow.service
install -p -D -m 644 share/pkgs/ALTLinux/opennebula-novnc.service %buildroot%_unitdir/opennebula-novnc.service

# Init scripts
install -p -D -m 755 share/pkgs/ALTLinux/opennebula %buildroot%_initdir/opennebula
install -p -D -m 755 share/pkgs/ALTLinux/opennebula-sunstone %buildroot%_initdir/opennebula-sunstone
install -p -D -m 755 share/pkgs/ALTLinux/opennebula-gate  %buildroot%_initdir/opennebula-gate
install -p -D -m 755 share/pkgs/ALTLinux/opennebula-econe %buildroot%_initdir/opennebula-econe
install -p -D -m 755 share/pkgs/ALTLinux/opennebula-flow  %buildroot%_initdir/opennebula-flow
install -p -D -m 755 share/pkgs/ALTLinux/opennebula-novnc %buildroot%_initdir/opennebula-novnc

install -p -D -m 644 share/pkgs/ALTLinux/opennebula.conf %buildroot%_tmpfilesdir/opennebula.conf
install -p -D -m 644 share/pkgs/ALTLinux/opennebula-node.conf %buildroot%_tmpfilesdir/opennebula-node.conf

install -p -D -m 644 share/pkgs/ALTLinux/opennebula-polkit.rules %buildroot%_sysconfdir/polkit-1/rules.d/50-opennebula.rules

# sudoers
mkdir -p %buildroot%_sysconfdir/sudoers.d
install -p -D -m 440 share/pkgs/ALTLinux/opennebula.sudoers %buildroot%_sysconfdir/sudoers.d/opennebula

# logrotate
mkdir -p %buildroot%_logrotatedir
install -p -D -m 644 share/pkgs/ALTLinux/opennebula.logrotate %buildroot%_logrotatedir/opennebula

# Java
install -p -D -m 644 src/oca/java/jar/org.opennebula.client.jar %buildroot%_javadir/org.opennebula.client.jar

# sysctl
install -p -D -m 644 share/etc/sysctl.d/bridge-nf-call.conf %buildroot%_sysconfdir/sysctl.d/bridge-nf-call.conf

# Gemfile
#install -p -D -m 644 share/install_gems/CentOS7/Gemfile.lock %buildroot%_datadir/one/Gemfile.lock


################################################################################
# common - scripts
################################################################################

%pre common
%_sbindir/groupadd -r -f oneadmin 2>/dev/null ||:
%_sbindir/useradd -r -m -g oneadmin -G disk,wheel -c 'Opennebula Daemon User' \
        -s /bin/bash -d %oneadmin_home oneadmin 2>/dev/null ||:


################################################################################
# server - scripts
################################################################################

%post server
%post_service %name

if [ $1 = 1 ]; then
    if [ ! -e %oneadmin_home/.one/one_auth ]; then
        PASSWORD=$(echo $RANDOM$(date '+%s')|md5sum|cut -d' ' -f1)
        mkdir -p %oneadmin_home/.one
        echo oneadmin:$PASSWORD > %oneadmin_home/.one/one_auth
        chown -R oneadmin:oneadmin %oneadmin_home/.one
    fi

    if [ ! -d %oneadmin_home/.ssh ]; then
        su oneadmin -c "ssh-keygen -N '' -t rsa -f %oneadmin_home/.ssh/id_rsa"
        cp -p %oneadmin_home/.ssh/id_rsa.pub %oneadmin_home/.ssh/authorized_keys
        /bin/chmod 600 %oneadmin_home/.ssh/authorized_keys
    fi
fi

%preun server
%preun_service %name


################################################################################
# node-xen - scripts
################################################################################

# %post node-xen
# if [ $1 = 1 ]; then
#     /usr/bin/grub-bootxen.sh
# fi

################################################################################
# sunstone - scripts
################################################################################

%post sunstone
%post_service %name-sunstone
%post_service %name-novnc

%preun sunstone
%preun_service %name-sunstone
%preun_service %name-novnc

################################################################################
# node-kvm - scripts
################################################################################
%pre node-kvm
%_sbindir/usermod -a -G vmusers oneadmin  2>/dev/null ||:

#Modify /etc/libvirt/qemu.conf to set oneadmin user as running user for libvirt daemon
#Otherwise, you might get some errors like :
#   could not open disk image /var/lib/one/datastores/0/0/disk.0: Permission denied
%post node-kvm
if [ $1 = 1 ]; then
    # Install
    if [ -e /etc/libvirt/qemu.conf ]; then
        cp /etc/libvirt/qemu.conf /etc/libvirt/qemu.conf.orig

        echo 'user  = "oneadmin"'    >  /etc/libvirt/qemu.conf
        echo 'group = "oneadmin"'    >> /etc/libvirt/qemu.conf
        echo 'dynamic_ownership = 0' >> /etc/libvirt/qemu.conf
    fi
elif [ $1 = 2 ]; then
    # Upgrade
    PID=$(cat /tmp/one-collectd-client.pid 2> /dev/null)
    [ -n "$PID" ] && kill $PID 2> /dev/null || :
fi

################################################################################
# ruby - scripts
################################################################################

#%post ruby
#cat <<EOF
#Please remember to execute %_datadir/one/install_gems to install all the
#required gems.
#EOF

################################################################################
# common - files
################################################################################

%files common
%config %_sysconfdir/sudoers.d/opennebula
%config %_sysconfdir/logrotate.d/opennebula

%_datadir/docs/one/*
%_tmpfilesdir/opennebula.conf

%dir %attr(0750, root, oneadmin) %_sysconfdir/one
%dir %attr(0770, root, oneadmin) %_logdir/one
%dir %attr(0775, root, oneadmin) %_runtimedir/one
%dir %attr(0775, root, oneadmin) %_lockdir/one

################################################################################
# node-kvm - files
################################################################################

%files node-kvm
%config %_sysconfdir/polkit-1/rules.d/50-opennebula.rules
%config %_sysconfdir/sysctl.d/bridge-nf-call.conf
%_tmpfilesdir/opennebula-node.conf

################################################################################
# node-xen - files
################################################################################

# %files node-xen

################################################################################
# java - files
################################################################################

%files java
%_javadir/org.opennebula.client.jar

################################################################################
# ruby - files
################################################################################

%files ruby
%_libexecdir/one/ruby/opennebula.rb
%_libexecdir/one/ruby/opennebula/*
%_libexecdir/one/ruby/vendors/rbvmomi/*
%_libexecdir/one/ruby/vcenter_driver.rb
%_libexecdir/one/ruby/vcenter_driver/*

%_libexecdir/one/ruby/OpenNebula.rb

%_libexecdir/one/ruby/cloud/CloudClient.rb
%_libexecdir/one/ruby/cloud/CloudAuth.rb
%_libexecdir/one/ruby/cloud/CloudServer.rb
%_libexecdir/one/ruby/cloud/CloudAuth/*

#%_datadir/one/install_gems
#%_datadir/one/Gemfile
#%_datadir/one/Gemfile.lock

################################################################################
# sunstone - files
################################################################################

%files sunstone
%_libexecdir/one/sunstone/*
%_libexecdir/one/ruby/OpenNebulaVNC.rb
%_libexecdir/one/ruby/cloud/econe/*

%_bindir/sunstone-server
%_bindir/novnc-server
%_bindir/econe-server
%_bindir/econe-allocate-address
%_bindir/econe-associate-address
%_bindir/econe-attach-volume
%_bindir/econe-create-keypair
%_bindir/econe-create-volume
%_bindir/econe-delete-keypair
%_bindir/econe-delete-volume
%_bindir/econe-describe-addresses
%_bindir/econe-describe-images
%_bindir/econe-describe-instances
%_bindir/econe-describe-keypairs
%_bindir/econe-describe-volumes
%_bindir/econe-detach-volume
%_bindir/econe-disassociate-address
%_bindir/econe-reboot-instances
%_bindir/econe-register
%_bindir/econe-release-address
%_bindir/econe-run-instances
%_bindir/econe-start-instances
%_bindir/econe-stop-instances
%_bindir/econe-terminate-instances
%_bindir/econe-upload

%_unitdir/opennebula-sunstone.service
%_unitdir/opennebula-econe.service
%_unitdir/opennebula-novnc.service
%_initdir/opennebula-sunstone
%_initdir/opennebula-econe
%_initdir/opennebula-novnc

%_datadir/one/websockify/*


%defattr(0640, root, oneadmin, 0750)
%config(noreplace) %_sysconfdir/one/sunstone-server.conf
%config(noreplace) %_sysconfdir/one/sunstone-logos.yaml
%config(noreplace) %_sysconfdir/one/ec2query_templates/*
%config(noreplace) %_sysconfdir/one/econe.conf
%config(noreplace) %_sysconfdir/one/sunstone-views.yaml
%config(noreplace) %_sysconfdir/one/sunstone-views/*
%config(noreplace) %_sysconfdir/one/ec2_driver.conf
%config %_sysconfdir/one/ec2_driver.default

################################################################################
# gate - files
################################################################################

%files gate
%config(noreplace) %attr(0640, root, oneadmin) %_sysconfdir/one/onegate-server.conf
%_libexecdir/one/onegate
%_bindir/onegate-server
%_unitdir/opennebula-gate.service
%_initdir/opennebula-gate


################################################################################
# flow - files
################################################################################

%files flow
%config(noreplace) %attr(0640, root, oneadmin) %_sysconfdir/one/oneflow-server.conf
%_libexecdir/one/oneflow
%_bindir/oneflow-server
%_unitdir/opennebula-flow.service
%_initdir/opennebula-flow


################################################################################
# server - files
################################################################################

%files server

%_unitdir/opennebula.service
%_unitdir/opennebula-scheduler.service
%_initdir/opennebula

%_bindir/mm_sched

%_bindir/one
%_bindir/oned
%_bindir/onedb
%_bindir/tty_expect

%_datadir/one/examples/*
%_datadir/one/esx-fw-vnc/*
%_datadir/one/follower_cleanup

%_libexecdir/one/mads/*
%_libexecdir/one/ruby/ActionManager.rb
%_libexecdir/one/ruby/az_driver.rb
%_libexecdir/one/ruby/CommandManager.rb
%_libexecdir/one/ruby/DriverExecHelper.rb
%_libexecdir/one/ruby/ec2_driver.rb
%_libexecdir/one/ruby/onedb/*
%_libexecdir/one/ruby/one_vnm.rb
%_libexecdir/one/ruby/OpenNebulaDriver.rb
%_libexecdir/one/ruby/scripts_common.rb
%_libexecdir/one/ruby/ssh_stream.rb
%_libexecdir/one/ruby/VirtualMachineDriver.rb
%_libexecdir/one/sh/*

%doc LICENSE NOTICE

%dir %attr(0750, oneadmin, oneadmin) %_sharedstatedir/one
%dir %attr(0750, oneadmin, oneadmin) %_sharedstatedir/one/datastores
%dir %attr(0750, oneadmin, oneadmin) %_sharedstatedir/one/remotes

%attr(-, oneadmin, oneadmin) %_sharedstatedir/one/datastores/*
%attr(-, oneadmin, oneadmin) %_sharedstatedir/one/vms
%config(noreplace) %attr(-, oneadmin, oneadmin) %_sharedstatedir/one/remotes/*

%defattr(0640, root, oneadmin, 0750)
%config(noreplace) %_sysconfdir/one/defaultrc
%config(noreplace) %_sysconfdir/one/tmrc
%config(noreplace) %_sysconfdir/one/hm/*
%config(noreplace) %_sysconfdir/one/oned.conf
%config(noreplace) %_sysconfdir/one/sched.conf
%config(noreplace) %_sysconfdir/one/vmm_exec/*
%config(noreplace) %_sysconfdir/one/az_driver.conf
%config %_sysconfdir/one/az_driver.default
%config %_sysconfdir/one/vcenter_driver.default
%config(noreplace) %_sysconfdir/one/auth/server_x509_auth.conf
%config(noreplace) %_sysconfdir/one/auth/ldap_auth.conf
%config(noreplace) %_sysconfdir/one/auth/x509_auth.conf

################################################################################
# tools package - files
################################################################################

%files tools
%dir %_sysconfdir/one/cli
%config(noreplace) %_sysconfdir/one/cli/*

%_bindir/oneacl
%_bindir/onecluster
%_bindir/onedatastore
%_bindir/onegroup
%_bindir/onehost
%_bindir/oneimage
%_bindir/onemarket
%_bindir/onemarketapp
%_bindir/onetemplate
%_bindir/oneuser
%_bindir/onevm
%_bindir/onevmgroup
%_bindir/onevnet
%_bindir/oneacct
%_bindir/onezone
%_bindir/onevcenter
%_bindir/onesecgroup
%_bindir/oneshowback
%_bindir/onevdc
%_bindir/onevrouter

%_bindir/oneflow
%_bindir/oneflow-template

%_libexecdir/one/ruby/cli/*

%_datadir/one/onetoken.sh

################################################################################
# Changelog
################################################################################

%changelog
* Sat Jan 27 2018 Alexey Shabalin <shaba@altlinux.ru> 5.4.6-alt1.S1
- 5.4.6

* Thu Dec 14 2017 Alexey Shabalin <shaba@altlinux.ru> 5.4.5-alt1%ubt
- 5.4.5
- fix install ALTLinux logo
- update Requires: libvirt-qemu to libvirt-kvm in node-kvm package

* Tue Dec 05 2017 Alexey Shabalin <shaba@altlinux.ru> 5.4.4-alt1%ubt
- 5.4.4

* Wed Nov 08 2017 Alexey Shabalin <shaba@altlinux.ru> 5.4.3-alt1%ubt
- 5.4.3

* Wed Oct 11 2017 Alexey Shabalin <shaba@altlinux.ru> 5.4.2-alt1%ubt
- 5.4.2

* Tue Sep 19 2017 Alexey Shabalin <shaba@altlinux.ru> 5.4.1-alt1%ubt
- 5.4.1

* Wed Sep 13 2017 Alexey Shabalin <shaba@altlinux.ru> 5.4.0-alt5%ubt
- update to one-5.4 branch

* Fri Sep 08 2017 Alexey Shabalin <shaba@altlinux.ru> 5.4.0-alt4%ubt
- add user oneadmin to wheel group for allow run sudo

* Tue Sep 05 2017 Alexey Shabalin <shaba@altlinux.ru> 5.4.0-alt3%ubt
- fix run sunstone (add nodejs and bower modules to source)

* Tue Sep 05 2017 Alexey Shabalin <shaba@altlinux.ru> 5.4.0-alt2%ubt
- update to one-5.4 branch
- fix post scripts
- rename package client to tools

* Wed Aug 30 2017 Alexey Shabalin <shaba@altlinux.ru> 5.4.0-alt1%ubt
- Initial build (based on upstream spec)
