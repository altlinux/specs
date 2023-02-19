%define oname oslo.context
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 5.1.0
Release: alt1.1

Summary: OpenStack Oslo Context library

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/oslo.context

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

Provides: python3-module-oslo-context = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-debtcollector >= 1.2.0

%if_with check
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-mypy >= 0.761
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-bandit >= 1.6.0
BuildRequires: python3-module-pre-commit >= 2.6.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx >= 1.6.2
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
%endif

%description
The Oslo context library has helpers to maintain useful information
about a request context. The request context is usually populated in
the WSGI pipeline and used by various modules such as logging.

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
Provides: python3-module-oslo-context-doc = %EVR

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
install -pDm 644 man/oslocontext.1 %buildroot%_man1dir/oslocontext.1
%endif

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%python3_sitelibdir/oslo_context
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/oslo_context/tests

%files tests
%python3_sitelibdir/oslo_context/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/oslocontext.1.xz
%endif

%changelog
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 5.1.0-alt1.1
- Moved on modern pyproject macros.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 5.1.0-alt1
- Automatically updated to 5.1.0.

* Sat Oct 15 2022 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt2
- Spec refactoring.

* Tue Oct 11 2022 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt1
- Automatically updated to 5.0.0.

* Fri Oct 07 2022 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt1
- Automatically updated to 4.1.0.
- Unified (thx for felixz@).

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 3.0.2-alt1
- Automatically updated to 3.0.2.
- Renamed spec file.
- Unify documentation building.
- Fix license.

* Fri Sep 20 2019 Grigory Ustinov <grenka@altlinux.org> 2.23.0-alt1
- new version 2.23.0
- Build without python2.

* Thu Dec 06 2018 Alexey Shabalin <shaba@altlinux.org> 2.21.0-alt1
- 2.21.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.12.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jul 18 2017 Alexey Shabalin <shaba@altlinux.ru> 2.12.2-alt1
- 2.12.2

* Wed May 24 2017 Alexey Shabalin <shaba@altlinux.ru> 2.12.1-alt1
- 2.12.1
- add test packages

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 2.9.0-alt1
- 2.9.0

* Fri Apr 08 2016 Alexey Shabalin <shaba@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2.0-alt1
- Initial release
