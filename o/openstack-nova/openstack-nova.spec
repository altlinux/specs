Name:		openstack-nova
Version:	2012.2.0.7
Release:	alt1
Summary:	OpenStack Compute (nova)

Group:		System/Servers
License:	ASL 2.0
URL:		http://openstack.org/projects/compute/
Source0:	%{name}-%{version}.tar.gz
Source1:	nova.conf
Source6:	nova.logrotate

Source10:	openstack-nova-api.service
Source11:	openstack-nova-cert.service
Source12:	openstack-nova-compute.service
Source13:	openstack-nova-network.service
Source14:	openstack-nova-objectstore.service
Source15:	openstack-nova-scheduler.service
Source16:	openstack-nova-volume.service
Source18:	openstack-nova-xvpvncproxy.service
Source19:	openstack-nova-console.service
Source20:	openstack-nova-consoleauth.service
Source25:	openstack-nova-metadata-api.service

Source21:	nova-polkit.pkla
Source22:	nova-ifc-template
Source24:	nova-sudoers

#
# patches_base=folsom-3
#
Patch0001:	%{name}-ensure-we-don-t-access-the-net-when-building-docs.patch

BuildArch:	noarch
BuildRequires:	intltool
BuildRequires:	python-module-sphinx
BuildRequires:	python-module-distribute
BuildRequires:	python-module-netaddr

Requires:	openstack-nova-compute = %{version}-%{release}
Requires:	openstack-nova-cert = %{version}-%{release}
Requires:	openstack-nova-scheduler = %{version}-%{release}
Requires:	openstack-nova-volume = %{version}-%{release}
Requires:	openstack-nova-api = %{version}-%{release}
Requires:	openstack-nova-network = %{version}-%{release}
Requires:	openstack-nova-objectstore = %{version}-%{release}
Requires:	openstack-nova-console = %{version}-%{release}

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

Requires(post):		systemd-units
Requires(preun):	systemd-units
Requires(postun):	systemd-units
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

BuildRequires:	systemd-units
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
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

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
install -d -m 755 %{buildroot}%{_localstatedir}/log/nova

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

# Install sudoers
install -p -D -m 400 %{SOURCE24} %{buildroot}%{_sysconfdir}/sudoers.d/nova

# Install logrotate
install -p -D -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/logrotate.d/openstack-nova

# Install pid directory
install -d -m 755 %{buildroot}%{_localstatedir}/run/nova

# Install template files
install -p -D -m 644 nova/cloudpipe/client.ovpn.template %{buildroot}%{_datadir}/nova/client.ovpn.template
install -p -D -m 644 nova/virt/interfaces.template %{buildroot}%{_datadir}/nova/interfaces.template
install -p -D -m 644 %{SOURCE22} %{buildroot}%{_datadir}/nova/interfaces.template

# Install rootwrap files in /usr/share/nova/rootwrap
mkdir -p %{buildroot}%{_datadir}/nova/rootwrap/
install -p -D -m 644 etc/nova/rootwrap.d/* %{buildroot}%{_datadir}/nova/rootwrap/

install -d -m 755 %{buildroot}%{_sysconfdir}/polkit-1/localauthority/50-local.d
install -p -D -m 644 %{SOURCE21} %{buildroot}%{_sysconfdir}/polkit-1/localauthority/50-local.d/50-nova.pkla

# Remove unneeded in production stuff
rm -f %{buildroot}%{_bindir}/nova-debug
rm -fr %{buildroot}%{python_sitelibdir}/nova/tests/
rm -fr %{buildroot}%{python_sitelibdir}/run_tests.*
rm -f %{buildroot}%{_bindir}/nova-combined
rm -f %{buildroot}/usr/share/doc/nova/README*

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
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%post network
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%post volume
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%post scheduler
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%post cert
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%post api
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%post objectstore
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%post console
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun compute
if [ $1 -eq 0 ] ; then
    for svc in compute; do
        /bin/systemctl --no-reload disable openstack-nova-${svc}.service > /dev/null 2>&1 || :
        /bin/systemctl stop openstack-nova-${svc}.service > /dev/null 2>&1 || :
    done
fi
%preun network
if [ $1 -eq 0 ] ; then
    for svc in network; do
        /bin/systemctl --no-reload disable openstack-nova-${svc}.service > /dev/null 2>&1 || :
        /bin/systemctl stop openstack-nova-${svc}.service > /dev/null 2>&1 || :
    done
fi
%preun volume
if [ $1 -eq 0 ] ; then
    for svc in volume; do
        /bin/systemctl --no-reload disable openstack-nova-${svc}.service > /dev/null 2>&1 || :
        /bin/systemctl stop openstack-nova-${svc}.service > /dev/null 2>&1 || :
    done
fi
%preun scheduler
if [ $1 -eq 0 ] ; then
    for svc in scheduler; do
        /bin/systemctl --no-reload disable openstack-nova-${svc}.service > /dev/null 2>&1 || :
        /bin/systemctl stop openstack-nova-${svc}.service > /dev/null 2>&1 || :
    done
fi
%preun cert
if [ $1 -eq 0 ] ; then
    for svc in cert; do
        /bin/systemctl --no-reload disable openstack-nova-${svc}.service > /dev/null 2>&1 || :
        /bin/systemctl stop openstack-nova-${svc}.service > /dev/null 2>&1 || :
    done
fi
%preun api
if [ $1 -eq 0 ] ; then
    for svc in api metadata-api; do
        /bin/systemctl --no-reload disable openstack-nova-${svc}.service > /dev/null 2>&1 || :
        /bin/systemctl stop openstack-nova-${svc}.service > /dev/null 2>&1 || :
    done
fi
%preun objectstore
if [ $1 -eq 0 ] ; then
    for svc in objectstore; do
        /bin/systemctl --no-reload disable openstack-nova-${svc}.service > /dev/null 2>&1 || :
        /bin/systemctl stop openstack-nova-${svc}.service > /dev/null 2>&1 || :
    done
fi
%preun console
if [ $1 -eq 0 ] ; then
    for svc in console consoleauth xvpvncproxy; do
        /bin/systemctl --no-reload disable openstack-nova-${svc}.service > /dev/null 2>&1 || :
        /bin/systemctl stop openstack-nova-${svc}.service > /dev/null 2>&1 || :
    done
fi

%postun compute
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in compute; do
        /bin/systemctl try-restart openstack-nova-${svc}.service >/dev/null 2>&1 || :
    done
fi
%postun network
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in network; do
        /bin/systemctl try-restart openstack-nova-${svc}.service >/dev/null 2>&1 || :
    done
fi
%postun volume
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in volume; do
        /bin/systemctl try-restart openstack-nova-${svc}.service >/dev/null 2>&1 || :
    done
fi
%postun scheduler
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in scheduler; do
        /bin/systemctl try-restart openstack-nova-${svc}.service >/dev/null 2>&1 || :
    done
fi
%postun cert
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in cert; do
        /bin/systemctl try-restart openstack-nova-${svc}.service >/dev/null 2>&1 || :
    done
fi
%postun api
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in api metadata-api; do
        /bin/systemctl try-restart openstack-nova-${svc}.service >/dev/null 2>&1 || :
    done
fi
%postun objectstore
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in objectstore; do
        /bin/systemctl try-restart openstack-nova-${svc}.service >/dev/null 2>&1 || :
    done
fi
%postun console
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in console consoleauth xvpvncproxy; do
        /bin/systemctl try-restart openstack-nova-${svc}.service >/dev/null 2>&1 || :
    done
fi

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
%config(noreplace) %{_sysconfdir}/logrotate.d/openstack-nova
%config(noreplace) %{_sysconfdir}/sudoers.d/nova
%config(noreplace) %{_sysconfdir}/polkit-1/localauthority/50-local.d/50-nova.pkla

%dir %attr(0755, nova, root) %{_localstatedir}/log/nova
%dir %attr(0755, nova, root) %{_localstatedir}/run/nova

%{_bindir}/nova-clear-rabbit-queues
# TODO. zmq-receiver may need its own service?
%{_bindir}/nova-rpc-zmq-receiver
%{_bindir}/nova-manage
%{_bindir}/nova-rootwrap

%{_datadir}/nova
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
%{_unitdir}/openstack-nova-compute.service
%{_datadir}/nova/rootwrap/compute.filters

%files network
%{_bindir}/nova-network
%{_bindir}/nova-dhcpbridge
%{_unitdir}/openstack-nova-network.service
%{_datadir}/nova/rootwrap/network.filters

%files volume
%{_bindir}/nova-volume
%{_bindir}/nova-volume-usage-audit
%{_unitdir}/openstack-nova-volume.service
%{_datadir}/nova/rootwrap/volume.filters

%files scheduler
%{_bindir}/nova-scheduler
%{_unitdir}/openstack-nova-scheduler.service

%files cert
%{_bindir}/nova-cert
%{_unitdir}/openstack-nova-cert.service
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
%{_unitdir}/openstack-nova-*api.service
%{_datadir}/nova/rootwrap/api-metadata.filters

%files objectstore
%{_bindir}/nova-objectstore
%{_unitdir}/openstack-nova-objectstore.service

%files console
%{_bindir}/nova-console*
%{_bindir}/nova-xvpvncproxy
%{_unitdir}/openstack-nova-console*.service
%{_unitdir}/openstack-nova-xvpvncproxy.service

%files -n python-module-nova
%defattr(-,root,root,-)
%doc LICENSE
%{python_sitelibdir}/nova
%{python_sitelibdir}/nova-*.egg-info

%files doc
%doc LICENSE doc/build/html

%changelog
* Thu Sep 27 2012 Pavel Shilovsky <piastry@altlinux.org> 2012.2.0.7-alt1
- Initial release for Sisyphus (based on Fedora)
