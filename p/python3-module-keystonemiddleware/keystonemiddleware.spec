%define oname keystonemiddleware
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 10.2.0
Release: alt1.1

Summary: Middleware for OpenStack Identity

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/keystonemiddleware

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-keystoneauth1 >= 3.12.0
BuildRequires: python3-module-oslo.cache >= 1.26.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.context >= 2.19.2
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-pycadf >= 1.1.0
BuildRequires: python3-module-keystoneclient >= 3.8.0
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-webob >= 1.7.1
BuildRequires: python3-module-pbr >= 2.0.0

%if_with check
BuildRequires: python3-module-hacking >= 3.0
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-cryptography >= 3.0
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-testresources >= 2.0.0
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-webtest
BuildRequires: python3-module-oslo.messaging >= 5.29.0
BuildRequires: python3-module-bandit >= 1.1.0
BuildRequires: python3-module-requests-mock >= 1.2.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx >= 1.6.2
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-sphinxcontrib-apidoc >= 0.2.0
BuildRequires: python3-module-sphinxcontrib-rsvgconverter
%endif

%description
This package contains middleware modules designed to provide authentication
and authorization features to web services other than OpenStack Keystone.
The most prominent module is keystonemiddleware.auth_token.
This package does not expose any CLI or Python API features.

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
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 10.2.0-alt1.1
- Moved on modern pyproject macros.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 10.2.0-alt1
- Automatically updated to 10.2.0.

* Sat Oct 15 2022 Grigory Ustinov <grenka@altlinux.org> 10.1.0-alt2
- Spec refactoring.

* Tue Oct 11 2022 Grigory Ustinov <grenka@altlinux.org> 10.1.0-alt1
- Automatically updated to 10.1.0.

* Sat Oct 08 2022 Grigory Ustinov <grenka@altlinux.org> 9.4.0-alt1
- Automatically updated to 9.4.0.
- Unified (thx for felixz@).

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 9.0.0-alt1
- Automatically updated to 9.0.0.
- Renamed spec file.
- Build with docs.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 7.0.1-alt1
- Automatically updated to 7.0.1.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 6.0.0-alt1
- Automatically updated to 6.0.0

* Tue Dec 18 2018 Alexey Shabalin <shaba@altlinux.org> 5.2.0-alt1
- 5.2.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.14.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 29 2017 Alexey Shabalin <shaba@altlinux.ru> 4.14.0-alt1
- 4.14.0
- add test packages

* Wed Feb 01 2017 Alexey Shabalin <shaba@altlinux.ru> 4.9.1-alt1
- 4.9.1

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 4.9.0-alt1
- 4.9.0

* Tue Apr 12 2016 Alexey Shabalin <shaba@altlinux.ru> 4.4.0-alt1
- 4.4.0

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 2.3.3-alt1
- 2.3.3

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.3.1-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Mon Aug 24 2015 Alexey Shabalin <shaba@altlinux.ru> 1.5.2-alt1
- 1.5.2

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Fri Mar 06 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- Initial package.
