%define sname neutron-vpnaas

Name: openstack-%sname
Version: 8.0.0
Release: alt1
Epoch: 1
Summary: OpenStack Networking VPNaaS

Group: System/Servers
License: ASL 2.0
Url: http://launchpad.net/neutron/

Source0: %name-%version.tar
Source1: neutron-vpn-agent.init
Source2: neutron-vpn-agent.service

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-reno
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-requests >= 2.8.1
BuildRequires: python-module-jinja2 >= 2.8
BuildRequires: python-module-netaddr >= 0.7.12
BuildRequires: python-module-SQLAlchemy >= 1.0.10
BuildRequires: python-module-alembic >= 0.8.0
BuildRequires: python-module-neutron-lib >= 0.0.1
BuildRequires: python-module-oslo.concurrency >= 3.5.0
BuildRequires: python-module-oslo.config >= 3.7.0
BuildRequires: python-module-oslo.db >= 4.1.0
BuildRequires: python-module-oslo.log >= 1.14.0
BuildRequires: python-module-oslo.messaging >= 4.0.0
BuildRequires: python-module-oslo.serialization >= 1.10.0
BuildRequires: python-module-oslo.service >= 1.0.0
BuildRequires: python-module-oslo.utils >= 3.5.0

BuildRequires: python-module-neutron >= 1:8.0.0-alt1

Requires: openstack-neutron >= 1:8.0.0-alt1
Requires: python-module-%sname = %EVR

%description

This package contains the code for the Neutron VPN as a Service
(VPNaaS) service. This includes third-party drivers. This package
requires Neutron to run.

%package -n python-module-%sname
Summary: Neutron VPNaaS Python libraries
Group: Development/Python
Requires: python-module-neutron >= 1:8.0.0-alt1

%description -n python-module-%sname

This package contains the code for the Neutron VPN as a Service
(VPNaaS) service. This includes third-party drivers. This package
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
install -p -D -m 644 etc/neutron_vpnaas.conf.sample %buildroot%_sysconfdir/neutron/neutron_vpnaas.conf
install -p -D -m 644 etc/vpn_agent.ini.sample %buildroot%_sysconfdir/neutron/vpn_agent.ini

# Install sysV init scripts
install -p -D -m 755 %SOURCE1 %buildroot%_initdir/neutron-vpn-agent
# Install systemd units
install -p -D -m 644 %SOURCE2 %buildroot%_unitdir/neutron-vpn-agent.service

# Remove unused files

%files
%doc LICENSE
%doc README.rst
%_bindir/*
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/*.ini
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/*.conf
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/rootwrap.d/*.filters
%_initdir/neutron-vpn-agent
%_unitdir/neutron-vpn-agent.service

%files -n python-module-%sname
%doc LICENSE
%python_sitelibdir/neutron_vpnaas
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/neutron_vpnaas/tests


%changelog
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
