%define oname oslo.i18n

%define _unpackaged_files_terminate_build 1

%def_without bootstrap
%if_with bootstrap
%def_disable check
%else
%def_enable check
%endif

Name: python3-module-%oname
Version: 4.0.1
Release: alt2

Summary: OpenStack i18n library

Group: Development/Python3
License: Apache-2.0
Url: http://docs.openstack.org/developer/oslo.i18n

Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

Provides: python3-module-oslo-i18n = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0

%if_without bootstrap
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-oslo.config >= 3.14.0

BuildRequires: python3-module-sphinx >= 1.2.1
BuildRequires: python3-module-reno >= 1.8.0
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-sphinxcontrib-apidoc

%if_enabled check
BuildRequires: python3-module-stestr
BuildRequires: python3-module-oslotest
%endif
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
The oslo.i18n library contain utilities for working with internationalization
(i18n) features, especially translation for text strings in an application
or library.

This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack i18n library
Group: Development/Documentation
Provides: python-module-oslo-i18n-doc = %EVR

%description doc
Documentation for the oslo.i18n library.

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rf %oname.egg-info

sed -i '/warning-is-error/d' setup.cfg

%build
%python3_build

%if_without bootstrap
export PYTHONPATH="$PWD"

# generate html docs
sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%python3_install

%check
stestr run

%files
%doc *.rst LICENSE
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%if_without bootstrap
%files tests
%python3_sitelibdir/*/tests

%files doc
%doc LICENSE html
%endif

%changelog
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
