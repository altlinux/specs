%define sname neutron-fwaas

Name: openstack-%sname
Version: 2015.1.2
Release: alt1
Summary: OpenStack Networking FWaaS

Group: System/Servers
License: ASL 2.0
Url: http://launchpad.net/neutron/

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr
BuildRequires: python-module-six
BuildRequires: python-module-d2to1

Requires: openstack-neutron >= 2015.1.2
Requires: python-module-%sname = %version-%release

%description
This package contains the code for the Neutron Firewall as a Service
(FWaaS) service. This includes third-party drivers. This package
requires Neutron to run.

%package -n python-module-%sname
Summary: Neutron FWaaS Python libraries
Group: Development/Python
Requires: python-module-neutron >= 2015.1.1

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
* Thu Oct 15 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.2-alt1
- 2015.1.2

* Tue Aug 25 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.1-alt1
- 2015.1.1

* Fri May 29 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt1
- initial build for Kilo
