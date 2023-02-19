%define oname automaton
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 3.1.0
Release: alt1.1

Summary: OpenStack Friendly state machines for python

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/automaton

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-prettytable >= 0.7.2

%if_with check
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-reno >= 3.1.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx >= 1.1.2
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
%endif

%description
Friendly state machines for python. The goal of this library is to provide well
documented state machine classes and associated utilities. The state machine
pattern (or the implemented variation there-of) is a commonly used pattern
and has a multitude of various usages. Some of the usages for this library
include providing state & transition validation and running/scheduling/analyzing
the execution of tasks.

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
install -pDm 644 man/%oname.1 %buildroot%_man1dir/%oname.1
%endif

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
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

* Fri Oct 07 2022 Grigory Ustinov <grenka@altlinux.org> 2.5.0-alt1
- Automatically updated to 2.5.0.
- Unified (thx for felixz@).

* Tue Nov 03 2020 Vitaly Lipatov <lav@altlinux.ru> 2.2.0-alt1
- NMU: new version 2.2.0 (with rpmrb script), cleanup spec
- NMU: temp. disable tests (needs old coverage module)

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 2.0.1-alt1
- Automatically updated to 2.0.1.
- Renamed spec file.
- Build with check.

* Wed Dec 18 2019 Grigory Ustinov <grenka@altlinux.org> 1.15.0-alt2
- Build without python2.

* Sat Dec 08 2018 Alexey Shabalin <shaba@altlinux.org> 1.15.0-alt1
- 1.15.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Mar 01 2017 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 0.7.0-alt1
- Initial release
