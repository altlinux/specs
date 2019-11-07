%define oname os-win

Name: python3-module-%oname
Version: 4.3.2
Release: alt1
Summary: Windows Hyper-V library for OpenStack projects
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
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-eventlet >= 0.18.2
BuildRequires: python3-module-oslo.concurrency >= 3.26.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3

%description
Library contains Windows / Hyper-V code commonly used in the OpenStack
projects: nova, cinder, networking-hyperv. The library can be used in any
other OpenStack projects where it is needed.

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
rm -fr doc/build/html/.buildinfo

%install
%python3_install

%files
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc README.rst doc/build/html

%changelog
* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 4.3.2-alt1
- Automatically updated to 4.3.2.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 4.2.0-alt1
- Automatically updated to 4.2.0

* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 4.0.1-alt1
- 4.0.1

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jul 18 2017 Alexey Shabalin <shaba@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Mon May 29 2017 Alexey Shabalin <shaba@altlinux.ru> 1.4.1-alt1
- 1.4.1
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Wed Apr 13 2016 Alexey Shabalin <shaba@altlinux.ru> 0.4.1-alt1
- Initial packaging
