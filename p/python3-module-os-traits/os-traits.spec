%define oname os-traits

Name: python3-module-%oname
Version: 2.1.0
Release: alt1

Summary: A library containing standardized trait strings

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
BuildRequires: python3-module-reno >= 0.8.0
BuildRequires: python3-module-openstackdocstheme

%description
Traits are strings that represent a feature of some resource provider.  This
library contains the catalog of constants that have been standardized in the
OpenStack community to refer to a particular hardware, virtualization, storage,
network, or device trait.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for %oname
Group: Development/Documentation

%description doc
Documentation for OpenStack os-brick library

%prep
%setup -n %oname-%version
# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

sed -i '/warning-is-error/d' setup.cfg

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
* Fri Dec 27 2019 Grigory Ustinov <grenka@altlinux.org> 2.1.0-alt1
- Automatically updated to 2.1.0.
- Added watch file.
- Renamed spec file.

* Wed Oct 23 2019 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt1
- new version 1.1.0
- Build without python2.

* Wed Jan 09 2019 Alexey Shabalin <shaba@altlinux.org> 0.9.0-alt1
- Initial packaging
