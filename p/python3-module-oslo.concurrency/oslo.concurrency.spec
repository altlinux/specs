%define oname oslo.concurrency
# Tests are broken very strange, w8 for upstream solution=(
%def_without check
%def_with docs

Name: python3-module-%oname
Version: 5.0.1
Release: alt3.2

Summary: OpenStack Oslo Concurrency library

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/oslo.concurrency

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

Provides: python3-module-oslo-concurrency = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-fasteners >= 0.7.0

%if_with check
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-eventlet >= 0.19.0
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-bandit >= 1.6.0
BuildRequires: python3-module-pre-commit >= 2.6.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme
BuildRequires: python3-module-sphinxcontrib-apidoc
%endif

%description
Oslo concurrency library has utilities for safely running multi-thread,
multi-process applications using locking mechanisms and for running
external processes.

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
Provides: python3-module-oslo-concurrency-doc = %EVR

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
install -pDm 644 man/osloconcurrency.1 %buildroot%_man1dir/osloconcurrency.1
%endif

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%_bindir/lockutils-wrapper
%python3_sitelibdir/oslo_concurrency
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/oslo_concurrency/tests

%files tests
%python3_sitelibdir/oslo_concurrency/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/osloconcurrency.1.xz
%endif

%changelog
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 5.0.1-alt3.2
- Moved on modern pyproject macros.

* Fri Oct 21 2022 Grigory Ustinov <grenka@altlinux.org> 5.0.1-alt3.1
- Little spec fix.

* Sat Oct 15 2022 Grigory Ustinov <grenka@altlinux.org> 5.0.1-alt3
- Spec refactoring.

* Wed Oct 12 2022 Grigory Ustinov <grenka@altlinux.org> 5.0.1-alt2
- Added manual.

* Sat Oct 08 2022 Grigory Ustinov <grenka@altlinux.org> 5.0.1-alt1
- Automatically updated to 5.0.1.
- Unified (thx for felixz@).
- Built without check.

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 4.0.2-alt1
- Automatically updated to 4.0.2.
- Unify documentation building.
- Fix license.

* Thu Dec 19 2019 Grigory Ustinov <grenka@altlinux.org> 3.31.0-alt1
- Automatically updated to 3.31.0.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 3.30.0-alt1
- Automatically updated to 3.30.0.
- Build without python2.

* Thu Dec 13 2018 Alexey Shabalin <shaba@altlinux.org> 3.27.0-alt1
- Build new version.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.18.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed May 24 2017 Alexey Shabalin <shaba@altlinux.ru> 3.18.0-alt1
- 3.18.0
- add test packages

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 3.14.0-alt1
- 3.14.0

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 3.7.0-alt1
- 3.7.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.6.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.6.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Oct 27 2015 Alexey Shabalin <shaba@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Mon Aug 24 2015 Alexey Shabalin <shaba@altlinux.ru> 1.8.2-alt1
- 1.8.2

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.7.0-alt1
- Initial release
