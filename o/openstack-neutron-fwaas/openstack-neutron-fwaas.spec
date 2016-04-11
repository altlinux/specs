%define sname neutron-fwaas

Name: openstack-%sname
Version: 8.0.0
Release: alt1
Epoch: 1
Summary: OpenStack Networking FWaaS

Group: System/Servers
License: ASL 2.0
Url: http://launchpad.net/neutron/

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-reno
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-eventlet >= 0.18.2
BuildRequires: python-module-httplib2 >= 0.7.5
BuildRequires: python-module-netaddr >= 0.7.12
BuildRequires: python-module-SQLAlchemy >= 1.0.10
BuildRequires: python-module-alembic >= 0.8.0
BuildRequires: python-module-neutron-lib >= 0.0.1
BuildRequires: python-module-oslo.config >= 3.7.0
BuildRequires: python-module-oslo.db >= 4.1.0
BuildRequires: python-module-oslo.log >= 1.14.0
BuildRequires: python-module-oslo.messaging >= 4.0.0
BuildRequires: python-module-oslo.serialization >= 1.10.0
BuildRequires: python-module-oslo.service >= 1.0.0
BuildRequires: python-module-oslo.utils >= 3.5.0

BuildRequires: python-module-neutron >= 8.0.0

Requires: openstack-neutron >= 1:8.0.0-alt1
Requires: python-module-%sname = %version-%release

%description
This package contains the code for the Neutron Firewall as a Service
(FWaaS) service. This includes third-party drivers. This package
requires Neutron to run.

%package -n python-module-%sname
Summary: Neutron FWaaS Python libraries
Group: Development/Python
Requires: python-module-neutron >= 1:7.0.0-alt1

%description -n python-module-%sname
This package contains the code for the Neutron Firewall as a Service
(FWaaS) service. This includes third-party drivers. This package
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

# configuration files
install -p -D -m 644 etc/fwaas_driver.ini.sample %buildroot%_sysconfdir/neutron/fwaas_driver.ini

%files
%doc LICENSE
%doc README.rst
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/*

%files -n python-module-%sname
%doc LICENSE
%python_sitelibdir/neutron_fwaas
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/neutron_fwaas/tests


%changelog
* Tue Apr 19 2016 Alexey Shabalin <shaba@altlinux.ru> 1:8.0.0-alt1
- 8.0.0

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 1:7.0.2-alt1
- 7.0.2

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
