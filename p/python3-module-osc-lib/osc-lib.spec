%define oname osc-lib

Name: python3-module-%oname
Version: 1.15.0
Release: alt1
Summary: OpenStackClient (aka OSC) is a command-line client for OpenStack
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
BuildRequires: python3-module-cliff >= 2.8.0
BuildRequires: python3-module-keystoneauth1 >= 3.7.0
BuildRequires: python3-module-openstacksdk >= 0.15.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-simplejson >= 3.5.1
BuildRequires: python3-module-stevedore >= 1.20.0

# doc
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinxcontrib-apidoc
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0

%description
OpenStackClient (aka OSC) is a command-line client for OpenStack.
osc-lib is a package of common support modules for writing OSC plugins.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack %oname library
Group: Development/Documentation

%description doc
Documentation for OpenStack %oname library

%prep
%setup -n %oname-%version
# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

%build
%python3_build

python3 setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr build/sphinx/html/.buildinfo

%install
%python3_install

%files
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Fri Dec 27 2019 Grigory Ustinov <grenka@altlinux.org> 1.15.0-alt1
- Automatically updated to 1.15.0.
- Added watch file.
- Renamed spec file.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 1.14.1-alt1
- Automatically updated to 1.14.1.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 1.12.1-alt1
- Automatically updated to 1.12.1

* Mon Aug 05 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.11.1-alt2
- Fix work with python 3.7

* Mon Dec 10 2018 Alexey Shabalin <shaba@altlinux.org> 1.11.1-alt1
- 1.11.1

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 30 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.0-alt1
- 1.3.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- Initial packaging
