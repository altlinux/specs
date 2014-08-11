%global release_name icehouse

Name:		openstack-neutron
Version:	2014.1.2
Release:	alt1
Provides:	openstack-quantum = %{version}-%{release}
Obsoletes:	openstack-quantum < 2013.2-0.4.b3
Summary:	OpenStack Networking Service

Group:		System/Servers
License:	ASL 2.0
URL:		http://launchpad.net/neutron/

Source0:	%{name}-%{version}.tar
Source1:	neutron.logrotate
Source2:	neutron-sudoers
Source10:	neutron-server.service
Source11:	neutron-linuxbridge-agent.service
Source12:	neutron-openvswitch-agent.service
Source13:	neutron-ryu-agent.service
Source14:	neutron-nec-agent.service
Source15:	neutron-dhcp-agent.service
Source16:	neutron-l3-agent.service
Source17:	neutron-metadata-agent.service
Source18:	neutron-ovs-cleanup.service
Source19:	neutron-lbaas-agent.service
Source20:	neutron-mlnx-agent.service
Source21:	neutron-vpn-agent.service
Source22:	neutron-metering-agent.service

Source30:	neutron-dist.conf
#
# patches_base=2014.1.2
#
Patch0001: 0001-remove-runtime-dependency-on-pbr.patch
Patch0002: 0002-Sync-service-and-systemd-modules-from-oslo-incubator.patch
Patch0003: 0003-Removed-signing_dir-from-neutron.conf.patch
Patch0004: 0004-Remove-kernel-version-check-for-OVS-VXLAN.patch
Patch0005: 0005-Notify-systemd-when-starting-Neutron-server.patch
Patch0101: 0101-fix-neutron-configuration.patch

BuildArch:	noarch

BuildRequires:	python-devel
BuildRequires:	python-module-setuptools
BuildRequires:  python-module-pbr
BuildRequires:  python-module-d2to1

Requires:	python-module-neutron = %{version}-%{release}
Requires:	python-module-oslo-rootwrap
Requires:	openstack-utils

# dnsmasq is not a hard requirement, but is currently the only option
# when neutron-dhcp-agent is deployed.
Requires:	dnsmasq
Requires:	dnsmasq-utils

Requires(pre):	shadow-utils

%description
Neutron is a virtual network service for Openstack. Just like
OpenStack Nova provides an API to dynamically request and configure
virtual servers, Neutron provides an API to dynamically request and
configure virtual networks. These networks connect "interfaces" from
other OpenStack services (e.g., virtual NICs from Nova VMs). The
Neutron API supports extensions to provide advanced network
capabilities (e.g., QoS, ACLs, network monitoring, etc.)


%package -n python-module-neutron
Summary:	Neutron Python libraries
Group:          Development/Python

Provides:	python-module-quantum = %{version}-%{release}
Obsoletes:	python-module-quantum < 2013.2-0.4.b3

Requires:	python-module-MySQLdb
Requires:	python-module-alembic
Requires:	python-module-amqplib
Requires:	python-module-anyjson
Requires:	python-module-babel
Requires:	python-module-eventlet
Requires:	python-module-greenlet
Requires:	python-module-httplib2 >= 0.7.5
Requires:	python-module-iso8601
Requires:	python-module-keystoneclient >= 0.7.0
Requires:	python-module-kombu
Requires:	python-module-lxml
Requires:	python-module-netaddr
Requires:	python-module-oslo-config >= 1.2.0
Requires:	python-module-PasteDeploy
Requires:	python-module-qpid
Requires:	python-module-neutronclient >= 2.3.4
Requires:	python-module-routes
Requires:	python-module-SQLAlchemy >= 0.7.8
Requires:	python-module-webob >= 1.2.3
Requires:	python-module-stevedore
Requires:	python-module-six >= 1.4.1
# requires.txt asks for six >= 1.5.2 actually
Requires:	python-module-novaclient >= 2.17.0
Requires:	sudo



%description -n python-module-neutron
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron Python library.


%package bigswitch
Summary:	Neutron Big Switch plugin
Group:          Development/Python

Provides:	openstack-quantum-bigswitch = %{version}-%{release}
Obsoletes:	openstack-quantum-bigswitch < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}


%description bigswitch
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using the FloodLight Openflow Controller or the Big Switch
Networks Controller.


%package brocade
Summary:	Neutron Brocade plugin
Group:          Development/Python

AutoReq: yes, nopython

Provides:	openstack-quantum-brocade = %{version}-%{release}
Obsoletes:	openstack-quantum-brocade < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}


%description brocade
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using Brocade VCS switches running NOS.


%package cisco
Summary:	Neutron Cisco plugin
Group:          Development/Python

Provides:	openstack-quantum-cisco = %{version}-%{release}
Obsoletes:	openstack-quantum-cisco < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}
Requires:	python-module-configobj


%description cisco
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using Cisco UCS and Nexus.


%package hyperv
Summary:	Neutron Hyper-V plugin
Group:          Development/Python

Provides:	openstack-quantum-hyperv = %{version}-%{release}
Obsoletes:	openstack-quantum-hyperv < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}


%description hyperv
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using Microsoft Hyper-V.


%package ibm
Summary:       Neutron IBM plugin
Group:          Development/Python

Requires:      openstack-neutron = %{version}-%{release}


%description ibm
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks from IBM.


%package linuxbridge
Summary:	Neutron linuxbridge plugin
Group:          Development/Python

Provides:	openstack-quantum-linuxbridge = %{version}-%{release}
Obsoletes:	openstack-quantum-linuxbridge < 2013.2-0.4.b3

Requires:	bridge-utils
Requires:	openstack-neutron = %{version}-%{release}


%description linuxbridge
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks as VLANs using Linux bridging.


%package midonet
Summary:	Neutron MidoNet plugin
Group:          Development/Python

AutoReq: yes, nopython

Provides:	openstack-quantum-midonet = %{version}-%{release}
Obsoletes:	openstack-quantum-midonet < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}


%description midonet
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using MidoNet from Midokura.


%package ml2
Summary:    Neutron ML2 plugin
Group:          Development/Python

Provides:	openstack-quantum-ml2 = %{version}-%{release}
Obsoletes:	openstack-quantum-ml2 < 2013.2-0.4.b3

Requires:   openstack-neutron = %{version}-%{release}


%description ml2
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains a neutron plugin that allows the use of drivers
to support separately extensible sets of network types and the mechanisms
for accessing those types.


%package mellanox
Summary:    Neutron Mellanox plugin
Group:          Development/Python

Provides:	openstack-quantum-mellanox = %{version}-%{release}
Obsoletes:	openstack-quantum-mellanox < 2013.2-0.4.b3

Requires:      openstack-neutron = %{version}-%{release}


%description mellanox
This plugin implements Neutron v2 APIs with support for Mellanox embedded
switch functionality as part of the VPI (Ethernet/InfiniBand) HCA.


%package nuage
Summary:    Neutron Nuage plugin
Group:          Development/Python

Requires:   openstack-neutron = %{version}-%{release}


%description nuage
This plugin implements Neutron v2 APIs with support for Nuage Networks
Virtual Service Platform (VSP).


%package ofagent
Summary:       Neutron ofagent plugin from ryu project
Group:          Development/Python

AutoReq: yes, nopython

Requires:      openstack-neutron = %{version}-%{release}


%description ofagent
This plugin implements Neutron v2 APIs with support for the ryu ofagent
plugin.


%package vmware
Summary:	Neutron Nicira plugin
Group:          Development/Python

Provides:	openstack-quantum-nicira = %{version}-%{release}
Obsoletes:	openstack-quantum-nicira < 2013.2-0.4.b3
Provides:	openstack-neutron-nicira = %{version}-%{release}
Obsoletes:	openstack-neutron-nicira < 2014.1-0.5.b2

Requires:	openstack-neutron = %{version}-%{release}


%description vmware
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using VMware NSX.


%package oneconvergence-nvsd
Summary:	Neutron One Convergence NVSD plugin
Group:          Development/Python

Requires:	openstack-neutron = %{version}-%{release}


%description oneconvergence-nvsd
Neutron provides an API to dynamnically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using One Convergence NVSD


%package openvswitch
Summary:	Neutron openvswitch plugin
Group:          Development/Python

Requires:	openstack-neutron = %{version}-%{release}
Requires:	openvswitch


%description openvswitch
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using Open vSwitch.


%package plumgrid
Summary:	Neutron PLUMgrid plugin
Group:          Development/Python

AutoReq: yes, nopython

Provides:	openstack-quantum-plumgrid = %{version}-%{release}
Obsoletes:	openstack-quantum-plumgrid < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}


%description plumgrid
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using the PLUMgrid platform.


%package ryu
Summary:	Neutron Ryu plugin
Group:          Development/Python

Provides:	openstack-quantum-ryu = %{version}-%{release}
Obsoletes:	openstack-quantum-ryu < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}


%description ryu
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using the Ryu Network Operating System.


%package nec
Summary:	Neutron NEC plugin
Group:          Development/Python

Provides:	openstack-quantum-nec = %{version}-%{release}
Obsoletes:	openstack-quantum-nec < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}


%description nec
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using the NEC OpenFlow controller.


%package metaplugin
Summary:	Neutron meta plugin
Group:          Development/Python

Provides:	openstack-quantum-metaplugin = %{version}-%{release}
Obsoletes:	openstack-quantum-metaplugin < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}


%description metaplugin
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using multiple other neutron plugins.


%package metering-agent
Summary:	Neutron bandwidth metering agent
Group:          Development/Python

Requires:   openstack-neutron = %{version}-%{release}

%description metering-agent
Neutron provides an API to measure bandwidth utilization

This package contains the neutron agent responsible for generating bandwidth
utilization notifications.


%package vpn-agent
Summary:	Neutron VPNaaS agent
Group:          Development/Python

Requires:	openstack-neutron = %{version}-%{release}
Requires:	python-module-jinja2

%description vpn-agent
Neutron provides an API to implement VPN as a service

This package contains the neutron agent responsible for implenting VPNaaS with
IPSec.


%prep
%setup

%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0101 -p1

find neutron -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

sed -i 's/RPMVERSION/%{version}/; s/RPMRELEASE/%{release}/' neutron/version.py

# Ensure SOURCES.txt ends in a newline and if any patches have added files, append them to SOURCES.txt
[ -n "$(tail -c 1 < neutron.egg-info/SOURCES.txt)" ] && echo >> neutron.egg-info/SOURCES.txt
if ls %{_sourcedir}/*.patch >/dev/null 2>&1; then
  awk '/^new file/ {split(a,files," ");print substr(files[3],3)} {a = $0}' %{_sourcedir}/*.patch >> neutron.egg-info/SOURCES.txt
fi

chmod 644 neutron/plugins/cisco/README

# Let's handle dependencies ourseleves
rm -f requirements.txt

#FIXME:
#Hack for ALT Autoreq mechanism:
# - python2.7(heleosapi) in embrane
# - python2.7(XenAPI) in agent/xenapi and bin/{quantum,neutron}-rootwrap-xen-dom0
# - python2.7(ncclient) in neutron/plugins/ml2/drivers/brocade
sed '/quantum-rootwrap-xen-dom0/d; /neutron-rootwrap-xen-dom0/d' -i setup.cfg neutron.egg-info/SOURCES.txt
rm -rfv neutron/plugins/embrane/ \
neutron/services/loadbalancer/drivers/embrane/ \
neutron/plugins/openvswitch/agent/xenapi \
bin/quantum-rootwrap-xen-dom0 \
bin/neutron-rootwrap-xen-dom0 \
neutron/plugins/ml2/drivers/brocade \
neutron/plugins/cisco/nexus \
neutron/plugins/ml2/drivers/cisco/nexus/

%build
%python_build

# Loop through values in neutron-dist.conf and make sure that the values
# are substituted into the neutron.conf as comments. Some of these values
# will have been uncommented as a way of upstream setting defaults outside
# of the code. For service_provider and notification-driver, there are
# commented examples above uncommented settings, so this specifically
# skips those comments and instead comments out the actual settings and
# substitutes the correct default values.
while read name eq value; do
  test "$name" && test "$value" || continue
  if [ "$name" = "service_provider" -o "$name" = "notification_driver" ]; then
    sed -ri "0,/^$name *=/{s!^$name *=.*!# $name = $value!}" etc/neutron.conf
  else
    sed -ri "0,/^(#)? *$name *=/{s!^(#)? *$name *=.*!# $name = $value!}" etc/neutron.conf
  fi
done < %{SOURCE30}

%install
%python_install

# Remove unused files
rm -rf %{buildroot}%{python_sitelibdir}/bin
rm -rf %{buildroot}%{python_sitelibdir}/doc
rm -rf %{buildroot}%{python_sitelibdir}/tools
rm -rf %{buildroot}%{python_sitelibdir}/neutron/tests
rm -rf %{buildroot}%{python_sitelibdir}/neutron/plugins/*/tests
rm -f %{buildroot}%{python_sitelibdir}/neutron/plugins/*/run_tests.*
rm %{buildroot}/usr/etc/init.d/neutron-server

# Move rootwrap files to proper location
install -d -m 755 %{buildroot}%{_datadir}/neutron/rootwrap
mv %{buildroot}/usr/etc/neutron/rootwrap.d/*.filters %{buildroot}%{_datadir}/neutron/rootwrap

# Move config files to proper location
install -d -m 755 %{buildroot}%{_sysconfdir}/neutron
mv %{buildroot}/usr/etc/neutron/* %{buildroot}%{_sysconfdir}/neutron
mv %{buildroot}%{_sysconfdir}/neutron/api-paste.ini %{buildroot}%{_datadir}/neutron/api-paste.ini
chmod 640  %{buildroot}%{_sysconfdir}/neutron/plugins/*/*.ini

# TODO: remove this once the plugin is separately packaged
rm %{buildroot}%{_sysconfdir}/neutron/plugins/embrane/heleos_conf.ini

# Install logrotate
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/openstack-neutron

# Install sudoers
install -p -D -m 400 %{SOURCE2} %{buildroot}%{_sysconfdir}/sudoers.d/neutron

# Install systemd units
install -p -D -m 644 %{SOURCE10} %{buildroot}%{_unitdir}/neutron-server.service
install -p -D -m 644 %{SOURCE11} %{buildroot}%{_unitdir}/neutron-linuxbridge-agent.service
install -p -D -m 644 %{SOURCE12} %{buildroot}%{_unitdir}/neutron-openvswitch-agent.service
install -p -D -m 644 %{SOURCE13} %{buildroot}%{_unitdir}/neutron-ryu-agent.service
install -p -D -m 644 %{SOURCE14} %{buildroot}%{_unitdir}/neutron-nec-agent.service
install -p -D -m 644 %{SOURCE15} %{buildroot}%{_unitdir}/neutron-dhcp-agent.service
install -p -D -m 644 %{SOURCE16} %{buildroot}%{_unitdir}/neutron-l3-agent.service
install -p -D -m 644 %{SOURCE17} %{buildroot}%{_unitdir}/neutron-metadata-agent.service
install -p -D -m 644 %{SOURCE18} %{buildroot}%{_unitdir}/neutron-ovs-cleanup.service
install -p -D -m 644 %{SOURCE19} %{buildroot}%{_unitdir}/neutron-lbaas-agent.service
install -p -D -m 644 %{SOURCE20} %{buildroot}%{_unitdir}/neutron-mlnx-agent.service
install -p -D -m 644 %{SOURCE21} %{buildroot}%{_unitdir}/neutron-vpn-agent.service
install -p -D -m 644 %{SOURCE22} %{buildroot}%{_unitdir}/neutron-metering-agent.service

# Setup directories
install -d -m 755 %{buildroot}%{_datadir}/neutron
install -d -m 755 %{buildroot}%{_sharedstatedir}/neutron
install -d -m 755 %{buildroot}%{_logdir}/neutron
install -d -m 755 %{buildroot}%{_runtimedir}/neutron

# Install dist conf
install -p -D -m 640 %{SOURCE30} %{buildroot}%{_datadir}/neutron/neutron-dist.conf

# Install version info file
cat > %{buildroot}%{_sysconfdir}/neutron/release <<EOF
[Neutron]
vendor = Fedora Project
product = OpenStack Neutron
package = %{release}
EOF

%pre
getent group neutron >/dev/null || groupadd -r neutron
getent passwd neutron >/dev/null || \
    useradd -r -g neutron -G neutron,wheel -d %{_sharedstatedir}/neutron -s /sbin/nologin \
    -c "OpenStack Neutron Daemons" neutron
exit 0


%post
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi


%preun
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable neutron-server.service > /dev/null 2>&1 || :
    /bin/systemctl stop neutron-server.service > /dev/null 2>&1 || :
    /bin/systemctl --no-reload disable neutron-dhcp-agent.service > /dev/null 2>&1 || :
    /bin/systemctl stop neutron-dhcp-agent.service > /dev/null 2>&1 || :
    /bin/systemctl --no-reload disable neutron-l3-agent.service > /dev/null 2>&1 || :
    /bin/systemctl stop neutron-l3-agent.service > /dev/null 2>&1 || :
    /bin/systemctl --no-reload disable neutron-metadata-agent.service > /dev/null 2>&1 || :
    /bin/systemctl stop neutron-metadata-agent.service > /dev/null 2>&1 || :
    /bin/systemctl --no-reload disable neutron-lbaas-agent.service > /dev/null 2>&1 || :
    /bin/systemctl stop neutron-lbaas-agent.service > /dev/null 2>&1 || :
fi


%postun
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart neutron-server.service >/dev/null 2>&1 || :
    /bin/systemctl try-restart neutron-dhcp-agent.service >/dev/null 2>&1 || :
    /bin/systemctl try-restart neutron-l3-agent.service >/dev/null 2>&1 || :
    /bin/systemctl try-restart neutron-metadata-agent.service >/dev/null 2>&1 || :
    /bin/systemctl try-restart neutron-lbaas-agent.service >/dev/null 2>&1 || :
fi


%preun linuxbridge
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable neutron-linuxbridge-agent.service > /dev/null 2>&1 || :
    /bin/systemctl stop neutron-linuxbridge-agent.service > /dev/null 2>&1 || :
fi


%postun linuxbridge
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart neutron-linuxbridge-agent.service >/dev/null 2>&1 || :
fi


%preun mellanox
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable neutron-mlnx-agent.service > /dev/null 2>&1 || :
    /bin/systemctl stop neutron-mlnx-agent.service > /dev/null 2>&1 || :
fi


%postun mellanox
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart neutron-mlnx-agent.service >/dev/null 2>&1 || :
fi


%preun openvswitch
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable neutron-openvswitch-agent.service > /dev/null 2>&1 || :
    /bin/systemctl stop neutron-openvswitch-agent.service > /dev/null 2>&1 || :
fi


%postun openvswitch
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart neutron-openvswitch-agent.service >/dev/null 2>&1 || :
fi


%preun ryu
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable neutron-ryu-agent.service > /dev/null 2>&1 || :
    /bin/systemctl stop neutron-ryu-agent.service > /dev/null 2>&1 || :
fi


%postun ryu
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart neutron-ryu-agent.service >/dev/null 2>&1 || :
fi


%preun nec
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable neutron-nec-agent.service > /dev/null 2>&1 || :
    /bin/systemctl stop neutron-nec-agent.service > /dev/null 2>&1 || :
fi


%postun nec
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart neutron-nec-agent.service >/dev/null 2>&1 || :
fi


%preun metering-agent
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable neutron-metering-agent.service > /dev/null 2>&1 || :
    /bin/systemctl stop neutron-metering-agent.service > /dev/null 2>&1 || :
fi


%postun metering-agent
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart neutron-metering-agent.service >/dev/null 2>&1 || :
fi


%preun vpn-agent
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable neutron-vpn-agent.service > /dev/null 2>&1 || :
    /bin/systemctl stop neutron-vpn-agent.service > /dev/null 2>&1 || :
fi


%postun vpn-agent
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart neutron-vpn-agent.service >/dev/null 2>&1 || :
fi


%files
%doc LICENSE
%doc README.rst
%{_bindir}/quantum-db-manage
%{_bindir}/quantum-debug
%{_bindir}/quantum-dhcp-agent
%{_bindir}/quantum-l3-agent
%{_bindir}/quantum-lbaas-agent
%{_bindir}/quantum-metadata-agent
%{_bindir}/quantum-netns-cleanup
%{_bindir}/quantum-ns-metadata-proxy
%{_bindir}/quantum-rootwrap
%{_bindir}/quantum-server
%{_bindir}/quantum-usage-audit

%{_bindir}/neutron-db-manage
%{_bindir}/neutron-debug
%{_bindir}/neutron-dhcp-agent
%{_bindir}/neutron-l3-agent
%{_bindir}/neutron-lbaas-agent
%{_bindir}/neutron-metadata-agent
%{_bindir}/neutron-netns-cleanup
%{_bindir}/neutron-ns-metadata-proxy
%{_bindir}/neutron-rootwrap
%{_bindir}/neutron-server
%{_bindir}/neutron-usage-audit

%{_unitdir}/neutron-dhcp-agent.service
%{_unitdir}/neutron-l3-agent.service
%{_unitdir}/neutron-lbaas-agent.service
%{_unitdir}/neutron-metadata-agent.service
%{_unitdir}/neutron-server.service
%dir %{_sysconfdir}/neutron
%{_sysconfdir}/neutron/release
%attr(-, root, neutron) %{_datadir}/neutron/neutron-dist.conf
%attr(-, root, neutron) %{_datadir}/neutron/api-paste.ini
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/dhcp_agent.ini
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/fwaas_driver.ini
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/l3_agent.ini
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/metadata_agent.ini
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/lbaas_agent.ini
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/policy.json
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/neutron.conf
%config(noreplace) %{_sysconfdir}/neutron/rootwrap.conf
%dir %{_sysconfdir}/neutron/plugins
%config(noreplace) %{_sysconfdir}/logrotate.d/*
%config(noreplace) %{_sysconfdir}/sudoers.d/neutron
%dir %attr(0755, neutron, neutron) %{_sharedstatedir}/neutron
%dir %attr(0755, neutron, neutron) %{_logdir}/neutron
%dir %{_datadir}/neutron
%dir %{_datadir}/neutron/rootwrap
%{_datadir}/neutron/rootwrap/debug.filters
%{_datadir}/neutron/rootwrap/dhcp.filters
%{_datadir}/neutron/rootwrap/iptables-firewall.filters
%{_datadir}/neutron/rootwrap/l3.filters
%{_datadir}/neutron/rootwrap/lbaas-haproxy.filters


%files -n python-module-neutron
%doc LICENSE
%doc README.rst
%{python_sitelibdir}/neutron
%{python_sitelibdir}/quantum
%exclude %{python_sitelibdir}/neutron/plugins/bigswitch
%exclude %{python_sitelibdir}/neutron/plugins/brocade
%exclude %{python_sitelibdir}/neutron/plugins/cisco
%exclude %{python_sitelibdir}/neutron/plugins/hyperv
%exclude %{python_sitelibdir}/neutron/plugins/ibm
%exclude %{python_sitelibdir}/neutron/plugins/linuxbridge
%exclude %{python_sitelibdir}/neutron/plugins/metaplugin
%exclude %{python_sitelibdir}/neutron/plugins/midonet
%exclude %{python_sitelibdir}/neutron/plugins/ml2
%exclude %{python_sitelibdir}/neutron/plugins/mlnx
%exclude %{python_sitelibdir}/neutron/plugins/nuage
%exclude %{python_sitelibdir}/neutron/plugins/nec
%exclude %{python_sitelibdir}/neutron/plugins/nicira
%exclude %{python_sitelibdir}/neutron/plugins/ofagent
%exclude %{python_sitelibdir}/neutron/plugins/oneconvergence
%exclude %{python_sitelibdir}/neutron/plugins/openvswitch
%exclude %{python_sitelibdir}/neutron/plugins/plumgrid
%exclude %{python_sitelibdir}/neutron/plugins/ryu
%exclude %{python_sitelibdir}/neutron/plugins/vmware
%{python_sitelibdir}/neutron-%%{version}*.egg-info


%files bigswitch
%doc LICENSE
%doc neutron/plugins/bigswitch/README
%{_bindir}/neutron-restproxy-agent
%{python_sitelibdir}/neutron/plugins/bigswitch
%dir %{_sysconfdir}/neutron/plugins/bigswitch
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/bigswitch/*.ini
%doc %{_sysconfdir}/neutron/plugins/bigswitch/README


%files brocade
%doc LICENSE
%doc neutron/plugins/brocade/README.md
%{python_sitelibdir}/neutron/plugins/brocade
%dir %{_sysconfdir}/neutron/plugins/brocade
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/brocade/*.ini


%files cisco
%doc LICENSE
%doc neutron/plugins/cisco/README
%{python_sitelibdir}/neutron/plugins/cisco
%dir %{_sysconfdir}/neutron/plugins/cisco
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/cisco/*.ini


%files hyperv
%doc LICENSE
#%%doc neutron/plugins/hyperv/README
%{_bindir}/neutron-hyperv-agent
%{_bindir}/quantum-hyperv-agent
%{python_sitelibdir}/neutron/plugins/hyperv
%dir %{_sysconfdir}/neutron/plugins/hyperv
%exclude %{python_sitelibdir}/neutron/plugins/hyperv/agent
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/hyperv/*.ini


%files ibm
%doc LICENSE
%{_bindir}/neutron-ibm-agent
%{_bindir}/quantum-ibm-agent
%doc neutron/plugins/ibm/README
%{python_sitelibdir}/neutron/plugins/ibm
%dir %{_sysconfdir}/neutron/plugins/ibm
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/ibm/*.ini


%files linuxbridge
%doc LICENSE
%doc neutron/plugins/linuxbridge/README
%{_bindir}/neutron-linuxbridge-agent
%{_bindir}/quantum-linuxbridge-agent
%{_unitdir}/neutron-linuxbridge-agent.service
%{python_sitelibdir}/neutron/plugins/linuxbridge
%{_datadir}/neutron/rootwrap/linuxbridge-plugin.filters
%dir %{_sysconfdir}/neutron/plugins/linuxbridge
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/linuxbridge/*.ini


%files midonet
%doc LICENSE
#%%doc neutron/plugins/midonet/README
%{python_sitelibdir}/neutron/plugins/midonet
%dir %{_sysconfdir}/neutron/plugins/midonet
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/midonet/*.ini


%files ml2
%doc LICENSE
%doc neutron/plugins/ml2/README
%{python_sitelibdir}/neutron/plugins/ml2
%dir %{_sysconfdir}/neutron/plugins/ml2
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/ml2/*.ini


%files mellanox
%doc LICENSE
%doc neutron/plugins/mlnx/README
%{_bindir}/neutron-mlnx-agent
%{_bindir}/quantum-mlnx-agent
%{_unitdir}/neutron-mlnx-agent.service
%{python_sitelibdir}/neutron/plugins/mlnx
%dir %{_sysconfdir}/neutron/plugins/mlnx
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/mlnx/*.ini

%files nuage
%doc LICENSE
%{python_sitelibdir}/neutron/plugins/nuage
%dir %{_sysconfdir}/neutron/plugins/nuage
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/nuage/*.ini

%files ofagent
%doc LICENSE
%doc neutron/plugins/ofagent/README
%{_bindir}/neutron-ofagent-agent
%{python_sitelibdir}/neutron/plugins/ofagent


%files oneconvergence-nvsd
%doc LICENSE
%doc neutron/plugins/oneconvergence/README
%dir %{_sysconfdir}/neutron/plugins/oneconvergence
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/oneconvergence/nvsdplugin.ini
%{_bindir}/neutron-nvsd-agent
%{_bindir}/quantum-nvsd-agent
%{python_sitelibdir}/neutron/plugins/oneconvergence

%files openvswitch
%doc LICENSE
%doc neutron/plugins/openvswitch/README
%{_bindir}/neutron-openvswitch-agent
%{_bindir}/quantum-openvswitch-agent
%{_bindir}/neutron-ovs-cleanup
%{_bindir}/quantum-ovs-cleanup
%{_unitdir}/neutron-openvswitch-agent.service
%{_unitdir}/neutron-ovs-cleanup.service
%{python_sitelibdir}/neutron/plugins/openvswitch
%{_datadir}/neutron/rootwrap/openvswitch-plugin.filters
%dir %{_sysconfdir}/neutron/plugins/openvswitch
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/openvswitch/*.ini


%files plumgrid
%doc LICENSE
%doc neutron/plugins/plumgrid/README
%{python_sitelibdir}/neutron/plugins/plumgrid
%dir %{_sysconfdir}/neutron/plugins/plumgrid
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/plumgrid/*.ini


%files ryu
%doc LICENSE
%doc neutron/plugins/ryu/README
%{_bindir}/neutron-ryu-agent
%{_bindir}/quantum-ryu-agent
%{_unitdir}/neutron-ryu-agent.service
%{python_sitelibdir}/neutron/plugins/ryu
%{_datadir}/neutron/rootwrap/ryu-plugin.filters
%dir %{_sysconfdir}/neutron/plugins/ryu
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/ryu/*.ini


%files nec
%doc LICENSE
%doc neutron/plugins/nec/README
%{_bindir}/neutron-nec-agent
%{_bindir}/quantum-nec-agent
%{_unitdir}/neutron-nec-agent.service
%{python_sitelibdir}/neutron/plugins/nec
%{_datadir}/neutron/rootwrap/nec-plugin.filters
%dir %{_sysconfdir}/neutron/plugins/nec
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/nec/*.ini


%files metaplugin
%doc LICENSE
%doc neutron/plugins/metaplugin/README
%{python_sitelibdir}/neutron/plugins/metaplugin
%dir %{_sysconfdir}/neutron/plugins/metaplugin
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/metaplugin/*.ini


%files vmware
%doc LICENSE
%{_bindir}/neutron-check-nvp-config
%{_bindir}/quantum-check-nvp-config
%{_bindir}/neutron-check-nsx-config
%{_bindir}/neutron-nsx-manage
%{python_sitelibdir}/neutron/plugins/vmware
%dir %{_sysconfdir}/neutron/plugins/nicira
%dir %{_sysconfdir}/neutron/plugins/vmware
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/nicira/*.ini
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/vmware/*.ini


%files metering-agent
%doc LICENSE
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/metering_agent.ini
%{_unitdir}/neutron-metering-agent.service
%{_bindir}/neutron-metering-agent


%files vpn-agent
%doc LICENSE
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/vpn_agent.ini
%{_unitdir}/neutron-vpn-agent.service
%{_bindir}/neutron-vpn-agent
%{_datadir}/neutron/rootwrap/vpnaas.filters


%changelog
* Tue Aug 12 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.2-alt1
- 2014.1.2

* Mon Aug 11 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.1-alt3
- openvswitch-agent takes plugins.ml2 by default: most usable configuration

* Tue Aug 05 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.1-alt2
- user neutron added to wheel group, for neutron-rootwrap

* Thu Jul 24 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.1-alt1
- First build for ALT (based on Fedora 2014.1.1-5.fc21.src)
- Add "AutoReq: yes, nopython" to subpackages:
  * brocade, midonet, ofagent, plumgrid


