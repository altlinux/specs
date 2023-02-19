%define oname debtcollector
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 2.5.0
Release: alt1.1

Summary: A collection of Python deprecation patterns and strategies

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/debtcollector

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-wrapt >= 1.7.0

%if_with check
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-hacking >= 3.0
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-pre-commit >= 2.6.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx >= 2.0.0
BuildRequires: python3-module-reno >= 3.1.0
BuildRequires: python3-module-doc8 >= 0.8.1
BuildRequires: python3-module-openstackdocstheme >= 2.2.1
%endif

%description
A collection of Python deprecation patterns and strategies that help you collect
your technical debt in a non-destructive manner. The goal of this library is to
provide well documented developer facing deprecation patterns that start of with
a basic set and can expand into a larger set of patterns as time goes on.
The desired output of these patterns is to apply the warnings module to emit
DeprecationWarning or PendingDeprecationWarning or similar derivative
to developers using libraries (or potentially applications) about future
deprecations.

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
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 2.5.0-alt1.1
- Moved on modern pyproject macros.

* Wed Oct 19 2022 Grigory Ustinov <grenka@altlinux.org> 2.5.0-alt1
- Automatically updated to 2.5.0.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 2.0.1-alt1
- Automatically updated to 2.0.1.

* Thu Dec 19 2019 Grigory Ustinov <grenka@altlinux.org> 1.22.0-alt2
- Build without python2.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 1.22.0-alt1
- Automatically updated to 1.22.0.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 1.21.0-alt1
- Automatically updated to 1.21.0

* Mon Dec 17 2018 Alexey Shabalin <shaba@altlinux.org> 1.20.0-alt1
- 1.20.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.11.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Apr 28 2017 Alexey Shabalin <shaba@altlinux.ru> 1.11.0-alt1
- 1.11.0
- add tests package

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Fri Apr 08 2016 Alexey Shabalin <shaba@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 0.3.0-alt1
- Initial build
