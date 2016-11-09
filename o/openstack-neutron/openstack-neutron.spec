
Name: openstack-neutron
Version: 9.1.0
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
Source6: neutron-enable-bridge-firewall.sh

Source10: neutron-server.service
Source11: neutron-linuxbridge-agent.service
Source12: neutron-openvswitch-agent.service
Source15: neutron-dhcp-agent.service
Source16: neutron-l3-agent.service
Source17: neutron-metadata-agent.service
Source18: neutron-ovs-cleanup.service
Source19: neutron-macvtap-agent.service
Source20: neutron-metering-agent.service
Source21: neutron-sriov-nic-agent.service
Source28: neutron-dev-server.service
Source29: neutron-rpc-server.service

Source110: neutron-server.init
Source111: neutron-linuxbridge-agent.init
Source112: neutron-openvswitch-agent.init
Source115: neutron-dhcp-agent.init
Source116: neutron-l3-agent.init
Source117: neutron-metadata-agent.init
Source118: neutron-ovs-cleanup.init
Source119: neutron-macvtap-agent.init
Source120: neutron-metering-agent.init
Source121: neutron-sriov-nic-agent.init
Source128: neutron-dev-server.init
Source129: neutron-rpc-server.init

BuildArch: noarch

BuildRequires: crudini
BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno >= 1.8.0
BuildRequires: python-module-paste
BuildRequires: python-module-PasteDeploy >= 1.5.0
BuildRequires: python-module-routes >= 1.12.3
BuildRequires: python-module-debtcollector >= 1.2.0
BuildRequires: python-module-eventlet >= 0.18.2
BuildRequires: python-module-pecan >= 1.0.0
BuildRequires: python-module-greenlet >= 0.3.2
BuildRequires: python-module-httplib2 >= 0.7.5
BuildRequires: python-module-requests >= 2.10.0
BuildRequires: python-module-jinja2 >= 2.8
BuildRequires: python-module-keystonemiddleware >= 4.0.0
BuildRequires: python-module-netaddr >= 0.7.13
BuildRequires: python-module-netifaces >= 0.10.4
BuildRequires: python-module-neutron-lib >= 0.4.0
BuildRequires: python-module-neutronclient >= 5.1.0
BuildRequires: python-module-retrying >= 1.2.3
BuildRequires: python-module-ryu >= 3.30
BuildRequires: python-module-SQLAlchemy >= 1.0.10
BuildRequires: python-module-webob >= 1.2.3
BuildRequires: python-module-keystoneauth1 >= 2.10.0
BuildRequires: python-module-alembic >= 0.8.4
BuildRequires: python-module-stevedore >= 1.16.0
BuildRequires: python-module-oslo.cache >= 1.5.0
BuildRequires: python-module-oslo.concurrency >= 3.8.0
BuildRequires: python-module-oslo.config >= 3.14.0
BuildRequires: python-module-oslo.context >= 2.9.0
BuildRequires: python-module-oslo.db >= 4.10.0 python-module-oslo.db-tests
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.log >= 1.14.0
BuildRequires: python-module-oslo.messaging >= 5.2.0
BuildRequires: python-module-oslo.middleware >= 3.0.0
BuildRequires: python-module-oslo.policy >= 1.9.0
BuildRequires: python-module-oslo.reports >= 0.6.0
BuildRequires: python-module-oslo.rootwrap >= 5.0.0
BuildRequires: python-module-oslo.serialization >= 1.10.0
BuildRequires: python-module-oslo.service >= 1.10.0
BuildRequires: python-module-oslo.utils >= 3.16.0
BuildRequires: python-module-oslo.versionedobjects >= 1.13.0
BuildRequires: python-module-osprofiler >= 1.4.0
BuildRequires: python-module-openvswitch >= 2.5.0
BuildRequires: python-module-novaclient >= 2.28.1
BuildRequires: python-module-designateclient >= 1.5.0

Requires: python-module-neutron = %EVR
Requires: python-module-PasteDeploy
Requires: python-module-oslo.rootwrap

Requires(pre): shadow-utils

Conflicts: %name-ml2 < %EVR

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

Requires: python-module-PasteDeploy
Requires: python-module-keystoneauth1 >= 2.1.0
Requires: python-module-keystonemiddleware >= 4.0.0
Requires: python-module-oslo.config >= 3.7.0
Requires: python-module-neutronclient >= 5.1.0
Requires: python-module-novaclient >= 2.22.0
Requires: sudo conntrack-tools

%description -n python-module-neutron
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron Python library.

%package server
Summary: OpenStack Network Neutron Server
Group: System/Servers
Requires: %name = %EVR
Provides: %name-rpc-server = %EVR
Obsoletes: %name-rpc-server < %EVR

%description server
This package provides the Neutron server

%package dhcp-agent
Summary: OpenStack Network - DHCP Agent
Group: Development/Python
Requires: %name = %EVR
Requires: dnsmasq dnsmasq-utils

%description dhcp-agent
This package provides the DHCP Agent.

%package linuxbridge-agent
Summary: OpenStack Network - Linux Bridge Agent
Group: Development/Python

Provides: openstack-quantum-linuxbridge = %EVR
Obsoletes: openstack-quantum-linuxbridge < 2013.2-0.4.b3
Provides: %name-linuxbridge = %EVR
Obsoletes: %name-linuxbridge < %EVR

Provides:  %name-agent = %EVR

Requires: bridge-utils
Requires: conntrack-tools
Requires: ebtables
Requires: ipset
Requires: iptables
Requires: kmod
Requires: %name = %EVR

%description linuxbridge-agent
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using Linux bridging.

%package l3-agent
Summary: OpenStack Network Service (Neutron) - L3 Agent
Group: Development/Python
Requires: %name = %EVR
Requires: conntrack-tools

%description l3-agent
This package provides the L3 Agent.

%package openvswitch-agent
Summary: OpenStack Network Service (Neutron) - Openvswitch Agent
Group: Development/Python
Provides: %name-openvswitch = %EVR
Obsoletes: %name-openvswitch < %EVR

Provides:  %name-agent = %EVR

Requires: %name = %EVR
Requires: openvswitch
Requires: python-module-openvswitch
Requires: conntrack-tools
Requires: ipset
Requires: iptables
Requires: kmod

%description openvswitch-agent
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using Open vSwitch.

%package macvtap-agent
Summary: OpenStack Network - macvtap
Group: Development/Python
Requires: %name = %EVR

%description macvtap-agent
This package provides the macvtap Agent.

%package metadata-agent
Summary: OpenStack Network - Meta Data Agent
Group: Development/Python
Requires: %name = %EVR

%description metadata-agent
This package provides the Meta Data Agent.

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

PYTHONPATH=. tools/generate_config_file_samples.sh

%install
%python_install --prefix=%_prefix --install-data=/


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

# Install helper scripts
install -p -D -m 755 %SOURCE6 %buildroot%_bindir/neutron-enable-bridge-firewall.sh

# Install systemd units
install -p -D -m 644 %SOURCE10 %buildroot%_unitdir/neutron-server.service
install -p -D -m 644 %SOURCE11 %buildroot%_unitdir/neutron-linuxbridge-agent.service
install -p -D -m 644 %SOURCE12 %buildroot%_unitdir/neutron-openvswitch-agent.service
install -p -D -m 644 %SOURCE15 %buildroot%_unitdir/neutron-dhcp-agent.service
install -p -D -m 644 %SOURCE16 %buildroot%_unitdir/neutron-l3-agent.service
install -p -D -m 644 %SOURCE17 %buildroot%_unitdir/neutron-metadata-agent.service
install -p -D -m 644 %SOURCE18 %buildroot%_unitdir/neutron-ovs-cleanup.service
install -p -D -m 644 %SOURCE19 %buildroot%_unitdir/neutron-macvtap-agent.service
install -p -D -m 644 %SOURCE20 %buildroot%_unitdir/neutron-metering-agent.service
install -p -D -m 644 %SOURCE21 %buildroot%_unitdir/neutron-sriov-nic-agent.service
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
install -p -D -m 755 %SOURCE119 %buildroot%_initdir/neutron-macvtap-agent
install -p -D -m 755 %SOURCE120 %buildroot%_initdir/neutron-metering-agent
install -p -D -m 755 %SOURCE121 %buildroot%_initdir/neutron-sriov-nic-agent
install -p -D -m 755 %SOURCE128 %buildroot%_initdir/neutron-dev-server
install -p -D -m 755 %SOURCE129 %buildroot%_initdir/neutron-rpc-server

# Setup directories
install -d -m 755 %buildroot%_sharedstatedir/neutron
install -d -m 755 %buildroot%_logdir/neutron
install -d -m 755 %buildroot%_runtimedir/neutron
install -d -m 750 %buildroot%_cachedir/neutron

# configuration files
for c in neutron.conf dhcp_agent.ini l3_agent.ini metadata_agent.ini metering_agent.ini ; do
    install -p -D -m 644 etc/$c.sample %buildroot%_sysconfdir/neutron/$c
done
for c in linuxbridge_agent.ini ml2_conf.ini ml2_conf_sriov.ini openvswitch_agent.ini sriov_agent.ini macvtap_agent.ini ; do
    install -p -D -m 644 etc/neutron/plugins/ml2/$c.sample %buildroot%_sysconfdir/neutron/plugins/ml2/$c
done

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

%post server
%post_service neutron-server
%preun server
%preun_service neutron-server

%post dhcp-agent
%post_service neutron-dhcp-agent
%preun dhcp-agent
%preun_service neutron-dhcp-agent

%post l3-agent
%post_service neutron-l3-agent
%preun l3-agent
%preun_service neutron-l3-agent

%post metadata-agent
%post_service neutron-metadata-agent
%preun metadata-agent
%preun_service neutron-metadata-agent


%post linuxbridge-agent
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

%preun linuxbridge-agent
%preun_service neutron-linuxbridge-agent

%post openvswitch-agent
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

%preun openvswitch-agent
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

%_bindir/neutron-debug
%_bindir/neutron-ipset-cleanup
%_bindir/neutron-keepalived-state-change
%_bindir/neutron-netns-cleanup
%_bindir/neutron-enable-bridge-firewall.sh
%_bindir/neutron-ns-metadata-proxy
%_bindir/neutron-rootwrap
%_bindir/neutron-rootwrap-daemon
#%_bindir/neutron-rootwrap-xen-dom0
%_bindir/neutron-sanity-check
%_bindir/neutron-usage-audit

%config(noreplace) %_sysconfdir/sysconfig/neutron
%dir %_sysconfdir/neutron
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/policy.json
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/api-paste.ini
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/neutron.conf
%config(noreplace) %_sysconfdir/neutron/rootwrap.conf
%dir %_sysconfdir/neutron/plugins
%dir %_sysconfdir/neutron/plugins/ml2
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/plugins/ml2/*.ini
%config(noreplace) %_sysconfdir/logrotate.d/*
%config(noreplace) %_sysconfdir/sudoers.d/neutron
%dir %attr(0755, neutron, neutron) %_sharedstatedir/neutron
%dir %attr(0770, root, neutron) %_logdir/neutron
%dir %attr(0750, neutron, neutron) %_runtimedir/neutron
%dir %attr(0750, neutron, neutron) %_cachedir/neutron
%_tmpfilesdir/%name.conf
%dir %_sysconfdir/neutron/rootwrap.d
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/rootwrap.d/*.filters
%exclude %_sysconfdir/neutron/rootwrap.d/linuxbridge-plugin.filters
%exclude %_sysconfdir/neutron/rootwrap.d/openvswitch-plugin.filters
%exclude %_sysconfdir/neutron/rootwrap.d/dhcp.filters
%exclude %_sysconfdir/neutron/rootwrap.d/l3.filters

%files -n python-module-neutron
%doc LICENSE
%doc README.rst
%python_sitelibdir/neutron
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/neutron/plugins/ml2/drivers/openvswitch/agent/xenapi

%files server
%_bindir/neutron-server
%_bindir/neutron-rpc-server
%_bindir/neutron-db-manage
%_unitdir/neutron-server.service
%_initdir/neutron-server
%_unitdir/neutron-rpc-server.service
%_initdir/neutron-rpc-server

%files dhcp-agent
%_bindir/neutron-dhcp-agent
%_initdir/neutron-dhcp-agent
%_unitdir/neutron-dhcp-agent.service
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/dhcp_agent.ini
%config %_sysconfdir/neutron/rootwrap.d/dhcp.filters

%files l3-agent
%_bindir/neutron-l3-agent
%_bindir/neutron-pd-notify
%_unitdir/neutron-l3-agent.service
%_initdir/neutron-l3-agent
%config %_sysconfdir/neutron/rootwrap.d/l3.filters
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/l3_agent.ini

%files metadata-agent
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/metadata_agent.ini
%_bindir/neutron-metadata-agent
%_unitdir/neutron-metadata-agent.service
%_initdir/neutron-metadata-agent

%files linuxbridge-agent
%_bindir/neutron-linuxbridge-cleanup
%_bindir/neutron-linuxbridge-agent
%_unitdir/neutron-linuxbridge-agent.service
%_initdir/neutron-linuxbridge-agent
%config %_sysconfdir/neutron/rootwrap.d/linuxbridge-plugin.filters

%files openvswitch-agent
%_bindir/neutron-openvswitch-agent
%_bindir/neutron-ovs-cleanup
%_unitdir/neutron-openvswitch-agent.service
%_initdir/neutron-openvswitch-agent
%_unitdir/neutron-ovs-cleanup.service
%_initdir/neutron-ovs-cleanup
%config %_sysconfdir/neutron/rootwrap.d/openvswitch-plugin.filters

%files macvtap-agent
%_bindir/neutron-macvtap-agent
%_unitdir/neutron-macvtap-agent.service
%_initdir/neutron-macvtap-agent

%files metering-agent
%_unitdir/neutron-metering-agent.service
%_initdir/neutron-metering-agent
%_bindir/neutron-metering-agent
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/metering_agent.ini

%files sriov-nic-agent
%_bindir/neutron-sriov-nic-agent
%_unitdir/neutron-sriov-nic-agent.service
%_initdir/neutron-sriov-nic-agent

%changelog
* Wed Nov 09 2016 Alexey Shabalin <shaba@altlinux.ru> 1:9.1.0-alt1
- update systemd units
- fix log dir permitions for logrotate
- add helper neutron-enable-bridge-firewall.sh

* Fri Oct 21 2016 Alexey Shabalin <shaba@altlinux.ru> 1:9.0.0-alt1
- 9.0.0 Newton release
- drop package bgp-dragent

* Fri Apr 15 2016 Alexey Shabalin <shaba@altlinux.ru> 1:8.0.0-alt1
- 8.0.0 Mitaka release
- rename packages:
  + linuxbridge -> linuxbridge-agent
  + openvswitch -> openvswitch-agent
- add packages:
  + metadata-agent
  + dhcp-agent
  + l3-agent
  + macvtap-agent
  + bgp-dragent
- drop packages:
  + bigswitch
  + brocade
  + embrane
  + mellanox
  + midonet
  + ml2
  + nuage
  + oneconvergence-nvsd
  + opencontrail
  + ovsvapp

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 1:7.0.3-alt1
- 7.0.3

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

