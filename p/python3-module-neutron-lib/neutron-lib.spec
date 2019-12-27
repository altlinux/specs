%define oname neutron-lib

Name: python3-module-%oname
Version: 1.30.0
Release: alt1
Summary: OpenStack Neutron shared routines and utilities
Group: Development/Python3
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-SQLAlchemy >= 1.0.10
BuildRequires: python3-module-pecan >= 1.0.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-oslo.concurrency >= 3.26.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.context >= 2.19.2
BuildRequires: python3-module-oslo.db >= 4.37.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.messaging >= 5.29.0
BuildRequires: python3-module-oslo.policy >= 1.30.0
BuildRequires: python3-module-oslo.service >= 1.24.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-oslo.versionedobjects >= 1.31.2
BuildRequires: python3-module-osprofiler >= 1.4.0
BuildRequires: python3-module-webob >= 1.7.1

# doc
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-os-api-ref >= 1.4.0
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-mock >= 2.0.0

%description
Neutron-lib is an OpenStack library project used by Neutron, Advanced Services,
and third-party projects to provide common functionality and remove duplication.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack Neutron shared routines and utilities
Group: Development/Documentation

%description doc
Documentation for OpenStack Neutron shared routines and utilities

%prep
%setup -n %oname-%version

%build
%python3_build

# generate html docs
python3 setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf build/sphinx/html/.{doctrees,buildinfo}

%install
%python3_install

%files
%doc AUTHORS ChangeLog README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/neutron_lib/fixture.py

%files tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/neutron_lib/fixture.py

%files doc
%doc build/sphinx/html

%changelog
* Fri Dec 27 2019 Grigory Ustinov <grenka@altlinux.org> 1.30.0-alt1
- Automatically updated to 1.30.0.
- Added watch file.
- Renamed spec file.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 1.29.1-alt1
- Automatically updated to 1.29.1.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 1.25.0-alt1
- Automatically updated to 1.25.0

* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 1.18.0-alt1
- 1.18.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 30 2017 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- 1.1.0
- add test packages

* Fri Oct 21 2016 Alexey Shabalin <shaba@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Fri Apr 15 2016 Alexey Shabalin <shaba@altlinux.ru> 0.0.1-alt1
- Initial package.
