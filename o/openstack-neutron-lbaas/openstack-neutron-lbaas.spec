%define sname neutron-lbaas

Name: openstack-%sname
Version: 9.1.0
Release: alt1
Epoch: 1
Summary: OpenStack Networking LBaaS

Group: System/Servers
License: ASL 2.0
Url: http://launchpad.net/neutron/

Source0: %name-%version.tar
Source1: neutron-lbaasv2-agent.init
Source2: neutron-lbaasv2-agent.service

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-reno
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-eventlet >= 0.18.2
BuildRequires: python-module-requests >= 2.10.0
BuildRequires: python-module-netaddr >= 0.7.13
BuildRequires: python-module-neutron-lib >= 0.4.0
BuildRequires: python-module-SQLAlchemy >= 1.0.10
BuildRequires: python-module-alembic >= 0.8.4
BuildRequires: python-module-oslo.config >= 3.14.0
BuildRequires: python-module-oslo.db >= 4.10.0
BuildRequires: python-module-oslo.log >= 1.14.0
BuildRequires: python-module-oslo.messaging >= 5.2.0
BuildRequires: python-module-oslo.reports >= 0.6.0
BuildRequires: python-module-oslo.serialization >= 1.10.0
BuildRequires: python-module-oslo.service >= 1.10.0
BuildRequires: python-module-oslo.utils >= 3.16.0
BuildRequires: python-module-barbicanclient >= 4.0.0
BuildRequires: python-module-pyasn1
BuildRequires: python-module-pyasn1-modules
BuildRequires: python-module-OpenSSL >= 0.14
BuildRequires: python-module-stevedore >= 1.16.0
BuildRequires: python-module-cryptography >= 1.0
BuildRequires: python-module-keystoneauth1 >= 2.10.0
BuildRequires: python-module-neutron >= 1:9.0.0
BuildRequires: python-module-neutron-lib  >= 0.4.0

Requires: openstack-neutron >= 1:9.0.0-alt1
Requires: python-module-%sname = %EVR
Requires: haproxy

%description
This package contains the code for the Neutron Load Balancer as a
Service (LBaaS) service. This includes third-party drivers. This package
requires Neutron to run.

%package -n python-module-%sname
Summary: Neutron LBaaS Python libraries
Group: Development/Python
Requires: python-module-neutron >= 1:8.0.0-alt1
Requires: python-module-neutron-lib
%add_python_req_skip a10_neutron_lbaas
%add_python_req_skip brocade_neutron_lbaas
%add_python_req_skip heleosapi
%add_python_req_skip kemptech_openstack_lbaas
%add_python_req_skip f5lbaasdriver

%description -n python-module-%sname
This package contains the code for the Neutron Load Balancer as a
Service (LBaaS) service. This includes third-party drivers. This package
requires Neutron to run.

This package contains the neutron Python library.

%prep
%setup

# Let's handle dependencies ourseleves
#rm -f requirements.txt

%build
%python_build

PYTHONPATH=. tools/generate_config_file_samples.sh

%install
%python_install --install-data=/

install -p -D -m 644 etc/neutron_lbaas.conf.sample %buildroot%_sysconfdir/neutron/neutron_lbaas.conf
install -p -D -m 644 etc/lbaas_agent.ini.sample %buildroot%_sysconfdir/neutron/lbaas_agent.ini
install -p -D -m 644 etc/services_lbaas.conf.sample %buildroot%_sysconfdir/neutron/services_lbaas.conf

# Install sysV init scripts
install -p -D -m 755 %SOURCE1 %buildroot%_initdir/neutron-lbaasv2-agent
# Install systemd units
install -p -D -m 644 %SOURCE2 %buildroot%_unitdir/neutron-lbaasv2-agent.service

# Remove unused files

%files
%doc LICENSE
%doc README.rst
%_bindir/*
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/*.ini
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/*.conf
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/rootwrap.d/*.filters
%_initdir/neutron-lbaasv2-agent
%_unitdir/neutron-lbaasv2-agent.service

%files -n python-module-%sname
%doc LICENSE
%python_sitelibdir/neutron_lbaas
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/neutron_lbaas/tests


%changelog
* Wed Nov 09 2016 Alexey Shabalin <shaba@altlinux.ru> 1:9.1.0-alt1
- 9.1.0
- drop support lbaas v1

* Mon Oct 24 2016 Alexey Shabalin <shaba@altlinux.ru> 1:9.0.0-alt1
- 9.0.0

* Tue Apr 19 2016 Alexey Shabalin <shaba@altlinux.ru> 1:8.0.0-alt1
- 8.0.0

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 1:7.0.3-alt1
- 7.0.3

* Wed Dec 30 2015 Alexey Shabalin <shaba@altlinux.ru> 1:7.0.1-alt1
- 7.0.1

* Mon Nov 02 2015 Alexey Shabalin <shaba@altlinux.ru> 1:7.0.0-alt1
- 7.0.0

* Thu Oct 15 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.2-alt1
- 2015.1.2

* Tue Aug 25 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.1-alt1
- 2015.1.1

* Fri May 29 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt1
- initial build for Kilo
