%define oname oslo.utils
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 6.1.0
Release: alt1

Summary: OpenStack Oslo Utility library

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/oslo.utils

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

Provides: python3-module-oslo-utils = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-iso8601 >= 0.1.11
BuildRequires: python3-module-netaddr >= 0.7.18
BuildRequires: python3-module-netifaces >= 0.10.4
BuildRequires: python3-module-pytz >= 2013.6
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-pyparsing >= 2.1.0
BuildRequires: python3-module-packaging >= 20.4

%if_with check
BuildRequires: python3-module-eventlet >= 0.18.2
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-testscenarios >= 0.4
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-ddt >= 1.0.1
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-bandit >= 1.6.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-pre-commit >= 2.6.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme
%endif

%description
The Oslo utils library provides support for common utility type functions,
such as encoding, exception handling, string manipulation, and time handling.

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
Provides: python3-module-oslo-utils-doc = %EVR

%description doc
This package contains documentation for %oname.
%endif

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rfv *.egg-info

%build
%python3_build

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
%python3_install

%if_with docs
# install man page
install -pDm 644 man/osloutils.1 %buildroot%_man1dir/osloutils.1
%endif

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%python3_sitelibdir/oslo_utils
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/oslo_utils/tests

%files tests
%python3_sitelibdir/oslo_utils/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/osloutils.1.xz
%endif

%changelog
* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 6.1.0-alt1
- Automatically updated to 6.1.0.

* Sat Oct 15 2022 Grigory Ustinov <grenka@altlinux.org> 6.0.1-alt2
- Spec refactoring.

* Tue Oct 11 2022 Grigory Ustinov <grenka@altlinux.org> 6.0.1-alt1
- Automatically updated to 6.0.1.

* Sat Oct 08 2022 Grigory Ustinov <grenka@altlinux.org> 4.13.0-alt1
- Automatically updated to 4.13.0.
- Unified (thx for felixz@).

* Sat Jul 24 2021 Grigory Ustinov <grenka@altlinux.org> 4.1.1-alt2
- Fixed BuildRequires.

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 4.1.1-alt1
- Automatically updated to 4.1.1.
- Unify documentation building.
- Fix license.

* Fri Dec 27 2019 Grigory Ustinov <grenka@altlinux.org> 3.42.1-alt1
- Automatically updated to 3.42.1.
- Added watch file.
- Renamed spec file.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 3.41.2-alt1
- Automatically updated to 3.41.2.
- Build without python2.

* Sun Aug 18 2019 Grigory Ustinov <grenka@altlinux.org> 3.40.3-alt1
- Automatically updated to 3.40.3

* Thu Dec 06 2018 Alexey Shabalin <shaba@altlinux.org> 3.36.4-alt1
- 3.36.4

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.22.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jul 18 2017 Alexey Shabalin <shaba@altlinux.ru> 3.22.1-alt1
- 3.22.1

* Tue May 02 2017 Alexey Shabalin <shaba@altlinux.ru> 3.22.0-alt1
- 3.22.0

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 3.16.0-alt1
- 3.16.0

* Fri Apr 08 2016 Alexey Shabalin <shaba@altlinux.ru> 3.8.0-alt1
- 3.8.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.5.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.5.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Mon Feb 16 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- Initial package.
