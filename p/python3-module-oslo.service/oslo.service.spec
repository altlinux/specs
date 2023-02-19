%define oname oslo.service
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 3.1.0
Release: alt1

Summary: OpenStack Oslo Service library

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/oslo.service

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

Provides: python3-module-oslo-service = %EVR

# Very strange thing, idk where it came from :)
%add_python3_req_skip __original_module_threading

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-webob >= 1.7.1
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-eventlet >= 0.25.2
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-greenlet >= 0.4.15
BuildRequires: python3-module-oslo.utils >= 3.40.2
BuildRequires: python3-module-oslo.concurrency >= 3.25.0
BuildRequires: python3-module-oslo.config >= 5.1.0
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-routes >= 2.3.1
BuildRequires: python3-module-paste >= 2.0.2
BuildRequires: python3-module-yappi >= 1.0

%if_with check
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-doc8 >= 0.6.0
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-bandit >= 1.6.0
BuildRequires: /proc
BuildRequires: python3-module-pre-commit >= 2.6.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
%endif

%description
This project provides a framework for defining new long-running services
using the patterns established by other OpenStack applications. It also includes
utilities long-running applications might need for working with SSL or WSGI,
performing periodic operations, interacting with systemd, etc.

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
Provides: python3-module-oslo-service-doc = %EVR

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
install -pDm 644 man/osloservice.1 %buildroot%_man1dir/osloservice.1
%endif

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%python3_sitelibdir/oslo_service
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/oslo_service/tests

%files tests
%python3_sitelibdir/oslo_service/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/osloservice.1.xz
%endif

%changelog
* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 3.1.0-alt1
- Automatically updated to 3.1.0.

* Sat Oct 15 2022 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt2
- Spec refactoring.

* Tue Oct 11 2022 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt1
- Automatically updated to 3.0.0.

* Mon Oct 10 2022 Grigory Ustinov <grenka@altlinux.org> 2.8.0-alt1
- Automatically updated to 2.8.0.
- Unified (thx for felixz@).

* Thu Jun 16 2022 Grigory Ustinov <grenka@altlinux.org> 2.1.1-alt2
- Build without docs.

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 2.1.1-alt1
- Automatically updated to 2.1.1.
- Unify documentation building.
- Fix license.
- Removed watch file.

* Thu Jan 09 2020 Grigory Ustinov <grenka@altlinux.org> 1.41.1-alt1
- Automatically updated to 1.41.1.
- Added watch file.
- Renamed spec file.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 1.40.2-alt1
- Automatically updated to 1.40.2.
- Build without python2.
- Build without docs.

* Sun Aug 18 2019 Grigory Ustinov <grenka@altlinux.org> 1.40.0-alt1
- Automatically updated to 1.40.0

* Mon Apr 22 2019 Alexey Shabalin <shaba@altlinux.org> 1.31.8-alt1
- 1.31.8

* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 1.31.7-alt1
- 1.31.7

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.19.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jun 22 2017 Alexey Shabalin <shaba@altlinux.ru> 1.19.1-alt1
- 1.19.1

* Thu May 25 2017 Alexey Shabalin <shaba@altlinux.ru> 1.19.0-alt1
- 1.19.0

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 1.16.0-alt1
- 1.16.0

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 0.9.0-alt1
- Initial package.
