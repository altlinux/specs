%define oname osc-lib
%def_without check
%def_with docs

Name: python3-module-%oname
Version: 2.5.0
Release: alt1

Summary: OpenStackClient (aka OSC) is a command-line client for OpenStack

License: Apache-2.0
Group: Development/Python3
Url: https://docs.openstack.org/osc-lib/latest

Source: %name-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-cliff
BuildRequires: python3-module-keystoneauth1 >= 3.14.0
BuildRequires: python3-module-openstacksdk >= 0.15.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-simplejson >= 3.5.1
BuildRequires: python3-module-stevedore >= 1.20.0

%if_with check
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-requests-mock >= 1.1.0
BuildRequires: python3-module-stestr >= 1.0.0
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-osprofiler >= 1.4.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinxcontrib-apidoc
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0
%endif

%description
OpenStackClient (aka OSC) is a command-line client for OpenStack.
osc-lib is a package of common support modules for writing OSC plugins.

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
%setup

# Remove bundled egg-info
rm -rfv %oname.egg-info

%build
%python3_build

%if_with docs
export PYTHONPATH="$PWD"
# generate html docs
sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%python3_install

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%endif

%changelog
* Sat Oct 08 2022 Grigory Ustinov <grenka@altlinux.org> 2.5.0-alt1
- Automatically updated to 2.5.0.
- Unified (thx for felixz@).
- Built without check.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1
- Automatically updated to 2.0.0.

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
