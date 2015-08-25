%add_findreq_skiplist %python_sitelibdir/nova/cloudpipe/*.template

Name: openstack-nova
Version: 2015.1.1
Release: alt1
Summary: OpenStack Compute (nova)

Group: System/Servers
License: ASL 2.0
Url: http://openstack.org/projects/compute/
Source0: %name-%version.tar

Source1: nova-dist.conf
Source2: nova.conf.sample
Source6: nova.logrotate

Source3: %name.tmpfiles

Source10: %name-api.service
Source11: %name-cert.service
Source12: %name-compute.service
Source13: %name-network.service
Source14: %name-objectstore.service
Source15: %name-scheduler.service
Source18: %name-xvpvncproxy.service
Source19: %name-console.service
Source20: %name-consoleauth.service
Source25: %name-metadata-api.service
Source26: %name-conductor.service
Source27: %name-cells.service
Source28: %name-spicehtml5proxy.service
Source29: %name-novncproxy.service
Source31: %name-serialproxy.service

Source110: %name-api.init
Source111: %name-cert.init
Source112: %name-compute.init
Source113: %name-network.init
Source114: %name-objectstore.init
Source115: %name-scheduler.init
Source118: %name-xvpvncproxy.init
Source119: %name-console.init
Source120: %name-consoleauth.init
Source125: %name-metadata-api.init
Source126: %name-conductor.init
Source127: %name-cells.init
Source128: %name-spicehtml5proxy.init
Source129: %name-novncproxy.init
Source131: %name-serialproxy.init

Source21: nova-polkit.pkla
Source23: nova-polkit.rules
Source22: nova-ifc-template
Source24: nova-sudoers
Source30: %name-novncproxy.sysconfig

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr
BuildRequires: python-module-d2to1
BuildRequires: python-module-six
BuildRequires: python-module-babel
BuildRequires: python-module-oslo.i18n >= 1.5.0
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-netaddr
# Required to build module documents
BuildRequires: python-module-boto
BuildRequires: python-module-eventlet >= 0.16.1
BuildRequires: python-module-routes
BuildRequires: python-module-SQLAlchemy >= 0.9.7
BuildRequires: python-module-webob
BuildRequires: python-module-migrate >= 0.9.5
BuildRequires: python-module-iso8601
BuildRequires: python-module-keystonemiddleware >= 1.5.0

BuildRequires: graphviz

Requires: %name-compute = %version-%release
Requires: %name-cert = %version-%release
Requires: %name-scheduler = %version-%release
Requires: %name-api = %version-%release
Requires: %name-network = %version-%release
Requires: %name-objectstore = %version-%release
Requires: %name-conductor = %version-%release
Requires: %name-console = %version-%release
Requires: %name-cells = %version-%release
Requires: %name-novncproxy = %version-%release

%description
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

%package common
Summary: Components common to all OpenStack Nova services
Group: System/Servers

Requires: python-module-nova = %version-%release
Requires: python-module-oslo.rootwrap >= 1.6.0
Requires: python-module-oslo.messaging >= 1.8.0
Requires(pre): shadow-utils

%description common
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains scripts, config and dependencies shared
between all the OpenStack nova services.

%package compute
Summary: OpenStack Nova Virtual Machine control service
Group: System/Servers

Requires: openstack-nova-common = %version-%release
Requires: curl
Requires: open-iscsi
Requires: iptables iptables-ipv6
Requires: ipmitool
Requires: python-module-libvirt libvirt-kvm
Requires: openssh-clients
Requires: rsync
Requires: lvm2
Requires: python-module-cinderclient
Requires(pre): qemu-kvm
Requires: genisoimage
Requires: bridge-utils
Requires: sysfsutils
Requires: guestfs-data python-module-libguestfs libguestfs-tools

%description compute
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova service for controlling Virtual Machines.

%package network
Summary: OpenStack Nova Network control service
Group: System/Servers

Requires: openstack-nova-common = %version-%release
Requires: radvd
Requires: bridge-utils
Requires: dnsmasq
Requires: dnsmasq-utils
Requires: ebtables

%description network
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova service for controlling networking.

%package scheduler
Summary: OpenStack Nova VM distribution service
Group: System/Servers

Requires: openstack-nova-common = %version-%release

%description scheduler
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the service for scheduling where
to run Virtual Machines in the cloud.

%package cert
Summary: OpenStack Nova certificate management service
Group: System/Servers

Requires: openstack-nova-common = %version-%release

%description cert
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova service for managing certificates.

%package api
Summary: OpenStack Nova API services
Group: System/Servers

Requires: openstack-nova-common = %version-%release

%description api
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova services providing programmatic access.

%package conductor
Summary: OpenStack Nova Conductor services
Group: System/Servers

Requires: openstack-nova-common = %version-%release

%description conductor
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova services providing database access for
the compute service

%package objectstore
Summary: OpenStack Nova simple object store service
Group: System/Servers

Requires: openstack-nova-common = %version-%release

%description objectstore
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova service providing a simple object store.

%package console
Summary: OpenStack Nova console access services
Group: System/Servers

Requires: openstack-nova-common = %version-%release
Requires: python-module-websockify

%description console
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova services providing
console access services to Virtual Machines.

%package cells
Summary: OpenStack Nova Cells services
Group: System/Servers

Requires: openstack-nova-common = %version-%release

%description cells
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova Cells service providing additional
scaling and (geographic) distribution for compute services.

%package novncproxy
Summary: OpenStack Nova noVNC proxy service
Group: System/Servers

Requires: openstack-nova-common = %version-%release
Requires: novnc
Requires: python-module-websockify

%description novncproxy
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova noVNC Proxy service that can proxy
VNC traffic over browser websockets connections.

%package spicehtml5proxy
Summary: OpenStack Nova Spice HTML5 console access service
Group: System/Servers

Requires: openstack-nova-common = %version-%release
Requires: python-module-websockify

%description spicehtml5proxy
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova services providing the
spice HTML5 console access service to Virtual Machines.

%package serialproxy
Summary: OpenStack Nova serial console access service
Group: System/Servers

Requires: openstack-nova-common = %version-%release
Requires: python-module-websockify

%description serialproxy
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova services providing the
serial console access service to Virtual Machines.

%package -n python-module-nova
Summary: Nova Python libraries
Group: Development/Python

Requires: openssl
# Require openssh for ssh-keygen
Requires: openssh-common
Requires: sudo

%description -n python-module-nova
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform.

This package contains the nova Python library.

%package doc
Summary: Documentation for OpenStack Compute
Group: Documentation

%description doc
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform.

This package contains documentation files for nova.

%prep
%setup

find . \( -name .gitignore -o -name .placeholder \) -delete

find nova -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

# Remove the requirements file so that pbr hooks don't add it
# to distutils requiers_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

%build
%python_build
export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b man doc/source doc/build/man
sphinx-build -b html doc/source doc/build/html
bash tools/config/generate_sample.sh -b . -p nova -o etc/nova

#install -p -D -m 640 %SOURCE2 etc/nova/nova.conf.sample

# Avoid http://bugzilla.redhat.com/1059815. Remove when that is closed
sed -i 's|group/name|group;name|; s|\[DEFAULT\]/|DEFAULT;|' etc/nova/nova.conf.sample

# Programmatically update defaults in sample config
# which is installed at /etc/nova/nova.conf

#  First we ensure all values are commented in appropriate format.
#  Since icehouse, there was an uncommented keystone_authtoken section
#  at the end of the file which mimics but also conflicted with our
#  distro editing that had been done for many releases.
sed -i '/^[^#[]/{s/^/#/; s/ //g}; /^#[^ ]/s/ = /=/' etc/nova/nova.conf.sample

#  TODO: Make this more robust
#  Note it only edits the first occurance, so assumes a section ordering in sample
#  and also doesn't support multi-valued variables like dhcpbridge_flagfile.
while read name eq value; do
  test "$name" && test "$value" || continue
  sed -i "0,/^# *$name=/{s!^# *$name=.*!#$name=$value!}" etc/nova/nova.conf.sample
done < %SOURCE1

%install
%python_install

mkdir -p %buildroot%_man1dir
install -p -D -m 644 doc/build/man/*.1 %buildroot%_man1dir/

# Setup directories
install -d -m 755 %buildroot%_sharedstatedir/nova
install -d -m 755 %buildroot%_sharedstatedir/nova/buckets
install -d -m 755 %buildroot%_sharedstatedir/nova/instances
install -d -m 755 %buildroot%_sharedstatedir/nova/keys
install -d -m 755 %buildroot%_sharedstatedir/nova/networks
install -d -m 755 %buildroot%_sharedstatedir/nova/tmp
install -d -m 750 %buildroot%_logdir/nova

# Setup ghost CA cert
install -d -m 755 %buildroot%_sharedstatedir/nova/CA
install -p -m 755 nova/CA/*.sh %buildroot%_sharedstatedir/nova/CA
install -p -m 644 nova/CA/openssl.cnf.tmpl %buildroot%_sharedstatedir/nova/CA
install -d -m 755 %buildroot%_sharedstatedir/nova/CA/{certs,crl,newcerts,projects,reqs}
touch %buildroot%_sharedstatedir/nova/CA/{cacert.pem,crl.pem,index.txt,openssl.cnf,serial}
install -d -m 750 %buildroot%_sharedstatedir/nova/CA/private
touch %buildroot%_sharedstatedir/nova/CA/private/cakey.pem

# Install config files
install -d -m 755 %buildroot%_sysconfdir/nova
install -p -D -m 640 %SOURCE1 %buildroot%_datadir/nova/nova-dist.conf
install -p -D -m 640 etc/nova/nova.conf.sample  %buildroot%_sysconfdir/nova/nova.conf
install -p -D -m 640 etc/nova/rootwrap.conf %buildroot%_sysconfdir/nova/
install -p -D -m 640 etc/nova/api-paste.ini %buildroot%_sysconfdir/nova/
install -p -D -m 640 etc/nova/policy.json %buildroot%_sysconfdir/nova/

# Install version info file
cat > %buildroot%_sysconfdir/nova/release <<EOF
[Nova]
vendor = ALTLinux
product = OpenStack Nova
package = %version
EOF

# tmpfiles
install -p -D -m 644 %SOURCE3 %buildroot%_tmpfilesdir/%name.conf

# Install initscripts for Nova services
install -p -D -m 644 %SOURCE10 %buildroot%_unitdir/openstack-nova-api.service
install -p -D -m 644 %SOURCE11 %buildroot%_unitdir/openstack-nova-cert.service
install -p -D -m 644 %SOURCE12 %buildroot%_unitdir/openstack-nova-compute.service
install -p -D -m 644 %SOURCE13 %buildroot%_unitdir/openstack-nova-network.service
install -p -D -m 644 %SOURCE14 %buildroot%_unitdir/openstack-nova-objectstore.service
install -p -D -m 644 %SOURCE15 %buildroot%_unitdir/openstack-nova-scheduler.service
install -p -D -m 644 %SOURCE18 %buildroot%_unitdir/openstack-nova-xvpvncproxy.service
install -p -D -m 644 %SOURCE19 %buildroot%_unitdir/openstack-nova-console.service
install -p -D -m 644 %SOURCE20 %buildroot%_unitdir/openstack-nova-consoleauth.service
install -p -D -m 644 %SOURCE25 %buildroot%_unitdir/openstack-nova-metadata-api.service
install -p -D -m 644 %SOURCE26 %buildroot%_unitdir/openstack-nova-conductor.service
install -p -D -m 644 %SOURCE27 %buildroot%_unitdir/openstack-nova-cells.service
install -p -D -m 644 %SOURCE28 %buildroot%_unitdir/openstack-nova-spicehtml5proxy.service
install -p -D -m 644 %SOURCE29 %buildroot%_unitdir/openstack-nova-novncproxy.service
install -p -D -m 644 %SOURCE31 %buildroot%_unitdir/openstack-nova-serialproxy.service

# Install init scripts
install -p -D -m 755 %SOURCE110 %buildroot%_initdir/openstack-nova-api
install -p -D -m 755 %SOURCE111 %buildroot%_initdir/openstack-nova-cert
install -p -D -m 755 %SOURCE112 %buildroot%_initdir/openstack-nova-compute
install -p -D -m 755 %SOURCE113 %buildroot%_initdir/openstack-nova-network
install -p -D -m 755 %SOURCE114 %buildroot%_initdir/openstack-nova-objectstore
install -p -D -m 755 %SOURCE115 %buildroot%_initdir/openstack-nova-scheduler
install -p -D -m 755 %SOURCE118 %buildroot%_initdir/openstack-nova-xvpvncproxy
install -p -D -m 755 %SOURCE119 %buildroot%_initdir/openstack-nova-console
install -p -D -m 755 %SOURCE120 %buildroot%_initdir/openstack-nova-consoleauth
install -p -D -m 755 %SOURCE125 %buildroot%_initdir/openstack-nova-metadata-api
install -p -D -m 755 %SOURCE126 %buildroot%_initdir/openstack-nova-conductor
install -p -D -m 755 %SOURCE127 %buildroot%_initdir/openstack-nova-cells
install -p -D -m 755 %SOURCE128 %buildroot%_initdir/openstack-nova-spicehtml5proxy
install -p -D -m 755 %SOURCE129 %buildroot%_initdir/openstack-nova-novncproxy
install -p -D -m 755 %SOURCE131 %buildroot%_initdir/openstack-nova-serialproxy

# Install sudoers
install -p -D -m 400 %SOURCE24 %buildroot%_sysconfdir/sudoers.d/nova

# Install logrotate
install -p -D -m 644 %SOURCE6 %buildroot%_sysconfdir/logrotate.d/openstack-nova

# Install pid directory
install -d -m 755 %buildroot%_runtimedir/nova

# Install template files
install -p -D -m 644 nova/cloudpipe/client.ovpn.template %buildroot%_datadir/nova/client.ovpn.template
install -p -D -m 644 %SOURCE22 %buildroot%_datadir/nova/interfaces.template

# Install rootwrap files in /usr/share/nova/rootwrap
mkdir -p %buildroot%_datadir/nova/rootwrap/
install -p -D -m 644 etc/nova/rootwrap.d/* %buildroot%_datadir/nova/rootwrap/

# Install policy-kit rules to allow nova user to manage libvirt
install -p -D -m 644 %SOURCE23 %buildroot%_sysconfdir/polkit-1/rules.d/50-nova.rules

# Install novncproxy service options template
install -d %buildroot%_sysconfdir/sysconfig
install -p -m 0644 %SOURCE30 %buildroot%_sysconfdir/sysconfig/openstack-nova-novncproxy

# Remove unneeded in production stuff
rm -f %buildroot%_bindir/nova-debug
rm -fr %buildroot%python_sitelibdir/nova/tests/
rm -f %buildroot%python_sitelibdir/nova/test.*
rm -fr %buildroot%python_sitelibdir/run_tests.*
rm -f %buildroot%_bindir/nova-combined
rm -f %buildroot/usr/share/doc/nova/README*

%pre common
# 162:162 for nova (openstack-nova)
%_sbindir/groupadd -r -g 162 -f nova 2>/dev/null ||:
%_sbindir/useradd -r -u 162 -g nova -G nova,nobody,wheel -c 'OpenStack Nova Daemons' \
        -s /sbin/nologin  -d %_sharedstatedir/nova nova 2>/dev/null ||:


%pre compute
usermod -a -G vmusers nova 2>/dev/null ||:
usermod -a -G fuse nova 2>/dev/null ||:

%post compute
%post_service %name-compute
%preun compute
%preun_service %name-compute

%post network
%post_service %name-network
%preun network
%preun_service %name-network

%post scheduler
%post_service %name-scheduler
%preun scheduler
%preun_service %name-scheduler

%post cert
%post_service %name-cert
%preun cert
%preun_service %name-cert

%post api
%post_service %name-api
%post_service %name-metadata-api
%preun api
%preun_service %name-api
%preun_service %name-metadata-api

%post conductor
%post_service %name-conductor
%preun conductor
%preun_service %name-conductor

%post objectstore
%post_service %name-objectstore
%preun objectstore
%preun_service %name-objectstore

%post console
%post_service %name-console
%post_service %name-consoleauth
%post_service %name-xvpvncproxy
%preun console
%preun_service %name-console
%preun_service %name-consoleauth
%preun_service %name-xvpvncproxy

%post cells
%post_service %name-cells
%preun cells
%preun_service %name-cells

%post novncproxy
%post_service %name-novncproxy
%preun novncproxy
%preun_service %name-novncproxy

%post spicehtml5proxy
%post_service %name-spicehtml5proxy
%preun spicehtml5proxy
%preun_service %name-spicehtml5proxy

%post serialproxy
%post_service %name-serialproxy
%preun serialproxy
%preun_service %name-serialproxy


%files
%doc LICENSE
%_bindir/nova-all

%files common
%doc LICENSE
%dir %_sysconfdir/nova
%_sysconfdir/nova/release
%attr(-, root, nova) %_datadir/nova/nova-dist.conf
%config(noreplace) %attr(-, root, nova) %_sysconfdir/nova/nova.conf
%config(noreplace) %attr(-, root, nova) %_sysconfdir/nova/api-paste.ini
%config(noreplace) %attr(-, root, nova) %_sysconfdir/nova/rootwrap.conf
%config(noreplace) %attr(-, root, nova) %_sysconfdir/nova/policy.json
%config(noreplace) %_sysconfdir/logrotate.d/%name
%config(noreplace) %_sysconfdir/sudoers.d/nova
%config(noreplace) %_sysconfdir/polkit-1/rules.d/50-nova.rules

%_tmpfilesdir/%name.conf
%dir %attr(0750, nova, root) %_logdir/nova
%dir %attr(0755, nova, root) %_runtimedir/nova

%_bindir/nova-manage
%_bindir/nova-rootwrap

%_datadir/nova
%exclude %_datadir/nova/rootwrap/compute.filters
%exclude %_datadir/nova/rootwrap/network.filters
%exclude %_datadir/nova/rootwrap/api-metadata.filters

%_man1dir/nova*.1.*

%defattr(-, nova, nova, -)
%dir %_sharedstatedir/nova
%dir %_sharedstatedir/nova/buckets
%dir %_sharedstatedir/nova/instances
%dir %_sharedstatedir/nova/keys
%dir %_sharedstatedir/nova/networks
%dir %_sharedstatedir/nova/tmp

%files compute
%_bindir/nova-compute
%_bindir/nova-idmapshift
%_unitdir/%name-compute.service
%_initdir/%name-compute
%_datadir/nova/rootwrap/compute.filters

%files network
%_bindir/nova-network
%_bindir/nova-dhcpbridge
%_unitdir/%name-network.service
%_initdir/%name-network
%_datadir/nova/rootwrap/network.filters

%files scheduler
%_bindir/nova-scheduler
%_unitdir/%name-scheduler.service
%_initdir/%name-scheduler

%files cert
%_bindir/nova-cert
%_unitdir/%name-cert.service
%_initdir/%name-cert
%defattr(-, nova, nova, -)
%dir %_sharedstatedir/nova/CA/
%dir %_sharedstatedir/nova/CA/certs
%dir %_sharedstatedir/nova/CA/crl
%dir %_sharedstatedir/nova/CA/newcerts
%dir %_sharedstatedir/nova/CA/projects
%dir %_sharedstatedir/nova/CA/reqs
%_sharedstatedir/nova/CA/*.sh
%_sharedstatedir/nova/CA/openssl.cnf.tmpl
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %_sharedstatedir/nova/CA/cacert.pem
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %_sharedstatedir/nova/CA/crl.pem
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %_sharedstatedir/nova/CA/index.txt
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %_sharedstatedir/nova/CA/openssl.cnf
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %_sharedstatedir/nova/CA/serial
%dir %attr(0750, nova, nova) %_sharedstatedir/nova/CA/private
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %_sharedstatedir/nova/CA/private/cakey.pem

%files api
%_bindir/nova-api*
%_unitdir/%name-*api.service
%_initdir/%name-*api
%_datadir/nova/rootwrap/api-metadata.filters

%files conductor
%_bindir/nova-conductor
%_unitdir/%name-conductor.service
%_initdir/%name-conductor

%files objectstore
%_bindir/nova-objectstore
%_unitdir/%name-objectstore.service
%_initdir/%name-objectstore

%files console
%_bindir/nova-console*
%_bindir/nova-xvpvncproxy
%_unitdir/%name-console*.service
%_unitdir/%name-xvpvncproxy.service
%_initdir/%name-console*
%_initdir/%name-xvpvncproxy

%files cells
%_bindir/nova-cells
%_unitdir/%name-cells.service
%_initdir/%name-cells

%files novncproxy
%_bindir/nova-novncproxy
%_unitdir/%name-novncproxy.service
%_initdir/%name-novncproxy
%config(noreplace) %_sysconfdir/sysconfig/openstack-nova-novncproxy

%files spicehtml5proxy
%_bindir/nova-spicehtml5proxy
%_unitdir/%name-spicehtml5proxy.service
%_initdir/%name-spicehtml5proxy

%files serialproxy
%_bindir/nova-serialproxy
%_unitdir/%name-serialproxy.service
%_initdir/%name-serialproxy

%files -n python-module-nova
%doc LICENSE
%python_sitelibdir/nova
%python_sitelibdir/nova-*.egg-info

%files doc
%doc LICENSE doc/build/html

%changelog
* Tue Aug 25 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.1-alt1
- 2015.1.1

* Tue May 19 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt1
- 2015.1.0 Kilo release

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt0.b3.0
- 2015.1.0b3.0

* Fri Mar 13 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt0.b2.0
- 2015.1.0b2.0

* Fri Aug 15 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.2-alt2
- Patch added for live migration:
  * 0100-libvirt-convert-cpu-features-attribute-from-list-to-a-set.patch

* Tue Aug 12 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.2-alt1
- 2014.1.2

* Sat Aug 09 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.1-alt3
- sysfsutils added to Requires: warning about systool

* Tue Aug 05 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.1-alt2
- user nova added to wheel group, for nova-rootwrap

* Wed Jul 09 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.1-alt1
- New version - icehouse (based on Fedora)

* Wed Aug 28 2013 Pavel Shilovsky <piastry@altlinux.org> 2012.2.0.7-alt4
- Cleanup spec

* Fri Aug 16 2013 Pavel Shilovsky <piastry@altlinux.org> 2012.2.0.7-alt3
- Fix sysvinit scripts

* Sat Mar 30 2013 Pavel Shilovsky <piastry@altlinux.org> 2012.2.0.7-alt2.1
- Add SysVinit support

* Wed Mar 06 2013 Pavel Shilovsky <piastry@altlinux.org> 2012.2.0.7-alt2
- Use post/preun_service scripts in spec

* Thu Nov 08 2012 Pavel Shilovsky <piastry@altlinux.org> 2012.2.0.7-alt1
- Initial release for Sisyphus (based on Fedora)
