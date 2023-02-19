%define oname zaqarclient
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 2.5.1
Release: alt1

Summary: Client Library for OpenStack Zaqar Messaging API

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/python-zaqarclient

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-jsonschema >= 2.6.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-osc-lib >= 1.8.0

%if_with check
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-mock >= 2.0.0
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-stestr >= 1.0.0
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-ddt >= 1.0.1
BuildRequires: python3-module-osc-lib-tests
BuildRequires: python3-module-hacking >= 3.0
BuildRequires: python3-module-requests-mock >= 1.2.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme
%endif

%description
%summary.

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
install -pDm 644 man/python-%oname.1 %buildroot%_man1dir/%oname.1
%endif

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/python_zaqarclient-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 2.5.1-alt1
- Automatically updated to 2.5.1.

* Mon Oct 10 2022 Grigory Ustinov <grenka@altlinux.org> 2.4.0-alt1
- Automatically updated to 2.4.0.

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 1.13.1-alt2
- Unify documentation building.
- Add tests subpackage.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 1.13.1-alt1
- Automatically updated to 1.13.1.

* Fri Dec 27 2019 Grigory Ustinov <grenka@altlinux.org> 1.12.0-alt1
- Automatically updated to 1.12.0.

* Fri Oct 25 2019 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt2
- Build without python2.
- Build without docs=(.

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Nov 03 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2.0-alt1
- Initial build.


