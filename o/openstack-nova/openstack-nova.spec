Name:		openstack-nova
Version:	2012.2.0.7
Release:	alt4
Summary:	OpenStack Compute (nova)

Group:		System/Servers
License:	ASL 2.0
URL:		http://openstack.org/projects/compute/
Source0:	%{name}-%{version}.tar
Source1:	nova.conf
Source6:	nova.logrotate

Source10:	%{name}-api.service
Source11:	%{name}-cert.service
Source12:	%{name}-compute.service
Source13:	%{name}-network.service
Source14:	%{name}-objectstore.service
Source15:	%{name}-scheduler.service
Source16:	%{name}-volume.service
Source18:	%{name}-xvpvncproxy.service
Source19:	%{name}-console.service
Source20:	%{name}-consoleauth.service
Source25:	%{name}-metadata-api.service

Source101:	%{name}-api.init
Source111:	%{name}-cert.init
Source121:	%{name}-compute.init
Source131:	%{name}-network.init
Source141:	%{name}-objectstore.init
Source151:	%{name}-scheduler.init
Source161:	%{name}-volume.init
Source181:	%{name}-xvpvncproxy.init
Source191:	%{name}-console.init
Source201:	%{name}-consoleauth.init
Source251:	%{name}-metadata-api.init

Source21:	nova-polkit.rules
Source22:	nova-ifc-template
Source24:	nova-sudoers
Source26:	init-functions.sh

#
# patches_base=folsom-3
#
Patch0001:	%{name}-ensure-we-don-t-access-the-net-when-building-docs.patch

BuildArch:	noarch
BuildRequires:	intltool
BuildRequires:	python-module-sphinx
BuildRequires:	python-module-distribute
BuildRequires:	python-module-netaddr

Requires:	%{name}-compute = %{version}-%{release}
Requires:	%{name}-cert = %{version}-%{release}
Requires:	%{name}-scheduler = %{version}-%{release}
Requires:	%{name}-volume = %{version}-%{release}
Requires:	%{name}-api = %{version}-%{release}
Requires:	%{name}-network = %{version}-%{release}
Requires:	%{name}-objectstore = %{version}-%{release}
Requires:	%{name}-console = %{version}-%{release}

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
Summary:	Components common to all OpenStack Nova services
Group:		System/Servers

Requires:	python-module-nova = %{version}-%{release}
Requires:	polkit

Requires(pre):		shadow-utils

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
Summary:	OpenStack Nova Virtual Machine control service
Group:		System/Servers

Requires:	openstack-nova-common = %{version}-%{release}
Requires:	curl
Requires:	iscsitarget-utils
Requires:	iptables iptables-ipv6
Requires:	vlan-utils
Requires:	libguestfs-tools >= 1.7.17
Requires:	libvirt >= 0.9.6
Requires:	python-module-libvirt
Requires(pre):	qemu-kvm

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
Summary:	OpenStack Nova Network control service
Group:		System/Servers

Requires:	openstack-nova-common = %{version}-%{release}
Requires:	vlan-utils
Requires:	radvd
Requires:	bridge-utils
Requires:	dnsmasq

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


%package volume
Summary:	OpenStack Nova storage volume control service
Group:		System/Servers

Requires:	openstack-nova-common = %{version}-%{release}
Requires:	lvm2
Requires:	scsitarget-utils

%description volume
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova service for controlling storage volumes.


%package scheduler
Summary:	OpenStack Nova VM distribution service
Group:		System/Servers

Requires:	openstack-nova-common = %{version}-%{release}

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
Summary:	OpenStack Nova certificate management service
Group:		System/Servers

Requires:	openstack-nova-common = %{version}-%{release}

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
Summary:	OpenStack Nova API services
Group:		System/Servers

Requires:	openstack-nova-common = %{version}-%{release}

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


%package objectstore
Summary:	OpenStack Nova simple object store service
Group:		System/Servers

Requires:	openstack-nova-common = %{version}-%{release}

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
Summary:	OpenStack Nova console access services
Group:		System/Servers

Requires:	openstack-nova-common = %{version}-%{release}

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


%package -n python-module-nova
Summary:	Nova Python libraries
Group:		Development/Python

Requires:	openssl
Requires:	sudo

Requires:	python-module-MySQLdb
Requires:	python-module-paramiko
Requires:	python-module-qpid
Requires:	python-module-kombu
Requires:	python-module-amqplib
Requires:	python-module-daemon
Requires:	python-module-eventlet
Requires:	python-module-greenlet
Requires:	python-module-iso8601
Requires:	python-module-netaddr
Requires:	python-module-lxml
Requires:	python-module-anyjson
Requires:	python-module-boto
Requires:	python-module-cheetah
Requires:	python-module-ldap
Requires:	python-module-memcached
Requires:	python-module-SQLAlchemy
Requires:	python-module-migrate
Requires:	python-module-PasteDeploy
Requires:	python-module-routes
Requires:	python-module-webob
Requires:	python-module-glanceclient
Requires:	python-module-quantumclient
Requires:	python-module-cinderclient
Requires:	python-module-novaclient

%description -n python-module-nova
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform.

This package contains the nova Python library.

%package doc
Summary:	Documentation for OpenStack Compute
Group:		Documentation

Requires:	%{name} = %{version}-%{release}

BuildRequires:	graphviz

# Required to build module documents
BuildRequires:	python-module-boto
BuildRequires:	python-module-eventlet
BuildRequires:	python-module-routes
BuildRequires:	python-module-SQLAlchemy
BuildRequires:	python-module-webob
# while not strictly required, quiets the build down when building docs.
BuildRequires:	python-module-migrate
BuildRequires:	python-module-iso8601

%description doc
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform.

This package contains documentation files for nova.

%prep
%setup -q

%patch0001 -p1

find . \( -name .gitignore -o -name .placeholder \) -delete

find nova -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

sed -i '/setuptools_git/d' setup.py

%build
%python_build

%install
%python_install

# docs generation requires everything to be installed first
export PYTHONPATH="$( pwd ):$PYTHONPATH"

pushd doc

SPHINX_DEBUG=1 sphinx-build -b html source build/html
# Fix hidden-file-or-dir warnings
rm -fr build/html/.doctrees build/html/.buildinfo

# Create dir link to avoid a sphinx-build exception
mkdir -p build/man/.doctrees/
ln -s .  build/man/.doctrees/man
SPHINX_DEBUG=1 sphinx-build -b man -c source source/man build/man
mkdir -p %{buildroot}%{_mandir}/man1
install -p -D -m 644 build/man/*.1 %{buildroot}%{_mandir}/man1/

popd

# Setup directories
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/buckets
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/images
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/instances
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/keys
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/networks
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/tmp
install -d -m 755 %{buildroot}%{_logdir}/nova

# Setup ghost CA cert
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/CA
install -p -m 755 nova/CA/*.sh %{buildroot}%{_sharedstatedir}/nova/CA
install -p -m 644 nova/CA/openssl.cnf.tmpl %{buildroot}%{_sharedstatedir}/nova/CA
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/CA/{certs,crl,newcerts,projects,reqs}
touch %{buildroot}%{_sharedstatedir}/nova/CA/{cacert.pem,crl.pem,index.txt,openssl.cnf,serial}
install -d -m 750 %{buildroot}%{_sharedstatedir}/nova/CA/private
touch %{buildroot}%{_sharedstatedir}/nova/CA/private/cakey.pem

# Install config files
install -d -m 755 %{buildroot}%{_sysconfdir}/nova
install -p -D -m 640 %{SOURCE1} %{buildroot}%{_sysconfdir}/nova/nova.conf
install -p -D -m 640 etc/nova/rootwrap.conf %{buildroot}%{_sysconfdir}/nova/rootwrap.conf
install -p -D -m 640 etc/nova/api-paste.ini %{buildroot}%{_sysconfdir}/nova/api-paste.ini
install -p -D -m 640 etc/nova/policy.json %{buildroot}%{_sysconfdir}/nova/policy.json

# Install initscripts for Nova services
install -p -D -m 755 %{SOURCE10} %{buildroot}%{_unitdir}/openstack-nova-api.service
install -p -D -m 755 %{SOURCE11} %{buildroot}%{_unitdir}/openstack-nova-cert.service
install -p -D -m 755 %{SOURCE12} %{buildroot}%{_unitdir}/openstack-nova-compute.service
install -p -D -m 755 %{SOURCE13} %{buildroot}%{_unitdir}/openstack-nova-network.service
install -p -D -m 755 %{SOURCE14} %{buildroot}%{_unitdir}/openstack-nova-objectstore.service
install -p -D -m 755 %{SOURCE15} %{buildroot}%{_unitdir}/openstack-nova-scheduler.service
install -p -D -m 755 %{SOURCE16} %{buildroot}%{_unitdir}/openstack-nova-volume.service
install -p -D -m 755 %{SOURCE18} %{buildroot}%{_unitdir}/openstack-nova-xvpvncproxy.service
install -p -D -m 755 %{SOURCE19} %{buildroot}%{_unitdir}/openstack-nova-console.service
install -p -D -m 755 %{SOURCE20} %{buildroot}%{_unitdir}/openstack-nova-consoleauth.service
install -p -D -m 755 %{SOURCE25} %{buildroot}%{_unitdir}/openstack-nova-metadata-api.service

# Install init scripts
install -p -D -m 755 %{SOURCE101} %{buildroot}%{_initdir}/openstack-nova-api
install -p -D -m 755 %{SOURCE111} %{buildroot}%{_initdir}/openstack-nova-cert
install -p -D -m 755 %{SOURCE121} %{buildroot}%{_initdir}/openstack-nova-compute
install -p -D -m 755 %{SOURCE131} %{buildroot}%{_initdir}/openstack-nova-network
install -p -D -m 755 %{SOURCE141} %{buildroot}%{_initdir}/openstack-nova-objectstore
install -p -D -m 755 %{SOURCE151} %{buildroot}%{_initdir}/openstack-nova-scheduler
install -p -D -m 755 %{SOURCE161} %{buildroot}%{_initdir}/openstack-nova-volume
install -p -D -m 755 %{SOURCE181} %{buildroot}%{_initdir}/openstack-nova-xvpvncproxy
install -p -D -m 755 %{SOURCE191} %{buildroot}%{_initdir}/openstack-nova-console
install -p -D -m 755 %{SOURCE201} %{buildroot}%{_initdir}/openstack-nova-consoleauth
install -p -D -m 755 %{SOURCE251} %{buildroot}%{_initdir}/openstack-nova-metadata-api

# Install init-funstions.sh
install -p -D -m 644 %{SOURCE26} %{buildroot}%{_datadir}/nova/init-functions.sh

# Install sudoers
install -p -D -m 400 %{SOURCE24} %{buildroot}%{_sysconfdir}/sudoers.d/nova

# Install logrotate
install -p -D -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/logrotate.d/openstack-nova

# Install pid directory
install -d -m 755 %{buildroot}%{_runtimedir}/nova

# Install template files
install -p -D -m 644 nova/cloudpipe/client.ovpn.template %{buildroot}%{_datadir}/nova/client.ovpn.template
install -p -D -m 644 nova/virt/interfaces.template %{buildroot}%{_datadir}/nova/interfaces.template
install -p -D -m 644 %{SOURCE22} %{buildroot}%{_datadir}/nova/interfaces.template

# Install rootwrap files in /usr/share/nova/rootwrap
mkdir -p %{buildroot}%{_datadir}/nova/rootwrap/
install -p -D -m 644 etc/nova/rootwrap.d/* %{buildroot}%{_datadir}/nova/rootwrap/

# Install policy-kit rules to allow nova user to manage libvirt
install -p -D -m 644 %{SOURCE21} %{buildroot}%{_sysconfdir}/polkit-1/rules.d/50-libvirt-nova.rules

# Remove unneeded in production stuff
rm -f %{buildroot}%{_bindir}/nova-debug
rm -fr %{buildroot}%{python_sitelibdir}/nova/tests/
rm -fr %{buildroot}%{python_sitelibdir}/run_tests.*
rm -f %{buildroot}%{_bindir}/nova-combined
rm -f %{buildroot}/usr/share/doc/nova/README*

# FIXME
# TODO. On F18 branch of novnc package, move the openstack-nova-novncproxy
# subpackage to the openstack-nova-console subpackage here, and have
# it provide openstack-nova-novncproxy
rm -f %{buildroot}%{_bindir}/nova-novncproxy

%pre common
getent group nova >/dev/null || groupadd -r nova --gid 162
if ! getent passwd nova >/dev/null; then
  useradd -u 162 -r -g nova -G nova,nobody -d %{_sharedstatedir}/nova -s /sbin/nologin -c "OpenStack Nova Daemons" nova
fi
exit 0

%pre compute
usermod -a -G qemu nova
# Add nova to the fuse group (if present) to support guestmount
if getent group fuse >/dev/null; then
  usermod -a -G fuse nova
fi
exit 0

%post compute
%post_service %{name}-compute

%preun compute
%preun_service %{name}-compute

%post network
%post_service %{name}-network

%preun network
%preun_service %{name}-network

%post volume
%post_service %{name}-volume

%preun volume
%preun_service %{name}-volume

%post scheduler
%post_service %{name}-scheduler

%preun scheduler
%preun_service %{name}-scheduler

%post cert
%post_service %{name}-cert

%preun cert
%preun_service %{name}-cert

%post api
%post_service %{name}-api
%post_service %{name}-metadata-api

%preun api
%preun_service %{name}-api
%preun_service %{name}-metadata-api

%post objectstore
%post_service %{name}-objectstore

%preun objectstore
%preun_service %{name}-objectstore

%post console
%post_service %{name}-console
%post_service %{name}-consoleauth
%post_service %{name}-xvpvncproxy

%preun console
%preun_service %{name}-console
%preun_service %{name}-consoleauth
%preun_service %{name}-xvpvncproxy

%files
%doc LICENSE
%{_bindir}/nova-all

%files common
%doc LICENSE
%dir %{_sysconfdir}/nova
%config(noreplace) %attr(-, root, nova) %{_sysconfdir}/nova/nova.conf
%config(noreplace) %attr(-, root, nova) %{_sysconfdir}/nova/api-paste.ini
%config(noreplace) %attr(-, root, nova) %{_sysconfdir}/nova/rootwrap.conf
%config(noreplace) %attr(-, root, nova) %{_sysconfdir}/nova/policy.json
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/sudoers.d/nova
%config(noreplace) %{_sysconfdir}/polkit-1/rules.d/50-libvirt-nova.rules

%dir %attr(0755, nova, root) %{_logdir}/nova
%dir %attr(0755, nova, root) %{_runtimedir}/nova

%{_bindir}/nova-clear-rabbit-queues
# TODO. zmq-receiver may need its own service?
%{_bindir}/nova-rpc-zmq-receiver
%{_bindir}/nova-manage
%{_bindir}/nova-rootwrap

%dir %{_datadir}/nova
%dir %{_datadir}/nova/rootwrap
%{_datadir}/nova/interfaces.template
%{_datadir}/nova/client.ovpn.template
%{_datadir}/nova/init-functions.sh

%{_mandir}/man1/nova*.1.gz

%defattr(-, nova, nova, -)
%dir %{_sharedstatedir}/nova
%dir %{_sharedstatedir}/nova/buckets
%dir %{_sharedstatedir}/nova/images
%dir %{_sharedstatedir}/nova/instances
%dir %{_sharedstatedir}/nova/keys
%dir %{_sharedstatedir}/nova/networks
%dir %{_sharedstatedir}/nova/tmp

%files compute
%{_bindir}/nova-compute
%{_unitdir}/%{name}-compute.service
%{_initdir}/openstack-nova-compute
%{_datadir}/nova/rootwrap/compute.filters

%files network
%{_bindir}/nova-network
%{_bindir}/nova-dhcpbridge
%{_unitdir}/%{name}-network.service
%{_initdir}/openstack-nova-network
%{_datadir}/nova/rootwrap/network.filters

%files volume
%{_bindir}/nova-volume
%{_bindir}/nova-volume-usage-audit
%{_unitdir}/%{name}-volume.service
%{_initdir}/openstack-nova-volume
%{_datadir}/nova/rootwrap/volume.filters

%files scheduler
%{_bindir}/nova-scheduler
%{_unitdir}/%{name}-scheduler.service
%{_initdir}/openstack-nova-scheduler

%files cert
%{_bindir}/nova-cert
%{_unitdir}/%{name}-cert.service
%{_initdir}/openstack-nova-cert
%defattr(-, nova, nova, -)
%dir %{_sharedstatedir}/nova/CA/
%dir %{_sharedstatedir}/nova/CA/certs
%dir %{_sharedstatedir}/nova/CA/crl
%dir %{_sharedstatedir}/nova/CA/newcerts
%dir %{_sharedstatedir}/nova/CA/projects
%dir %{_sharedstatedir}/nova/CA/reqs
%{_sharedstatedir}/nova/CA/*.sh
%{_sharedstatedir}/nova/CA/openssl.cnf.tmpl
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/cacert.pem
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/crl.pem
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/index.txt
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/openssl.cnf
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/serial
%dir %attr(0750, nova, nova) %{_sharedstatedir}/nova/CA/private
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/private/cakey.pem

%files api
%{_bindir}/nova-api*
%{_unitdir}/%{name}-*api.service
%{_initdir}/openstack-nova-*api
%{_datadir}/nova/rootwrap/api-metadata.filters

%files objectstore
%{_bindir}/nova-objectstore
%{_unitdir}/%{name}-objectstore.service
%{_initdir}/openstack-nova-objectstore

%files console
%{_bindir}/nova-console*
%{_bindir}/nova-xvpvncproxy
%{_unitdir}/%{name}-console*.service
%{_unitdir}/%{name}-xvpvncproxy.service
%{_initdir}/openstack-nova-console*
%{_initdir}/openstack-nova-xvpvncproxy

%files -n python-module-nova
%doc LICENSE
%{python_sitelibdir}/nova
%{python_sitelibdir}/nova-*.egg-info

%files doc
%doc LICENSE doc/build/html

%changelog
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
