%global oname cliff
%def_with docs
%def_with check

Name: python3-module-%oname
Version: 4.0.0
Release: alt2.2

Summary: OpenStack Command Line Interface Formulation Framework

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/cliff

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-prettytable >= 0.7.2
BuildRequires: python3-module-cmd2 >= 1.0.0
BuildRequires: python3-module-stevedore >= 2.0.1
BuildRequires: python3-module-yaml >= 3.10.0

%if_with check
BuildRequires: python3-module-sphinx >= 2.0.0
BuildRequires: python3-module-mock
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-stestr >= 1.0.0
BuildRequires: python3-module-testscenarios >= 0.4
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-bandit >= 1.1.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx >= 2.0.0
BuildRequires: python3-module-autopage
BuildRequires: python3-module-importlib-metadata
%endif

%description
cliff is a framework for building command line programs. It uses setuptools
entry points to provide subcommands, output formatters, and other extensions.

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
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt2.2
- Moved on modern pyproject macros.

* Fri Oct 21 2022 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt2.1
- Little spec fix.

* Sat Oct 15 2022 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt2
- Spec refactoring.

* Wed Oct 12 2022 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt1
- Automatically updated to 4.0.0.
- Unified.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 3.1.0-alt1
- Automatically updated to 3.1.0.
- Build with docs.

* Fri Dec 27 2019 Grigory Ustinov <grenka@altlinux.org> 2.17.0-alt1
- Automatically updated to 2.17.0.
- Added watch file.
- Renamed spec file.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 2.16.0-alt1
- Automatically updated to 2.16.0.
- Build without python2.
- Build without docs.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 2.14.1-alt1
- Automatically updated to 2.14.1

* Fri Jan 25 2019 Stanislav Levin <slev@altlinux.org> 2.13.0-alt2
- Dropped BR and RR on python argparse.

* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 2.13.0-alt1
- 2.13.0

* Mon Nov 19 2018 Leontiy Volodin <lvol@altlinux.org> 2.4.0-alt2
- fixed build
- added patch for tests

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.4.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 29 2017 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt1
- 2.4.0
- add test packages
- add doc package

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.15.0-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.15.0-alt2.1
- NMU: Use buildreq for BR.

* Tue Nov 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.15.0-alt2
- update R:

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 1.15.0-alt1
- 1.15.0

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12.0-alt1
- Version 1.12.0

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 1.10.1-alt1
- 1.10.1

* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1
- Version 1.9.0
- Added module for Python 3

* Tue Aug 05 2014 Lenar Shakirov <snejok@altlinux.ru> 1.6.1-alt1
- New version

* Mon Sep 30 2013 Pavel Shilovsky <piastry@altlinux.org> 1.0-alt2
- Remove distribute bootstrap
- Fix check section in spec

* Thu Sep 27 2012 Pavel Shilovsky <piastry@altlinux.org> 1.0-alt1
- Initial release for Sisyphus (based on Fedora)
