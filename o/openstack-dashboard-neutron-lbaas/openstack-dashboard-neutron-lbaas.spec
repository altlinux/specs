
%define oname neutron-lbaas-dashboard

Name: openstack-dashboard-neutron-lbaas
Version: 2.0.0
Release: alt1
Summary: Horizon UI support for Neutron LBaaS
Group: System/Servers

License: ASL 2.0
Url: http://docs.openstack.org/developer/neutron-lbaas-dashboard/
Source:  %oname-%version.tar.gz

BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno >= 1.8.0
BuildRequires: python-module-paste
BuildRequires: python-module-PasteDeploy >= 1.5.0
BuildRequires: openstack-dashboard >= 11.0.0
BuildRequires: python-module-barbicanclient  >= 4.0.0

Requires: openstack-dashboard >= 11.0.0
Requires: python-module-barbicanclient >= 4.0.0
Requires: python-module-%oname = %EVR

Provides: neutron-lbaas-dashboard

%description
Horizon panels for Neutron LBaaS v2

%package doc
Summary: Documentation for Neutron LBaaS dashboard
Group: Development/Documentation

%description doc
Documentation for Neutron LBaaS dashboard

%package -n python-module-%oname
Summary: Horizon UI support for Neutron LBaaS
Group: Development/Python
Conflicts: openstack-dashboard-neutron-lbaas < 2.0.0-alt1

%description -n python-module-%oname
Horizon UI support for Neutron LBaaS

%package -n python-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python
Requires: python-module-%oname = %EVR

%description -n python-module-%oname-tests
This package contains tests for %oname.

%prep
%setup -n %oname-%version

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

%build
%python_build

sphinx-build doc/source html

# clean up files after sphinx
rm html/.buildinfo
rm -rf html/.doctrees

%install
%python_install

mkdir -p %buildroot%_datadir/openstack-dashboard/openstack_dashboard/local/enabled/
install -p -D -m 640 neutron_lbaas_dashboard/enabled/_148[01]_project* %buildroot%_datadir/openstack-dashboard/openstack_dashboard/local/enabled/

%files
%doc README.rst doc LICENSE
%_datadir/openstack-dashboard/openstack_dashboard/local/enabled/_148[01]*

%files -n python-module-%oname
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files -n python-module-%oname-tests
%python_sitelibdir/*/tests

%files doc
%doc html LICENSE

%changelog
* Thu Jun 15 2017 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt1
- 2.0.0
- add test package

* Tue Nov 22 2016 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- initial build
