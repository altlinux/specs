%define oname oslo.versionedobjects
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 3.1.0
Release: alt1.1

Summary: OpenStack Oslo Versioned Objects library

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/oslo.versionedobjects

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

Provides: python3-module-oslo-versionedobjects = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-oslo.concurrency >= 3.26.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.context >= 2.19.2
BuildRequires: python3-module-oslo.messaging >= 5.29.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 4.7.0
BuildRequires: python3-module-iso8601 >= 0.1.11
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-webob >= 1.7.1
BuildRequires: python3-module-netaddr >= 0.7.18

%if_with check
BuildRequires: python3-module-hacking >= 3.1.0
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-jsonschema >= 3.2.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-bandit >= 1.6.0
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-pre-commit >= 2.6.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx >= 2.0.0
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
%endif

%description
The oslo.versionedobjects library provides a generic versioned object model
that is RPC-friendly, with inbuilt serialization, field typing, and remotable
method calls. It can be used to define a data model within a project independent
of external APIs or database schema for the purposes of providing upgrade
compatibility across distributed services.

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
Provides: python3-module-oslo-versionedobjects-doc = %EVR

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
install -pDm 644 man/osloversionedobjects.1 %buildroot%_man1dir/osloversionedobjects.1
%endif

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%python3_sitelibdir/oslo_versionedobjects
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/oslo_versionedobjects/tests
%exclude %python3_sitelibdir/oslo_versionedobjects/test.py

%files tests
%python3_sitelibdir/oslo_versionedobjects/tests
%python3_sitelibdir/oslo_versionedobjects/test.py

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/osloversionedobjects.1.xz
%endif

%changelog
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 3.1.0-alt1.1
- Moved on modern pyproject macros.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 3.1.0-alt1
- Automatically updated to 3.1.0.

* Sat Oct 15 2022 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt2
- Spec refactoring.

* Tue Oct 11 2022 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt1
- Automatically updated to 3.0.1.

* Sat Oct 08 2022 Grigory Ustinov <grenka@altlinux.org> 2.6.0-alt1
- Automatically updated to 2.6.0.
- Unified (thx for felixz@).

* Tue Apr 06 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.2-alt1.1
- FTBFS: remove requirement of test from main module.

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 2.0.2-alt1
- Automatically updated to 2.0.2.
- Fix license.

* Thu Jan 09 2020 Grigory Ustinov <grenka@altlinux.org> 1.37.0-alt1
- Automatically updated to 1.37.0.
- Added watch file.
- Renamed spec file.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 1.36.1-alt1
- Automatically updated to 1.36.1.
- Build without python2.

* Fri Aug 23 2019 Grigory Ustinov <grenka@altlinux.org> 1.36.0-alt1
- new version 1.36.0

* Mon Dec 10 2018 Alexey Shabalin <shaba@altlinux.org> 1.33.3-alt1
- 1.33.3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.21.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 11 2017 Alexey Shabalin <shaba@altlinux.ru> 1.21.1-alt1
- 1.21.1

* Fri May 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1.21.0-alt1
- 1.21.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.17.0-alt1
- 1.17.0

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.10.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt1
- 0.10.0

* Mon Jun 01 2015 Alexey Shabalin <shaba@altlinux.ru> 0.1.1-alt1
- Initial release
