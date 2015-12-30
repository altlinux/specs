%def_disable embrane
%def_enable linuxbridge
%def_enable brocade
%def_enable openvswitch
%def_enable mellanox

Name: openstack-neutron
Version: 7.0.1
Release: alt1
Epoch: 1
Provides: openstack-quantum = %EVR
Obsoletes: openstack-quantum < 2013.2-0.4.b3
Summary: OpenStack Networking Service

Group: System/Servers
License: ASL 2.0
Url: http://launchpad.net/neutron/

Source0: %name-%version.tar
Source1: neutron.logrotate
Source2: neutron-sudoers
Source3: %name.tmpfiles
Source5: neutron.sysconfig

Source10: neutron-server.service
Source11: neutron-linuxbridge-agent.service
Source12: neutron-openvswitch-agent.service
Source15: neutron-dhcp-agent.service
Source16: neutron-l3-agent.service
Source17: neutron-metadata-agent.service
Source18: neutron-ovs-cleanup.service
Source19: neutron-mlnx-agent.service
Source20: neutron-metering-agent.service
Source21: neutron-sriov-nic-agent.service
Source22: neutron-netns-cleanup.service
Source28: neutron-dev-server.service
Source29: neutron-rpc-server.service

Source110: neutron-server.init
Source111: neutron-linuxbridge-agent.init
Source112: neutron-openvswitch-agent.init
Source115: neutron-dhcp-agent.init
Source116: neutron-l3-agent.init
Source117: neutron-metadata-agent.init
Source118: neutron-ovs-cleanup.init
Source119: neutron-mlnx-agent.init
Source120: neutron-metering-agent.init
Source121: neutron-sriov-nic-agent.init
Source122: neutron-netns-cleanup.init
Source128: neutron-dev-server.init
Source129: neutron-rpc-server.init

BuildArch: noarch

BuildRequires: crudini
BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-d2to1
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno >= 0.1.1
BuildRequires: python-module-PasteDeploy
BuildRequires: python-module-routes >= 1.12.3
BuildRequires: python-module-debtcollector >= 0.3.0
BuildRequires: python-module-eventlet >= 0.17.4
BuildRequires: python-module-pecan >= 1.0.0
BuildRequires: python-module-greenlet >= 0.3.2
BuildRequires: python-module-httplib2 >= 0.7.5
BuildRequires: python-module-requests >= 2.5.2
BuildRequires: python-module-keystonemiddleware >= 2.0.0
BuildRequires: python-module-netaddr >= 0.7.12
BuildRequires: python-module-neutronclient >= 2.6.0
BuildRequires: python-module-retrying >= 1.2.3
BuildRequires: python-module-ryu >= 3.23.2
BuildRequires: python-module-SQLAlchemy >= 0.9.9
BuildRequires: python-module-keystoneclient >= 1.6.0
BuildRequires: python-module-alembic >= 0.8.0
BuildRequires: python-module-stevedore >= 1.5.0
BuildRequires: python-module-oslo.concurrency >= 2.3.0
BuildRequires: python-module-oslo.config >= 2.3.0
BuildRequires: python-module-oslo.context >= 0.2.0
BuildRequires: python-module-oslo.db >= 2.4.1 python-module-oslo.db-tests
BuildRequires: python-module-oslo.i18n >= 1.5.0
BuildRequires: python-module-oslo.log >= 1.8.0
BuildRequires: python-module-oslo.messaging >= 1.16.0
BuildRequires: python-module-oslo.middleware >= 1.8.0
BuildRequires: python-module-oslo.policy >= 0.5.0
BuildRequires: python-module-oslo.rootwrap >= 2.0.0
BuildRequires: python-module-oslo.serialization >= 1.4.0
BuildRequires: python-module-oslo.service >= 0.7.0
BuildRequires: python-module-oslo.utils >= 2.0.0
BuildRequires: python-module-oslo.versionedobjects >= 0.9.0
BuildRequires: python-module-novaclient >= 2.28.1


Requires: python-module-neutron = %EVR
Requires: python-module-PasteDeploy
Requires: python-module-oslo.rootwrap
Requires: openstack-utils

# dnsmasq is not a hard requirement, but is currently the only option
# when neutron-dhcp-agent is deployed.
Requires: dnsmasq
Requires: dnsmasq-utils

Requires(pre): shadow-utils

%description
Neutron is a virtual network service for Openstack. Just like
OpenStack Nova provides an API to dynamically request and configure
virtual servers, Neutron provides an API to dynamically request and
configure virtual networks. These networks connect "interfaces" from
other OpenStack services (e.g., virtual NICs from Nova VMs). The
Neutron API supports extensions to provide advanced network
capabilities (e.g., QoS, ACLs, network monitoring, etc.)

%package -n python-module-neutron
Summary: Neutron Python libraries
Group: Development/Python

Provides: python-module-quantum = %EVR
Obsoletes: python-module-quantum < 2013.2-0.4.b3

Requires: python-module-keystoneclient >= 1.2.0
Requires: python-module-keystonemiddleware >= 1.5.0
Requires: python-module-oslo.config >= 1.9.0
Requires: python-module-neutronclient >= 2.4.0
Requires: python-module-novaclient >= 2.22.0
Requires: sudo conntrack-tools

%description -n python-module-neutron
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron Python library.

%package rpc-server
Summary: Neutron (RPC only) Server
Group: System/Servers
Requires: %name = %EVR

%description rpc-server
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains an alternative Neutron server that handles AMQP RPC
workload only.

%package dev-server
Summary: Neutron Server (WSGI pecan)
Group: System/Servers
Requires: %name = %EVR

%description dev-server
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains an alternative Neutron server implementation that uses
pecan library as its WSGI backend.

%package bigswitch
Summary: Neutron Big Switch plugin
Group: Development/Python

Provides: openstack-quantum-bigswitch = %EVR
Obsoletes: openstack-quantum-bigswitch < 2013.2-0.4.b3

Requires: %name = %EVR

%description bigswitch
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using the FloodLight Openflow Controller or the Big Switch
Networks Controller.

%package brocade
Summary: Neutron Brocade plugin
Group: Development/Python

Provides: openstack-quantum-brocade = %EVR
Obsoletes: openstack-quantum-brocade < 2013.2-0.4.b3

Requires: %name = %EVR
Requires: python-module-ncclient

%description brocade
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using Brocade VCS switches running NOS.

%package embrane
Summary: Neutron Embrane plugin
Group: Development/Python

Requires: %name = %EVR

%description embrane
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the Neutron plugin that implements virtual
L3-L7 network services using Embrane's heleos platform.

This package contains the neutron plugin that implements virtual
networks using Microsoft Hyper-V.

%package linuxbridge
Summary: Neutron linuxbridge plugin
Group: Development/Python

Provides: openstack-quantum-linuxbridge = %EVR
Obsoletes: openstack-quantum-linuxbridge < 2013.2-0.4.b3

Requires: bridge-utils
Requires: %name = %EVR

%description linuxbridge
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks as VLANs using Linux bridging.

%package mellanox
Summary: Neutron Mellanox plugin
Group: Development/Python

Provides: openstack-quantum-mellanox = %EVR
Obsoletes: openstack-quantum-mellanox < 2013.2-0.4.b3

Requires: %name = %EVR

%description mellanox
This plugin implements Neutron v2 APIs with support for Mellanox embedded
switch functionality as part of the VPI (Ethernet/InfiniBand) HCA.

%package midonet
Summary: Neutron MidoNet plugin
Group: Development/Python

Provides: openstack-quantum-midonet = %EVR
Obsoletes: openstack-quantum-midonet < 2013.2-0.4.b3

Requires: %name = %EVR

%description midonet
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using MidoNet from Midokura.

%package ml2
Summary: Neutron ML2 plugin
Group: Development/Python

Provides: openstack-quantum-ml2 = %EVR
Obsoletes: openstack-quantum-ml2 < 2013.2-0.4.b3

Requires: %name = %EVR

%description ml2
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains a neutron plugin that allows the use of drivers
to support separately extensible sets of network types and the mechanisms
for accessing those types.

%package nuage
Summary: Neutron Nuage plugin
Group: Development/Python

Requires: %name = %EVR

%description nuage
This plugin implements Neutron v2 APIs with support for Nuage Networks
Virtual Service Platform (VSP).

%package oneconvergence-nvsd
Summary: Neutron One Convergence NVSD plugin
Group: Development/Python

Requires: %name = %EVR

%description oneconvergence-nvsd
Neutron provides an API to dynamnically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using One Convergence NVSD

%package opencontrail
Summary: Neutron OpenContrail plugin
Group: Development/Python

Requires: %name = %EVR

%description opencontrail
This plugin implements Neutron v2 APIs with support for the OpenContrail
plugin.

%package openvswitch
Summary: Neutron openvswitch plugin
Group: Development/Python

Requires: %name = %EVR
Requires: openvswitch

%description openvswitch
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using Open vSwitch.

%package ovsvapp
Summary: Neutron OVSvApp vSphere plugin
Group: Development/Python

Requires: %name = %EVR

%description ovsvapp
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using OVSvApp vSphere L2 agent.


%package metering-agent
Summary: Neutron bandwidth metering agent
Group: Development/Python

Requires: %name = %EVR

%description metering-agent
Neutron provides an API to measure bandwidth utilization

This package contains the neutron agent responsible for generating bandwidth
utilization notifications.

%package sriov-nic-agent
Summary: Neutron SR-IOV NIC agent
Group: Development/Python

Requires: %name = %EVR

%description sriov-nic-agent
Neutron allows to run virtual instances using SR-IOV NIC hardware

This package contains the Neutron agent to support advanced features of
SR-IOV network cards.

%prep
%setup

find neutron -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +


# Let's handle dependencies ourseleves
rm -f requirements.txt

%build
export PBR_VERSION=%version
export SKIP_PIP_INSTALL=1

%python_build

export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b man doc/source doc/build/man
sphinx-build -b html doc/source doc/build/html

%install
%python_install --prefix=%_prefix --install-data=/

install -d -m 750 %buildroot%_cachedir/neutron

# Remove unused files
rm -rf %buildroot%python_sitelibdir/bin
rm -rf %buildroot%python_sitelibdir/doc
rm -rf %buildroot%python_sitelibdir/tools
rm -rf %buildroot%python_sitelibdir/neutron/tests
rm -rf %buildroot%python_sitelibdir/neutron/plugins/*/tests
rm -f %buildroot%python_sitelibdir/neutron/plugins/*/run_tests.*
rm -f %buildroot/etc/init.d/neutron-server

# Install logrotate
install -p -D -m 644 %SOURCE1 %buildroot%_sysconfdir/logrotate.d/%name

# Install sudoers
install -p -D -m 400 %SOURCE2 %buildroot%_sysconfdir/sudoers.d/neutron

# Install tmpfiles
install -p -D -m 644 %SOURCE3 %buildroot%_tmpfilesdir/%name.conf

# Install sysconfig
install -p -D -m 644 %SOURCE5 %buildroot%_sysconfdir/sysconfig/neutron

# Install systemd units
install -p -D -m 644 %SOURCE10 %buildroot%_unitdir/neutron-server.service
install -p -D -m 644 %SOURCE11 %buildroot%_unitdir/neutron-linuxbridge-agent.service
install -p -D -m 644 %SOURCE12 %buildroot%_unitdir/neutron-openvswitch-agent.service
install -p -D -m 644 %SOURCE15 %buildroot%_unitdir/neutron-dhcp-agent.service
install -p -D -m 644 %SOURCE16 %buildroot%_unitdir/neutron-l3-agent.service
install -p -D -m 644 %SOURCE17 %buildroot%_unitdir/neutron-metadata-agent.service
install -p -D -m 644 %SOURCE18 %buildroot%_unitdir/neutron-ovs-cleanup.service
install -p -D -m 644 %SOURCE19 %buildroot%_unitdir/neutron-mlnx-agent.service
install -p -D -m 644 %SOURCE20 %buildroot%_unitdir/neutron-metering-agent.service
install -p -D -m 644 %SOURCE21 %buildroot%_unitdir/neutron-sriov-nic-agent.service
install -p -D -m 644 %SOURCE22 %buildroot%_unitdir/neutron-netns-cleanup.service
install -p -D -m 644 %SOURCE28 %buildroot%_unitdir/neutron-dev-server.service
install -p -D -m 644 %SOURCE29 %buildroot%_unitdir/neutron-rpc-server.service

# Install sysV init scripts
install -p -D -m 755 %SOURCE110 %buildroot%_initdir/neutron-server
install -p -D -m 755 %SOURCE111 %buildroot%_initdir/neutron-linuxbridge-agent
install -p -D -m 755 %SOURCE112 %buildroot%_initdir/neutron-openvswitch-agent
install -p -D -m 755 %SOURCE115 %buildroot%_initdir/neutron-dhcp-agent
install -p -D -m 755 %SOURCE116 %buildroot%_initdir/neutron-l3-agent
install -p -D -m 755 %SOURCE117 %buildroot%_initdir/neutron-metadata-agent
install -p -D -m 755 %SOURCE118 %buildroot%_initdir/neutron-ovs-cleanup
install -p -D -m 755 %SOURCE119 %buildroot%_initdir/neutron-mlnx-agent
install -p -D -m 755 %SOURCE120 %buildroot%_initdir/neutron-metering-agent
install -p -D -m 755 %SOURCE121 %buildroot%_initdir/neutron-sriov-nic-agent
install -p -D -m 755 %SOURCE122 %buildroot%_initdir/neutron-netns-cleanup
install -p -D -m 755 %SOURCE128 %buildroot%_initdir/neutron-dev-server
install -p -D -m 755 %SOURCE129 %buildroot%_initdir/neutron-rpc-server

# Setup directories
install -d -m 755 %buildroot%_sharedstatedir/neutron
install -d -m 755 %buildroot%_logdir/neutron
install -d -m 755 %buildroot%_runtimedir/neutron

# Kill hyperv agent since it's of no use for Linux
rm %buildroot/%_bindir/neutron-hyperv-agent


sed -i -e 's|# root_helper = sudo|root_helper = sudo neutron-rootwrap /etc/neutron/rootwrap.conf|' %buildroot%_sysconfdir/neutron/neutron.conf

## ALTLinux configuration defaults
%define neutron_conf %buildroot/etc/neutron/neutron.conf
%define plugin_dir %buildroot/etc/neutron/plugins/
crudini --set %neutron_conf DEFAULT core_plugin neutron.plugins.ml2.plugin.Ml2Plugin
crudini --set %neutron_conf DEFAULT service_plugins "neutron.services.l3_router.l3_router_plugin.L3RouterPlugin"
crudini --set %neutron_conf DEFAULT state_path /var/lib/neutron
crudini --set %neutron_conf agent root_helper "sudo neutron-rootwrap /etc/neutron/rootwrap.conf"
crudini --set %neutron_conf DEFAULT log_dir /var/log/neutron
crudini --set %neutron_conf oslo_concurrency lock_path /var/run/neutron
crudini --set %neutron_conf keystone_authtoken signing_dir /var/cache/neutron/keystone-signing
for i in dhcp_agent.ini l3_agent.ini ; do
  crudini --set %buildroot/etc/neutron/$i DEFAULT interface_driver neutron.agent.linux.interface.BridgeInterfaceDriver
done
crudini --set %buildroot/etc/neutron/dhcp_agent.ini DEFAULT dhcp_delete_namespaces True

#crudini --set %buildroot/etc/neutron/l3_agent.ini DEFAULT external_network_bridge "br-ex"
#crudini --set %buildroot/etc/neutron/l3_agent.ini DEFAULT external_network_bridge ""
#crudini --set %plugin_dir/ml2/ml2_conf.ini ml2 mechanism_drivers linuxbridge
#crudini --set %plugin_dir/ml2/ml2_conf.ini securitygroup firewall_driver neutron.agent.linux.iptables_firewall.IptablesFirewallDriver
#crudini --set %plugin_dir/linuxbridge/linuxbridge_conf.ini securitygroup firewall_driver neutron.agent.linux.iptables_firewall.IptablesFirewallDriver

%pre
%_sbindir/groupadd -r -f neutron 2>/dev/null ||:
%_sbindir/useradd -r -g neutron -G neutron,wheel -c 'OpenStack Neutron Daemons' \
        -s /sbin/nologin  -d %_sharedstatedir/neutron neutron 2>/dev/null ||:

%post
%post_service neutron-dhcp-agent
%post_service neutron-l3-agent
%post_service neutron-metadata-agent
%post_service neutron-server
%post_service neutron-netns-cleanup

%preun
%preun_service neutron-dhcp-agent
%preun_service neutron-l3-agent
%preun_service neutron-metadata-agent
%preun_service neutron-server
%preun_service neutron-netns-cleanup

%post linuxbridge
oldconf=%_sysconfdir/neutron/plugins/linuxbridge/linuxbridge_conf.ini
newconf=%_sysconfdir/neutron/plugins/ml2/linuxbridge_agent.ini
if [ $1 -gt 1 ]; then
    if [ -e $oldconf ]; then
        # Imitate noreplace
        cp $newconf ${newconf}.rpmnew
        cp $oldconf $newconf
    fi
fi
%post_service neutron-linuxbridge-agent

%preun linuxbridge
%preun_service neutron-linuxbridge-agent

%post mellanox
%post_service neutron-mlnx-agent
%preun mellanox
%preun_service neutron-mlnx-agent

%post openvswitch
oldconf=%_sysconfdir/neutron/plugins/openvswitch/ovs_neutron_plugin.ini
newconf=%_sysconfdir/neutron/plugins/ml2/openvswitch_agent.ini
if [ $1 -gt 1 ]; then
    if [ -e $oldconf ]; then
        # Imitate noreplace
        cp $newconf ${newconf}.rpmnew
        cp $oldconf $newconf
    fi
fi

%post_service neutron-openvswitch-agent
%post_service neutron-ovs-cleanup

%preun openvswitch
%preun_service neutron-openvswitch-agent
%preun_service neutron-ovs-cleanup

%post metering-agent
%post_service neutron-metering-agent
%preun metering-agent
%preun_service neutron-metering-agent

%post sriov-nic-agent
%post_service neutron-sriov-nic-agent
%preun sriov-nic-agent
%preun_service neutron-sriov-nic-agent

%files
%doc LICENSE
%doc README.rst

%_bindir/neutron-db-manage
%_bindir/neutron-debug
%_bindir/neutron-dhcp-agent
%_bindir/neutron-ipset-cleanup
%_bindir/neutron-keepalived-state-change
%_bindir/neutron-l3-agent
%_bindir/neutron-metadata-agent
%_bindir/neutron-netns-cleanup
%_bindir/neutron-ns-metadata-proxy
%_bindir/neutron-pd-notify
%_bindir/neutron-rootwrap
%_bindir/neutron-rootwrap-daemon
#%_bindir/neutron-rootwrap-xen-dom0
%_bindir/neutron-sanity-check
%_bindir/neutron-server
%_bindir/neutron-usage-audit

%_unitdir/neutron-dhcp-agent.service
%_unitdir/neutron-l3-agent.service
%_unitdir/neutron-metadata-agent.service
%_unitdir/neutron-server.service
%_unitdir/neutron-netns-cleanup.service
%_initdir/neutron-dhcp-agent
%_initdir/neutron-l3-agent
%_initdir/neutron-metadata-agent
%_initdir/neutron-server
%_initdir/neutron-netns-cleanup

%config(noreplace) %_sysconfdir/sysconfig/neutron
%dir %_sysconfdir/neutron
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/dhcp_agent.ini
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/l3_agent.ini
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/metadata_agent.ini
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/policy.json
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/api-paste.ini
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/neutron.conf
%config(noreplace) %_sysconfdir/neutron/rootwrap.conf
%dir %_sysconfdir/neutron/plugins
%config(noreplace) %_sysconfdir/logrotate.d/*
%config(noreplace) %_sysconfdir/sudoers.d/neutron
%dir %attr(0755, neutron, neutron) %_sharedstatedir/neutron
%dir %attr(0750, neutron, adm) %_logdir/neutron
%dir %attr(0750, neutron, neutron) %_runtimedir/neutron
%dir %attr(0750, neutron, neutron) %_cachedir/neutron
%_tmpfilesdir/%name.conf
%dir %_sysconfdir/neutron/rootwrap.d
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/rootwrap.d/*.filters
%exclude %_sysconfdir/neutron/rootwrap.d/linuxbridge-plugin.filters
%exclude %_sysconfdir/neutron/rootwrap.d/openvswitch-plugin.filters

%files -n python-module-neutron
%doc LICENSE
%doc README.rst
%python_sitelibdir/neutron
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/neutron/plugins/ml2/drivers/openvswitch/agent/xenapi
%if_disabled embrane
%exclude %python_sitelibdir/neutron/plugins/embrane
%endif

%files rpc-server
%_bindir/neutron-rpc-server
%_unitdir/neutron-rpc-server.service
%_initdir/neutron-rpc-server

%files dev-server
%_bindir/neutron-dev-server
%_unitdir/neutron-dev-server.service
%_initdir/neutron-dev-server

%files bigswitch
%doc LICENSE
%_bindir/neutron-restproxy-agent
%dir %_sysconfdir/neutron/plugins/bigswitch
%_sysconfdir/neutron/plugins/bigswitch/ssl
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/bigswitch/*.ini

%if_enabled brocade
%files brocade
%doc LICENSE
%doc neutron/plugins/brocade/README.md
%dir %_sysconfdir/neutron/plugins/brocade
%dir %_sysconfdir/neutron/plugins/brocade/vyatta
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/brocade/*.ini
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/brocade/vyatta/*.ini
%endif


%if_enabled embrane
%files embrane
%doc LICENSE
%doc neutron/plugins/embrane/README
%dir %_sysconfdir/neutron/plugins/embrane
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/embrane/*.ini
%endif

%if_enabled linuxbridge
%files linuxbridge
%doc LICENSE
%_bindir/neutron-linuxbridge-agent
%_unitdir/neutron-linuxbridge-agent.service
%_initdir/neutron-linuxbridge-agent
%config %_sysconfdir/neutron/rootwrap.d/linuxbridge-plugin.filters
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/ml2/linuxbridge_agent.ini
%endif

%if_enabled mellanox
%files mellanox
%doc LICENSE
%doc neutron/plugins/ml2/drivers/mlnx/README
%_bindir/neutron-mlnx-agent
%_unitdir/neutron-mlnx-agent.service
%_initdir/neutron-mlnx-agent
%dir %_sysconfdir/neutron/plugins/mlnx
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/mlnx/*.ini
%endif

%files midonet
%doc LICENSE
#%%doc neutron/plugins/midonet/README
%dir %_sysconfdir/neutron/plugins/midonet
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/midonet/*.ini

%files ml2
%doc LICENSE
%doc neutron/plugins/ml2/README
%dir %_sysconfdir/neutron/plugins/ml2
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/ml2/*.ini
%exclude %_sysconfdir/neutron/plugins/ml2/linuxbridge_agent.ini
%exclude %_sysconfdir/neutron/plugins/ml2/openvswitch_agent.ini

%files nuage
%doc LICENSE
%dir %_sysconfdir/neutron/plugins/nuage
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/nuage/*.ini

%files oneconvergence-nvsd
%doc LICENSE
%doc neutron/plugins/oneconvergence/README
%_bindir/neutron-nvsd-agent
%dir %_sysconfdir/neutron/plugins/oneconvergence
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/oneconvergence/nvsdplugin.ini

%files opencontrail
%doc LICENSE
#%doc neutron/plugins/opencontrail/README
%dir %_sysconfdir/neutron/plugins/opencontrail
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/opencontrail/*.ini

%if_enabled openvswitch
%files openvswitch
%doc LICENSE
%_bindir/neutron-openvswitch-agent
%_bindir/neutron-ovs-cleanup
%_unitdir/neutron-openvswitch-agent.service
%_initdir/neutron-openvswitch-agent
%_unitdir/neutron-ovs-cleanup.service
%_initdir/neutron-ovs-cleanup
%config %_sysconfdir/neutron/rootwrap.d/openvswitch-plugin.filters
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/ml2/openvswitch_agent.ini
%endif

%files ovsvapp
%doc LICENSE
%_bindir/neutron-ovsvapp-agent
# TODO: add a systemd unit file
%dir %_sysconfdir/neutron/plugins/ovsvapp
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/ovsvapp/*.ini

%files metering-agent
%doc LICENSE
%_unitdir/neutron-metering-agent.service
%_initdir/neutron-metering-agent
%_bindir/neutron-metering-agent
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/metering_agent.ini

%files sriov-nic-agent
%doc LICENSE
%_bindir/neutron-sriov-nic-agent
%_unitdir/neutron-sriov-nic-agent.service
%_initdir/neutron-sriov-nic-agent

%changelog
* Wed Dec 30 2015 Alexey Shabalin <shaba@altlinux.ru> 1:7.0.1-alt1
- 7.0.1

* Mon Nov 09 2015 Alexey Shabalin <shaba@altlinux.ru> 1:7.0.0-alt2
- fix systemd units and sysv scripts

* Fri Oct 30 2015 Alexey Shabalin <shaba@altlinux.ru> 1:7.0.0-alt1
- 7.0.0 Liberty Release

* Mon Oct 26 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.2-alt2
- add read config from /etc/sysconfig/neutron to l3-agent
- add R:conntrack-tools

* Thu Oct 15 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.2-alt1
- 2015.1.2

* Fri Oct 02 2015 Lenar Shakirov <snejok@altlinux.ru> 2015.1.1-alt6
- neutron-netaddr-broadcast-bug.patch added

* Tue Sep 29 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.1-alt5
- fix init for neutron-openvswitch-agent

* Tue Sep 29 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.1-alt3
- fix neutron-server.service
- fix neutron-dhcp-agent.init
- update tmpfiles
- update default config install section with crudini

* Fri Sep 04 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2015.1.1-alt2
- config files changed in neutron-openvswitch-agent.service and 
  neutron-dhcp-agent.service

* Mon Aug 24 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.1-alt1
- 2015.1.1
- drop neutron-dist.conf in datadir

* Thu Aug 20 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2015.1.0-alt2
- neutron/plugins/common exclusion fixed. closes: #31220

* Mon May 25 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt1
- 2015.1.0 Kilo Release

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt0.b3.0
- 2015.1.0b3

* Fri Mar 13 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt0.b2.0
- 2015.1.0b2

* Fri Aug 15 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.2-alt2
- openvswitch-agent takes plugins.ml2 directly

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

