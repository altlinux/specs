%define oname monascaclient

Name:       python3-module-%oname
Version:    2.1.0
Release:    alt2

Summary:    Python API and CLI for OpenStack Monasca

Group:      Development/Python3
License:    Apache-2.0
Url:        http://docs.openstack.org/developer/python-%oname

Source:     https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz

BuildArch:  noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-osc-lib >= 1.8.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-iso8601 >= 0.1.11
BuildRequires: python3-module-prettytable >= 0.7.2
BuildRequires: python3-module-yaml >= 3.12

BuildRequires: python3-module-sphinx >= 1.6.5
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-doc8 >= 0.6.0

%description
This is a client library for Monasca built to interface with the Monasca API. It
provides a Python API the monascaclient module and a command-line tool
monasca.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack Monasca API Client
Group: Development/Documentation

%description doc
This is a client library for Monasca built to interface with the Monasca API. It
provides a Python API the monascaclient module and a command-line tool
monasca.

This package contains documentation for %oname.

%prep
%setup -n python-%oname-%version

# Let RPM handle the dependencies
rm -f {,test-}requirements.txt

%build
%python3_build

export PYTHONPATH="$PWD"

# generate html docs
sphinx-build-3 doc/source html
# generate man page
sphinx-build-3 -b man doc/source man
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%python3_install

# install man page
install -p -D -m 644 man/python-monascaclient.1 %buildroot%_man1dir/monascaclient.1

%files
%doc *.rst LICENSE
%_bindir/monasca
%_man1dir/monascaclient*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc LICENSE html

%changelog
* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 2.1.0-alt2
- Unify documentation building.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 2.1.0-alt1
- Automatically updated to 2.1.0.
- Renamed spec file.

* Fri Oct 18 2019 Grigory Ustinov <grenka@altlinux.org> 1.16.0-alt1
- Automatically updated to 1.16.0.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 1.15.0-alt1
- Automatically updated to 1.15.0

* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 1.12.1-alt1
- Updated to 1.12.1.
- Added building docs.

* Fri Jul 20 2018 Grigory Ustinov <grenka@altlinux.org> 1.10.0-alt1
- new version 1.10.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.5.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed May 31 2017 Alexey Shabalin <shaba@altlinux.ru> 1.5.0-alt1
- 1.5.0
- add test packages

* Tue Nov 22 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- Initial release for Sisyphus
