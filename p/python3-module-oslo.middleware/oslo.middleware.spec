%define oname oslo.middleware
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 5.1.0
Release: alt1.1

Summary: OpenStack Oslo Middleware library

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/oslo.middleware

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

Provides: python3-module-oslo-middleware = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-jinja2 >= 2.10
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.context >= 2.19.2
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-webob >= 1.7.1
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-statsd >= 3.2.1
BuildRequires: python3-module-bcrypt >= 3.1.3

%if_with check
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-bandit >= 1.6.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-pre-commit >= 2.6.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0
%endif

%description
Oslo middleware library includes components that can be injected into
wsgi pipelines to intercept request/response flows. The base class can be
enhanced with functionality like add/delete/modification of http headers
and support for limiting size/connection etc.

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
Provides: python3-module-oslo-middleware-doc = %EVR

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
install -pDm 644 man/oslomiddleware.1 %buildroot%_man1dir/oslomiddleware.1
%endif

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%python3_sitelibdir/oslo_middleware
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/oslo_middleware/tests

%files tests
%python3_sitelibdir/oslo_middleware/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/oslomiddleware.1.xz
%endif

%changelog
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 5.1.0-alt1.1
- Moved on modern pyproject macros.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 5.1.0-alt1
- Automatically updated to 5.1.0.

* Tue Oct 18 2022 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt1
- Automatically updated to 5.0.0.

* Mon May 16 2022 Grigory Ustinov <grenka@altlinux.org> 4.5.1-alt1
- Automatically updated to 4.5.1.
- Build without check
- Build without docs

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 4.0.2-alt1
- Automatically updated to 4.0.2.
- Renamed spec file.
- Fix license.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 3.38.1-alt1
- Automatically updated to 3.38.1.
- Build without python2.

* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 3.36.0-alt1
- 3.36.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.23.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jul 18 2017 Alexey Shabalin <shaba@altlinux.ru> 3.23.2-alt1
- 3.23.2

* Thu May 25 2017 Alexey Shabalin <shaba@altlinux.ru> 3.23.1-alt1
- 3.23.1
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 3.19.0-alt1
- 3.19.0

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 3.8.0-alt1
- 3.8.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.8.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.8.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- Initial release
