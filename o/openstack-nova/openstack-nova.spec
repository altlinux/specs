%define oname nova

%def_disable doc

Name: openstack-%oname
Version: 18.1.0
Release: alt1
Epoch: 1
Summary: OpenStack Compute (nova)

Group: System/Servers
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

Source6: nova.logrotate

Source3: %name.tmpfiles

Source10: %name-api.service
Source12: %name-compute.service
Source13: %name-network.service
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
Source32: %name-api-os-compute.service
Source33: %name-placement-api.service

Source110: %name-api.init
Source112: %name-compute.init
Source113: %name-network.init
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
Source132: %name-api-os-compute.init
Source133: %name-placement-api.init


Source21: nova-polkit.pkla
Source23: nova-polkit.rules
Source22: nova-ifc-template
Source24: nova-sudoers
Source30: %name-novncproxy.sysconfig

BuildArch: noarch
# /proc need for generate sample config fix "nova.cmd.novncproxy: [Errno 2] No such file or directory: '/proc/stat'"
BuildRequires: /proc
BuildRequires: crudini
BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-SQLAlchemy >= 1.0.10
BuildRequires: python-module-decorator >= 3.4.0
BuildRequires: python-module-eventlet >= 0.18.2
BuildRequires: python-module-jinja2 >= 2.10
BuildRequires: python-module-keystonemiddleware >= 4.17.0
BuildRequires: python-module-lxml >= 3.4.1
BuildRequires: python-module-routes >= 2.3.1
BuildRequires: python-module-cryptography >= 2.1
BuildRequires: python-module-webob >= 1.8.2
BuildRequires: python-module-greenlet >= 0.4.10
BuildRequires: python-module-PasteDeploy >= 1.5.0
BuildRequires: python-module-paste >= 2.0.2
BuildRequires: python-module-prettytable >= 0.7.1
BuildRequires: python-module-migrate >= 0.11.0
BuildRequires: python-module-numpy
BuildRequires: python-module-netaddr >= 0.7.18
BuildRequires: python-module-netifaces >= 0.10.4
BuildRequires: python-module-paramiko >= 2.0.0
BuildRequires: python-module-babel >= 2.3.4
BuildRequires: python-module-enum34 >= 1.0.4
BuildRequires: python-module-iso8601 >= 0.1.11
BuildRequires: python-module-jsonschema >= 2.6.0
BuildRequires: python-module-cinderclient >= 3.3.0
BuildRequires: python-module-keystoneauth1 >= 3.9.0
BuildRequires: python-module-neutronclient >= 6.7.0
BuildRequires: python-module-glanceclient >= 2.8.0
BuildRequires: python-module-requests >= 2.14.2
BuildRequires: python-module-stevedore >= 1.20.0
BuildRequires: python-module-websockify >= 0.8.0
BuildRequires: python-module-oslo.cache >= 1.26.0
BuildRequires: python-module-oslo.concurrency >= 3.26.0
BuildRequires: python-module-oslo.config >= 6.1.0
BuildRequires: python-module-oslo.context >= 2.19.2
BuildRequires: python-module-oslo.log >= 3.36.0
BuildRequires: python-module-oslo.reports >= 1.18.0
BuildRequires: python-module-oslo.serialization >= 2.18.0
BuildRequires: python-module-oslo.utils >= 3.33.0
BuildRequires: python-module-oslo.db >= 4.27.0
BuildRequires: python-module-oslo.rootwrap >= 5.8.0
BuildRequires: python-module-oslo.messaging >= 6.3.0
BuildRequires: python-module-oslo.policy >= 1.35.0
BuildRequires: python-module-oslo.privsep >= 1.23.0
BuildRequires: python-module-oslo.i18n >= 3.15.3
BuildRequires: python-module-oslo.service >= 1.24.0
BuildRequires: python-module-rfc3986 >= 0.3.1
BuildRequires: python-module-oslo.middleware >= 3.31.0
BuildRequires: python-module-psutil >= 3.2.2
BuildRequires: python-module-oslo.versionedobjects >= 1.31.2
BuildRequires: python-module-os-brick >= 2.5.0
BuildRequires: python-module-os-traits >= 0.4.0
BuildRequires: python-module-os-vif >= 1.7.0
BuildRequires: python-module-os-win >= 3.0.0
BuildRequires: python-module-castellan >= 0.16.0
BuildRequires: python-module-microversion-parse >= 0.2.1
BuildRequires: python-module-os-xenapi >= 0.3.3
BuildRequires: python-module-tooz >= 1.58.0
BuildRequires: python-module-cursive >= 0.2.1
BuildRequires: python-module-retrying >= 1.3.3
BuildRequires: python-module-pypowervm >= 1.1.15
BuildRequires: python-module-os-service-types >= 1.2.0
BuildRequires: python-module-taskflow >= 2.16.0
BuildRequires: python-module-dateutil >= 2.5.3
BuildRequires: python-module-zVMCloudConnector >= 1.1.1
BuildRequires: python-module-futures >= 3.0.0

BuildRequires: python-module-barbicanclient
BuildRequires: python-module-oslo.vmware >= 2.17.0

%if_enabled doc
# Required to build module documents
BuildRequires: python-module-sphinx >= 1.6.2
BuildRequires: python-module-sphinxcontrib-actdiag >= 0.8.5
BuildRequires: python-module-sphinxcontrib-seqdiag >= 0.8.4
BuildRequires: python-module-sphinx-feature-classification >= 0.2.0
BuildRequires: python-module-os-api-ref >= 1.4.0
BuildRequires: python-module-openstackdocstheme >= 1.19.0
BuildRequires: python-module-reno >= 2.5.0
%endif

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-SQLAlchemy >= 1.0.10
BuildRequires: python3-module-decorator >= 3.4.0
BuildRequires: python3-module-eventlet >= 0.18.2
BuildRequires: python3-module-jinja2 >= 2.10
BuildRequires: python3-module-keystonemiddleware >= 4.17.0
BuildRequires: python3-module-lxml >= 3.4.1
BuildRequires: python3-module-routes >= 2.3.1
BuildRequires: python3-module-cryptography >= 2.1
BuildRequires: python3-module-webob >= 1.8.2
BuildRequires: python3-module-greenlet >= 0.4.10
BuildRequires: python3-module-PasteDeploy >= 1.5.0
BuildRequires: python3-module-paste >= 2.0.2
BuildRequires: python3-module-prettytable >= 0.7.1
BuildRequires: python3-module-migrate >= 0.11.0
BuildRequires: python3-module-numpy
BuildRequires: python3-module-netaddr >= 0.7.18
BuildRequires: python3-module-netifaces >= 0.10.4
BuildRequires: python3-module-paramiko >= 2.0.0
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-iso8601 >= 0.1.11
BuildRequires: python3-module-jsonschema >= 2.6.0
BuildRequires: python3-module-cinderclient >= 3.3.0
BuildRequires: python3-module-keystoneauth1 >= 3.9.0
BuildRequires: python3-module-neutronclient >= 6.7.0
BuildRequires: python3-module-glanceclient >= 2.8.0
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-websockify >= 0.8.0
BuildRequires: python3-module-oslo.cache >= 1.26.0
BuildRequires: python3-module-oslo.concurrency >= 3.26.0
BuildRequires: python3-module-oslo.config >= 6.1.0
BuildRequires: python3-module-oslo.context >= 2.19.2
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.reports >= 1.18.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-oslo.db >= 4.27.0
BuildRequires: python3-module-oslo.rootwrap >= 5.8.0
BuildRequires: python3-module-oslo.messaging >= 6.3.0
BuildRequires: python3-module-oslo.policy >= 1.35.0
BuildRequires: python3-module-oslo.privsep >= 1.23.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.service >= 1.24.0
BuildRequires: python3-module-rfc3986 >= 0.3.1
BuildRequires: python3-module-oslo.middleware >= 3.31.0
BuildRequires: python3-module-psutil >= 3.2.2
BuildRequires: python3-module-oslo.versionedobjects >= 1.31.2
BuildRequires: python3-module-os-brick >= 2.5.0
BuildRequires: python3-module-os-traits >= 0.4.0
BuildRequires: python3-module-os-vif >= 1.7.0
BuildRequires: python3-module-os-win >= 3.0.0
BuildRequires: python3-module-castellan >= 0.16.0
BuildRequires: python3-module-microversion-parse >= 0.2.1
BuildRequires: python3-module-os-xenapi >= 0.3.3
BuildRequires: python3-module-tooz >= 1.58.0
BuildRequires: python3-module-cursive >= 0.2.1
BuildRequires: python3-module-retrying >= 1.3.3
BuildRequires: python3-module-pypowervm >= 1.1.15
BuildRequires: python3-module-os-service-types >= 1.2.0
BuildRequires: python3-module-taskflow >= 2.16.0
BuildRequires: python3-module-dateutil >= 2.5.3
BuildRequires: python3-module-zVMCloudConnector >= 1.1.1

BuildRequires: python3-module-barbicanclient
BuildRequires: python3-module-oslo.vmware >= 2.17.0

%if_enabled doc
# Required to build module documents
BuildRequires: python3-module-sphinx >= 1.6.2
BuildRequires: python3-module-sphinxcontrib-actdiag >= 0.8.5
BuildRequires: python3-module-sphinxcontrib-seqdiag >= 0.8.4
BuildRequires: python3-module-sphinx-feature-classification >= 0.2.0
BuildRequires: python3-module-os-api-ref >= 1.4.0
BuildRequires: python3-module-openstackdocstheme >= 1.19.0
BuildRequires: python3-module-reno >= 2.5.0
%endif

BuildRequires: graphviz

Requires: %name-compute = %EVR
Requires: %name-scheduler = %EVR
Requires: %name-api = %EVR
Requires: %name-network = %EVR
Requires: %name-conductor = %EVR
Requires: %name-console = %EVR
Requires: %name-cells = %EVR
Requires: %name-novncproxy = %EVR

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

Requires: python3-module-nova = %EVR
Requires: python3-module-oslo.rootwrap >= 5.0.0
Requires: python3-module-oslo.messaging >= 5.14.0
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

Requires: openstack-nova-common = %EVR
Requires: curl
Requires: open-iscsi
Requires: iptables iptables-ipv6
Requires: ipmitool
Requires: python3-module-libvirt libvirt-kvm
Requires: openssh-clients
Requires: rsync
Requires: lvm2
Requires: python3-module-cinderclient
Requires(pre): qemu-kvm
Requires: genisoimage
Requires: bridge-utils
Requires: sysfsutils
Requires: guestfs-data python3-module-libguestfs libguestfs-tools
Requires: polkit

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

Requires: openstack-nova-common = %EVR
Requires: radvd
Requires: bridge-utils
Requires: dnsmasq
Requires: dnsmasq-utils
Requires: ebtables iptables
Requires: conntrack-tools

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

Requires: openstack-nova-common = %EVR

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

%package api
Summary: OpenStack Nova API services
Group: System/Servers

Requires: openstack-nova-common = %EVR

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

Requires: openstack-nova-common = %EVR

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


%package console
Summary: OpenStack Nova console access services
Group: System/Servers

Requires: openstack-nova-common = %EVR
Requires: python3-module-websockify

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

Requires: openstack-nova-common = %EVR

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

Requires: openstack-nova-common = %EVR
Requires: novnc
Requires: python3-module-websockify

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

%package placement-api
Summary: OpenStack Nova Placement Service
Group: System/Servers
Requires: openstack-nova-common = %EVR

%description placement-api
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova Placement API Service.

%package spicehtml5proxy
Summary: OpenStack Nova Spice HTML5 console access service
Group: System/Servers

Requires: openstack-nova-common = %EVR
Requires: python3-module-websockify
Requires: spice-html5

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

Requires: openstack-nova-common = %EVR
Requires: python3-module-websockify

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

%package -n python-module-%oname
Summary: Nova Python libraries
Group: Development/Python

Requires: openssl
# Require openssh for ssh-keygen
Requires: openssh-common
Requires: sudo

Requires: python-module-SQLAlchemy
Requires: python-module-PasteDeploy

%description -n python-module-%oname
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform.

This package contains the nova Python library.

%package -n python-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python

%description -n python-module-%oname-tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Nova Python3 libraries
Group: Development/Python3

Requires: openssl
# Require openssh for ssh-keygen
Requires: openssh-common
Requires: sudo

Requires: python3-module-SQLAlchemy
Requires: python3-module-PasteDeploy

%description -n python3-module-%oname
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform.

This package contains the nova Python library.


%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack Compute
Group: Documentation

%description doc
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform.

This package contains documentation files for nova.

%prep
%setup -n %oname-%version

find . \( -name .gitignore -o -name .placeholder \) -delete

find nova -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

# Remove the requirements file so that pbr hooks don't add it
# to distutils requiers_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires


rm -rf ../python3
cp -a . ../python3

%build
%python_build

%if_enabled doc
export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b man doc/source doc/build/man
sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

oslo-config-generator --config-file=etc/nova/nova-config-generator.conf
oslopolicy-sample-generator --config-file=etc/nova/nova-policy-generator.conf

pushd ../python3
%python3_build
popd

%install
%python_install

for f in $(ls -1 %buildroot%_bindir)
    do mv %buildroot%_bindir/$f %buildroot%_bindir/$f.py2
done

pushd ../python3
%python3_install
popd

%if_enabled doc
mkdir -p %buildroot%_man1dir
install -p -D -m 644 doc/build/man/*.1 %buildroot%_man1dir/
%endif

# Setup directories
install -d -m 755 %buildroot%_sharedstatedir/nova
install -d -m 755 %buildroot%_sharedstatedir/nova/buckets
install -d -m 755 %buildroot%_sharedstatedir/nova/instances
install -d -m 755 %buildroot%_sharedstatedir/nova/keys
install -d -m 755 %buildroot%_sharedstatedir/nova/networks
install -d -m 755 %buildroot%_sharedstatedir/nova/tmp
install -d -m 770 %buildroot%_logdir/nova
install -d -m 750 %buildroot%_cachedir/nova

# Install config files
install -d -m 755 %buildroot%_sysconfdir/nova
install -d -m 755 %buildroot%_sysconfdir/nova/nova.conf.d
install -p -D -m 640 etc/nova/nova.conf.sample  %buildroot%_sysconfdir/nova/nova.conf
install -p -D -m 640 etc/nova/rootwrap.conf %buildroot%_sysconfdir/nova/
install -p -D -m 640 etc/nova/api-paste.ini %buildroot%_sysconfdir/nova/
install -p -D -m 640 etc/nova/policy.yaml.sample %buildroot%_sysconfdir/nova/policy.yaml
mkdir -p %buildroot%_sysconfdir/nova/rootwrap.d/
install -p -D -m 644 etc/nova/rootwrap.d/* %buildroot%_sysconfdir/nova/rootwrap.d/

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
install -p -D -m 644 %SOURCE10 %buildroot%_unitdir/%name-api.service
install -p -D -m 644 %SOURCE12 %buildroot%_unitdir/%name-compute.service
install -p -D -m 644 %SOURCE13 %buildroot%_unitdir/%name-network.service
install -p -D -m 644 %SOURCE15 %buildroot%_unitdir/%name-scheduler.service
install -p -D -m 644 %SOURCE18 %buildroot%_unitdir/%name-xvpvncproxy.service
install -p -D -m 644 %SOURCE19 %buildroot%_unitdir/%name-console.service
install -p -D -m 644 %SOURCE20 %buildroot%_unitdir/%name-consoleauth.service
install -p -D -m 644 %SOURCE25 %buildroot%_unitdir/%name-metadata-api.service
install -p -D -m 644 %SOURCE26 %buildroot%_unitdir/%name-conductor.service
install -p -D -m 644 %SOURCE27 %buildroot%_unitdir/%name-cells.service
install -p -D -m 644 %SOURCE28 %buildroot%_unitdir/%name-spicehtml5proxy.service
install -p -D -m 644 %SOURCE29 %buildroot%_unitdir/%name-novncproxy.service
install -p -D -m 644 %SOURCE31 %buildroot%_unitdir/%name-serialproxy.service
install -p -D -m 644 %SOURCE32 %buildroot%_unitdir/%name-api-os-compute.service
install -p -D -m 644 %SOURCE33 %buildroot%_unitdir/%name-placement-api.service

# Install init scripts
install -p -D -m 755 %SOURCE110 %buildroot%_initdir/%name-api
install -p -D -m 755 %SOURCE112 %buildroot%_initdir/%name-compute
install -p -D -m 755 %SOURCE113 %buildroot%_initdir/%name-network
install -p -D -m 755 %SOURCE115 %buildroot%_initdir/%name-scheduler
install -p -D -m 755 %SOURCE118 %buildroot%_initdir/%name-xvpvncproxy
install -p -D -m 755 %SOURCE119 %buildroot%_initdir/%name-console
install -p -D -m 755 %SOURCE120 %buildroot%_initdir/%name-consoleauth
install -p -D -m 755 %SOURCE125 %buildroot%_initdir/%name-metadata-api
install -p -D -m 755 %SOURCE126 %buildroot%_initdir/%name-conductor
install -p -D -m 755 %SOURCE127 %buildroot%_initdir/%name-cells
install -p -D -m 755 %SOURCE128 %buildroot%_initdir/%name-spicehtml5proxy
install -p -D -m 755 %SOURCE129 %buildroot%_initdir/%name-novncproxy
install -p -D -m 755 %SOURCE131 %buildroot%_initdir/%name-serialproxy
install -p -D -m 755 %SOURCE132 %buildroot%_initdir/%name-api-os-compute
install -p -D -m 755 %SOURCE133 %buildroot%_initdir/%name-placement-api

# Install sudoers
install -p -D -m 400 %SOURCE24 %buildroot%_sysconfdir/sudoers.d/nova

# Install logrotate
install -p -D -m 644 %SOURCE6 %buildroot%_sysconfdir/logrotate.d/openstack-nova

# Install pid directory
install -d -m 755 %buildroot%_runtimedir/nova

# Install template files
install -p -D -m 644 %SOURCE22 %buildroot%_datadir/nova/interfaces.template


# Install policy-kit rules to allow nova user to manage libvirt
install -p -D -m 644 %SOURCE23 %buildroot%_sysconfdir/polkit-1/rules.d/50-nova.rules

# Install novncproxy service options template
install -d %buildroot%_sysconfdir/sysconfig
install -p -m 0644 %SOURCE30 %buildroot%_sysconfdir/sysconfig/openstack-nova-novncproxy

# Remove unneeded in production stuff
rm -f %buildroot%_bindir/nova-debug
rm -f %buildroot%_bindir/nova-combined
rm -f %buildroot/usr/share/doc/nova/README*

### set default configuration (mostly applies to package-only setups and quickstart, i.e. not generally crowbar)
%define nova_conf %buildroot%_sysconfdir/nova/nova.conf.d/010-nova.conf
crudini --set %nova_conf DEFAULT log_dir /var/log/nova
crudini --set %nova_conf DEFAULT state_path /var/lib/nova
crudini --set %nova_conf oslo_concurrency lock_path %_runtimedir/nova

# cleanup
rm -rf %buildroot/usr/etc/nova

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

%post api
%post_service %name-api
%post_service %name-metadata-api
%post_service %name-api-os-compute

%preun api
%preun_service %name-api
%preun_service %name-metadata-api
%preun_service %name-api-os-compute

%post conductor
%post_service %name-conductor
%preun conductor
%preun_service %name-conductor

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

%post placement-api
%post_service %name-placement-api
%preun placement-api
%preun_service %name-placement-api

%post spicehtml5proxy
%post_service %name-spicehtml5proxy
%preun spicehtml5proxy
%preun_service %name-spicehtml5proxy

%post serialproxy
%post_service %name-serialproxy
%preun serialproxy
%preun_service %name-serialproxy

%files

%files common
%doc LICENSE
%dir %_sysconfdir/nova
%dir %_sysconfdir/nova/nova.conf.d
%_sysconfdir/nova/release
%config(noreplace) %attr(0640, root, nova) %_sysconfdir/nova/nova.conf
%config(noreplace) %attr(0640, root, nova) %_sysconfdir/nova/nova.conf.d/010-nova.conf
%config(noreplace) %attr(0640, root, nova) %_sysconfdir/nova/api-paste.ini
%config %_sysconfdir/nova/rootwrap.conf
%dir %_sysconfdir/nova/rootwrap.d
%config %attr(0640, root, nova) %_sysconfdir/nova/policy.yaml
%config(noreplace) %_sysconfdir/logrotate.d/%name
%config(noreplace) %_sysconfdir/sudoers.d/nova
%config(noreplace) %_sysconfdir/polkit-1/rules.d/50-nova.rules

%_tmpfilesdir/%name.conf
%dir %attr(0770, root, nova) %_logdir/nova
%dir %attr(0775, root, nova) %_runtimedir/nova

%_datadir/nova
%if_enabled doc
%_man1dir/nova*.1.*
%endif

%defattr(-, nova, nova, -)
%dir %_sharedstatedir/nova
%dir %_sharedstatedir/nova/buckets
%dir %_sharedstatedir/nova/instances
%dir %_sharedstatedir/nova/keys
%dir %_sharedstatedir/nova/networks
%dir %_sharedstatedir/nova/tmp
%dir %_cachedir/nova

%files compute
%config %_sysconfdir/nova/rootwrap.d/compute.filters
%_unitdir/%name-compute.service
%_initdir/%name-compute

%files network
%config %_sysconfdir/nova/rootwrap.d/network.filters
%_unitdir/%name-network.service
%_initdir/%name-network


%files scheduler
%_unitdir/%name-scheduler.service
%_initdir/%name-scheduler

%files api
%config %_sysconfdir/nova/rootwrap.d/api-metadata.filters
%_initdir/%name-api
%_initdir/%name-metadata-api
%_initdir/%name-api-os-compute
%_unitdir/%name-api.service
%_unitdir/%name-metadata-api.service
%_unitdir/%name-api-os-compute.service

%files conductor
%_unitdir/%name-conductor.service
%_initdir/%name-conductor

%files console
%_unitdir/%name-console*.service
%_unitdir/%name-xvpvncproxy.service
%_initdir/%name-console*
%_initdir/%name-xvpvncproxy

%files cells
%_unitdir/%name-cells.service
%_initdir/%name-cells

%files novncproxy
%_unitdir/%name-novncproxy.service
%_initdir/%name-novncproxy
%config(noreplace) %_sysconfdir/sysconfig/openstack-nova-novncproxy

%files placement-api
%_unitdir/%name-placement-api.service
%_initdir/%name-placement-api

%files spicehtml5proxy
%_unitdir/%name-spicehtml5proxy.service
%_initdir/%name-spicehtml5proxy

%files serialproxy
%_unitdir/%name-serialproxy.service
%_initdir/%name-serialproxy

%files -n python-module-%oname
%doc LICENSE
%_bindir/nova*.py2
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/tests
%exclude %python_sitelibdir/%oname/test.*

%files -n python-module-%oname-tests
%python_sitelibdir/%oname/tests
%python_sitelibdir/%oname/test.*
%exclude %python_sitelibdir/%oname/tests/live_migration/hooks

%files -n python3-module-%oname
%doc LICENSE
%_bindir/*
%exclude %_bindir/nova*.py2
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/test.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests
%python3_sitelibdir/%oname/test.*
%exclude %python3_sitelibdir/%oname/tests/live_migration/hooks

%if_enabled doc
%files doc
%doc LICENSE doc/build/html
%endif

%changelog
* Wed Jan 09 2019 Alexey Shabalin <shaba@altlinux.org> 1:18.1.0-alt1
- 18.1.0 Rocky release

* Thu Jun 22 2017 Alexey Shabalin <shaba@altlinux.ru> 1:15.0.6-alt1
- 15.0.6
- drop signing_dir from default config

* Mon Jun 05 2017 Alexey Shabalin <shaba@altlinux.ru> 1:15.0.5-alt1
- 15.0.5 Ocata release

* Wed Apr 12 2017 Alexey Shabalin <shaba@altlinux.ru> 1:14.0.5-alt1
- 14.0.5

* Fri Dec 30 2016 Alexey Shabalin <shaba@altlinux.ru> 1:14.0.3-alt1
- 14.0.3

* Tue Nov 22 2016 Alexey Shabalin <shaba@altlinux.ru> 1:14.0.2-alt2
- fix logrotate

* Wed Nov 09 2016 Alexey Shabalin <shaba@altlinux.ru> 1:14.0.2-alt1
- 14.0.2
- fix log dir permitions for logrotate

* Wed Oct 26 2016 Alexey Shabalin <shaba@altlinux.ru> 1:14.0.1-alt2
- delete Requires: python-module-ldap

* Fri Oct 21 2016 Alexey Shabalin <shaba@altlinux.ru> 1:14.0.1-alt1
- 14.0.1 Newton release

* Thu Apr 14 2016 Alexey Shabalin <shaba@altlinux.ru> 1:13.0.0-alt1
- 13.0.0 Mitaka release

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 1:12.0.2-alt1
- 12.0.2

* Tue Nov 24 2015 Alexey Shabalin <shaba@altlinux.ru> 1:12.0.0-alt2
- add patch for fix attibute error when cloning raw images in Ceph

* Fri Oct 30 2015 Alexey Shabalin <shaba@altlinux.ru> 1:12.0.0-alt1
- 12.0.0 Liberty Release

* Thu Oct 15 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.2-alt1
- 2015.1.2

* Thu Sep 24 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.1-alt4
- update BR: for fix generate sample config file
- drop dist configs in /usr/share

* Mon Sep 21 2015 Lenar Shakirov <snejok@altlinux.ru> 2015.1.1-alt3
- Added Requires: polkit

* Tue Sep 15 2015 Lenar Shakirov <snejok@altlinux.ru> 2015.1.1-alt2
- Added Requires: python-module-{ldap,SQLAlchemy,PasteDeploy}

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
