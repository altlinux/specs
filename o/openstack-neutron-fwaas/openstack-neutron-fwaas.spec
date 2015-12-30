%define sname neutron-fwaas

Name: openstack-%sname
Version: 7.0.1
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
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-d2to1
BuildRequires: python-module-netaddr >= 0.7.12
BuildRequires: python-module-SQLAlchemy >= 0.9.9
BuildRequires: python-module-alembic >= 0.8.0
BuildRequires: python-module-oslo.config >= 2.3.0
BuildRequires: python-module-oslo.db >= 2.4.1
BuildRequires: python-module-oslo.log >= 1.8.0
BuildRequires: python-module-oslo.messaging >= 1.16.0
BuildRequires: python-module-oslo.serialization >= 1.4.0
BuildRequires: python-module-oslo.service >= 0.7.0
BuildRequires: python-module-oslo.utils >= 2.0.0

Requires: openstack-neutron >= 1:7.0.0-alt1
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

%install
%python_install --install-data=/

# Remove unused files

%files
%doc LICENSE
%doc README.rst
%config(noreplace) %_sysconfdir/neutron/fwaas_driver.ini

%files -n python-module-%sname
%doc LICENSE
%python_sitelibdir/neutron_fwaas
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/neutron_fwaas/tests


%changelog
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
