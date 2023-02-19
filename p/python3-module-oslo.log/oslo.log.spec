%define oname oslo.log
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 5.1.0
Release: alt1

Summary: OpenStack Oslo Log library

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/oslo.log

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

Provides: python3-module-oslo-log = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr >= 3.1.1
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.context >= 2.21.0
BuildRequires: python3-module-oslo.i18n >= 3.20.0
BuildRequires: python3-module-oslo.utils >= 3.36.0
BuildRequires: python3-module-oslo.serialization >= 2.25.0
BuildRequires: python3-module-debtcollector >= 1.19.0
BuildRequires: python3-module-pyinotify >= 0.9.6
BuildRequires: python3-module-dateutil >= 2.5.3

%if_with check
BuildRequires: python3-module-hacking >= 2.0.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-testtools >= 2.3.0
BuildRequires: python3-module-oslotest >= 3.3.0
BuildRequires: python3-module-coverage >= 4.5.1
BuildRequires: python3-module-bandit >= 1.6.0
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-pre-commit >= 2.6.0
BuildRequires: python3-module-eventlet >= 0.30.1
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
%endif

%description
OpenStack logging configuration library provides standardized configuration for
all openstack projects. It also provides custom formatters, handlers and
support for context specific logging (like resource id's etc).

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
Provides: python3-module-oslo-log-doc = %EVR

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
install -pDm 644 man/oslolog.1 %buildroot%_man1dir/oslolog.1
%endif

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%_bindir/convert-json
%python3_sitelibdir/oslo_log
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/oslo_log/tests

%files tests
%python3_sitelibdir/oslo_log/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/oslolog.1.xz
%endif

%changelog
* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 5.1.0-alt1
- Automatically updated to 5.1.0.

* Sat Oct 15 2022 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt3
- Spec refactoring.

* Wed Oct 12 2022 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt2
- Added manual.

* Sat Oct 08 2022 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt1
- Automatically updated to 5.0.0.
- Unified.

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 4.1.3-alt1
- Automatically updated to 4.1.3.
- Unify documentation building.
- Removed watch file.
- Fix license.

* Thu Jan 09 2020 Grigory Ustinov <grenka@altlinux.org> 3.45.2-alt1
- Automatically updated to 3.45.2.
- Added watch file.

* Fri Dec 27 2019 Grigory Ustinov <grenka@altlinux.org> 3.45.1-alt1
- Automatically updated to 3.45.1.
- Added watch file.
- Renamed spec file.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 3.44.1-alt1
- Automatically updated to 3.44.1.
- Build without python2.

* Tue Dec 11 2018 Alexey Shabalin <shaba@altlinux.org> 3.39.2-alt1
- 3.39.2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.20.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu May 25 2017 Alexey Shabalin <shaba@altlinux.ru> 3.20.1-alt1
- 3.20.1

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 3.16.0-alt1
- 3.16.0

* Thu Jun 16 2016 Lenar Shakirov <snejok@altlinux.ru> 3.3.0-alt2
- Fix urllib3 import in _options.py

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 3.3.0-alt1
- 3.3.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.11.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.11.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 1.11.0-alt1
- 1.11.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- Initial release
