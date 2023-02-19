%define oname barbicanclient
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 5.5.0
Release: alt1.1

Summary: Client Library for OpenStack Barbican Key Management API

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/python-barbicanclient

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-cliff >= 2.8.0
BuildRequires: python3-module-keystoneauth1 >= 5.1.1
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 3.33.0

%if_with check
BuildRequires: python3-module-coverage >= 4.1
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-hacking >= 3.1.0
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-requests-mock >= 1.2.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-sphinxcontrib-rsvgconverter
%endif

%description
There is a Python library for accessing the API (barbicanclient module),
and a command-line script (barbican).

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
install -pDm 644 man/python-%oname.1 %buildroot%_man1dir/%oname.1
%endif

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%_bindir/barbican
%python3_sitelibdir/%oname
%python3_sitelibdir/python_barbicanclient-%version.dist-info
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 5.5.0-alt1.1
- Moved on modern pyproject macros.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 5.5.0-alt1
- Automatically updated to 5.5.0.

* Mon Oct 10 2022 Grigory Ustinov <grenka@altlinux.org> 5.4.0-alt1
- Automatically updated to 5.4.0.

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 4.10.0-alt2
- Unify documentation building.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 4.10.0-alt1
- Automatically updated to 4.10.0.
- Renamed spec file.

* Fri Oct 18 2019 Grigory Ustinov <grenka@altlinux.org> 4.9.0-alt1
- Automatically updated to 4.9.0.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 4.8.1-alt1
- Automatically updated to 4.8.1

* Mon Dec 10 2018 Alexey Shabalin <shaba@altlinux.org> 4.7.1-alt1
- 4.7.1

* Tue Oct 09 2018 Grigory Ustinov <grenka@altlinux.org> 4.7.0-alt1
- Autoupdated to 4.7.0.

* Fri Jul 20 2018 Grigory Ustinov <grenka@altlinux.org> 4.6.0-alt1
- new version 4.6.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 30 2017 Alexey Shabalin <shaba@altlinux.ru> 4.2.0-alt1
- 4.2.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 4.1.0-alt1
- 4.1.0

* Thu Apr 14 2016 Alexey Shabalin <shaba@altlinux.ru> 4.0.1-alt1
- 4.0.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.3.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.3.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 3.3.0-alt1
- 3.3.0

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 3.0.3-alt1
- 3.0.3

* Thu Mar 12 2015 Alexey Shabalin <shaba@altlinux.ru> 3.0.2-alt1
- Initial release for Sisyphus

