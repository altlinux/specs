%define oname futurist
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 2.4.1
Release: alt1.1

Summary: Useful additions to futures, from the future

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/futurist

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 2.0.0

%if_with check
BuildRequires: python3-module-contextlib2 >= 0.4.0
BuildRequires: python3-module-prettytable >= 0.7.1
BuildRequires: python3-module-eventlet >= 0.18.2
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-testscenarios >= 0.4
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-pre-commit >= 2.6.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme
BuildRequires: python3-module-doc8 >= 0.6.0
%endif

%description
Code from the future, delivered to you in the now. The goal of this library
would be to provide a well documented futures classes/utilities/additions that
allows for providing a level of transparency in how asynchronous work
gets executed. This library currently adds statistics gathering,
an eventlet executor, a synchronous executor etc.

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
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 2.4.1-alt1.1
- Moved on modern pyproject macros.

* Wed Oct 19 2022 Grigory Ustinov <grenka@altlinux.org> 2.4.1-alt1
- Automatically updated to 2.4.1.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 2.1.1-alt1
- Automatically updated to 2.1.1.
- Renamed spec file.

* Thu Dec 19 2019 Grigory Ustinov <grenka@altlinux.org> 1.10.0-alt1
- Automatically updated to 1.10.0.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 1.9.0-alt1
- Automatically updated to 1.9.0.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 1.8.1-alt1
- Automatically updated to 1.8.1

* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 1.7.0-alt1
- 1.7.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.21.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 11 2017 Alexey Shabalin <shaba@altlinux.ru> 0.21.1-alt1
- 0.21.1

* Fri Apr 28 2017 Alexey Shabalin <shaba@altlinux.ru> 0.21.0-alt1
- 0.21.0
- add tests package

* Wed Feb 01 2017 Alexey Shabalin <shaba@altlinux.ru> 0.18.0-alt1
- 0.18.0

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 0.13.0-alt1
- 0.13.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- Initial package.
