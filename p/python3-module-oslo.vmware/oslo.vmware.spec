%define oname oslo.vmware
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 3.10.0
Release: alt1

Summary: Oslo VMware library for OpenStack projects

License: Apache-2.0
Group: Development/Python3
Url: https://docs.openstack.org/oslo.vmware/latest

Source: %name-%version.tar
Source1: %oname.watch

BuildArch: noarch

Provides: python3-module-oslo-vmware = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-netaddr >= 0.7.18
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-pyaml >= 3.13
BuildRequires: python3-module-lxml >= 4.5.0
BuildRequires: python3-module-suds >= 0.6
BuildRequires: python3-module-eventlet >= 0.18.2
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-urllib3 >= 1.21.1
BuildRequires: python3-module-oslo.concurrency >= 3.26.0
BuildRequires: python3-module-oslo.context >= 2.19.2

%if_with check
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-bandit >= 1.6.0
BuildRequires: python3-module-ddt >= 1.0.1
BuildRequires: python3-module-pre-commit >= 2.6.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-sphinxcontrib-apidoc
%endif

%description
The Oslo project intends to produce a python library containing infrastructure
code shared by OpenStack projects. The APIs provided by the project should be
high quality, stable, consistent and generally useful.

The Oslo VMware library offers session and API call management for VMware ESX/VC
server.

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
Provides: python3-module-oslo-vmware-doc = %EVR

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
* Sat Oct 08 2022 Grigory Ustinov <grenka@altlinux.org> 3.10.0-alt1
- Automatically updated to 3.10.0.
- Unified (thx for felixz@).

* Mon Apr 05 2021 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1.1
- FTBFS: use python3-module-suds instead of python3-module-suds-jurko.

* Fri Jun 05 2020 Grigory Ustinov <grenka@altlinux.org> 3.4.0-alt1
- Automatically updated to 3.4.0.
- Fix license.

* Fri Dec 27 2019 Grigory Ustinov <grenka@altlinux.org> 2.34.1-alt1
- Automatically updated to 2.34.1.
- Added watch file.
- Renamed spec file.

* Sat Oct 26 2019 Grigory Ustinov <grenka@altlinux.org> 2.31.0-alt2
- Build without python2.

* Mon Dec 10 2018 Alexey Shabalin <shaba@altlinux.org> 2.31.0-alt1
- 2.31.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.17.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jul 18 2017 Alexey Shabalin <shaba@altlinux.ru> 2.17.1-alt1
- 2.17.1

* Mon May 29 2017 Alexey Shabalin <shaba@altlinux.ru> 2.17.0-alt1
- 2.17.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 2.14.0-alt1
- 2.14.0

* Tue Apr 12 2016 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.21.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.21.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 1.21.0-alt1
- 1.21.0

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 0.11.1-alt1
- 0.11.1

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 0.11.0-alt1
- 0.11.0

* Fri Mar 06 2015 Alexey Shabalin <shaba@altlinux.ru> 0.7.0-alt1
- initial build
