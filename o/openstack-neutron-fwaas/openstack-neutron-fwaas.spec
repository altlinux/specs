%define oname neutron-fwaas

Name: openstack-%oname
Version: 10.0.1
Release: alt1
Epoch: 1
Summary: OpenStack Networking FWaaS

Group: System/Servers
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools-tests
BuildRequires: python-module-reno
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-eventlet >= 0.18.2
BuildRequires: python-module-netaddr >= 0.7.13
BuildRequires: python-module-SQLAlchemy >= 1.0.10
BuildRequires: python-module-alembic >= 0.8.10
BuildRequires: python-module-neutron-lib >= 1.1.0
BuildRequires: python-module-oslo.config >= 3.14.0
BuildRequires: python-module-oslo.db >= 4.15.0
BuildRequires: python-module-oslo.log >= 3.11.0
BuildRequires: python-module-oslo.messaging >= 5.14.0
BuildRequires: python-module-oslo.serialization >= 1.10.0
BuildRequires: python-module-oslo.service >= 1.10.0
BuildRequires: python-module-oslo.utils >= 3.18.0
BuildRequires: python-module-oslo.privsep >= 1.9.0
BuildRequires: python-module-pyroute2 >= 0.4.12
BuildRequires: python-module-neutron >= 9.0.0

Requires: openstack-neutron >= 1:10.0.0-alt1
Requires: python-module-%oname = %version-%release

%description
This package contains the code for the Neutron Firewall as a Service
(FWaaS) service. This includes third-party drivers. This package
requires Neutron to run.

%package -n python-module-%oname
Summary: Neutron FWaaS Python libraries
Group: Development/Python
Requires: python-module-neutron >= 1:10.0.0-alt1

%description -n python-module-%oname
This package contains the code for the Neutron Firewall as a Service
(FWaaS) service. This includes third-party drivers. This package
requires Neutron to run.

This package contains the neutron Python library.

%package -n python-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description -n python-module-%oname-tests
This package contains tests for %oname.

%prep
%setup -n %oname-%version

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
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/fwaas_driver.ini
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/rootwrap.d/fwaas-privsep.filters

%files -n python-module-%oname
%doc LICENSE
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files -n python-module-%oname-tests
%python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/tests/contrib

%changelog
* Wed Jun 07 2017 Alexey Shabalin <shaba@altlinux.ru> 1:10.0.1-alt1
- 10.0.1
- add tests package

* Wed Apr 12 2017 Alexey Shabalin <shaba@altlinux.ru> 1:9.0.1-alt1
- 9.0.1

* Mon Oct 24 2016 Alexey Shabalin <shaba@altlinux.ru> 1:9.0.0-alt1
- 9.0.0

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
