%define oname oslo.i18n
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 5.1.0
Release: alt1

Summary: OpenStack Oslo Internationalization Utilities

License: Apache-2.0
Group: Development/Python3
Url: https://docs.openstack.org/oslo.i18n/latest

Source: %name-%version.tar
Source1: %oname.watch

BuildArch: noarch

Provides: python3-module-oslo-i18n = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr >= 2.0.0

%if_with check
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-testscenarios >= 0.4
BuildRequires: python3-module-bandit >= 1.6.0
BuildRequires: python3-module-pre-commit >= 2.6.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx >= 1.2.1
BuildRequires: python3-module-reno >= 1.8.0
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-sphinxcontrib-apidoc
%endif

%description
The oslo.i18n library contain utilities for working with internationalization
(i18n) features, especially translation for text strings in an application
or library.

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
Provides: python3-module-oslo-i18n-doc = %EVR

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
* Sat Oct 08 2022 Grigory Ustinov <grenka@altlinux.org> 5.1.0-alt1
- Automatically updated to 5.1.0.
- Unified.

* Thu Jul 29 2021 Ivan A. Melnikov <iv@altlinux.org> 4.0.1-alt2
- Add bootstrap toggle.
- Add %%check section.

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 4.0.1-alt1
- Automatically updated to 4.0.1.
- Unify documentation building.
- Removed watch file.
- Fix license.

* Thu Jan 09 2020 Grigory Ustinov <grenka@altlinux.org> 3.25.1-alt1
- Automatically updated to 3.25.1.
- Added watch file.

* Fri Dec 27 2019 Grigory Ustinov <grenka@altlinux.org> 3.25.0-alt1
- Automatically updated to 3.25.0.
- Added watch file.
- Renamed spec file.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 3.24.0-alt1
- Automatically updated to 3.24.0.
- Build without python2.

* Mon Dec 17 2018 Alexey Shabalin <shaba@altlinux.org> 3.21.0-alt1
- Build new version.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.12.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Apr 28 2017 Alexey Shabalin <shaba@altlinux.ru> 3.12.0-alt1
- 3.12.0
- add tests package

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 3.9.0-alt1
- 3.9.0

* Fri Apr 08 2016 Alexey Shabalin <shaba@altlinux.ru> 3.5.0-alt1
- 3.5.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.6.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.6.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Oct 27 2015 Alexey Shabalin <shaba@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Mon Feb 16 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- Initial release
