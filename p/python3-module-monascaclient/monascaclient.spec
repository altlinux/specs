%define oname monascaclient
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 2.6.0
Release: alt1.1

Summary: OpenStack Monasca API Client Library

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/python-monascaclient

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-osc-lib >= 1.8.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-babel
BuildRequires: python3-module-iso8601 >= 0.1.11
BuildRequires: python3-module-prettytable >= 0.7.2
BuildRequires: python3-module-yaml >= 3.12

%if_with check
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-bandit >= 1.1.0
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-stestr >= 1.0.0
BuildRequires: python3-module-testscenarios >= 0.4
BuildRequires: python3-module-testtools >= 2.2.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx >= 1.6.5
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-doc8 >= 0.8.1
%endif

%description
This is a client library for Monasca built to interface with the Monasca API.
It provides a Python API (the monascaclient module) and a command-line tool
(monasca).

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%if_with docs
%package doc
Summary: Documentation for %oname
Group: Development/Documentation

%description doc
This package contains documentation for %oname.
%endif

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rfv *.egg-info

%build
%pyproject_build

%if_with docs
export PYTHONPATH="$PWD"
# generate html docs
sphinx-build-3 doc/source html
# generate man page
sphinx-build-3 -b man doc/source man
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install

%if_with docs
# install man page
install -pDm 644 man/python-%oname.1 %buildroot%_man1dir/%oname.1
%endif

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%_bindir/monasca
%python3_sitelibdir/%oname
%python3_sitelibdir/python_monascaclient-%version.dist-info
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 2.6.0-alt1.1
- Moved on modern pyproject macros.

* Thu Oct 20 2022 Grigory Ustinov <grenka@altlinux.org> 2.6.0-alt1
- Automatically updated to 2.6.0.

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
