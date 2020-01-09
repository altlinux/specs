%define oname oslo.db

Name: python3-module-%oname
Version: 6.0.0
Release: alt1
Summary: OpenStack oslo.db library
Group: Development/Python3
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz
Source1: oslo.db.watch

BuildArch: noarch

Provides: python3-module-oslo-db = %EVR

Requires: python3-module-oslo.i18n >= 3.15.3
Requires: python3-module-migrate
Requires: python3-module-stevedore >= 1.20.0
Requires: python3-module-SQLAlchemy
Requires: python3-module-iso8601

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-alembic >= 0.9.6
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.context >= 2.9.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-migrate
BuildRequires: python3-module-migrate-tests
BuildRequires: python3-module-eventlet
BuildRequires: python3-module-oslotest
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-six >= 1.10.0

BuildRequires: python3-module-testresources >= 2.0.0
BuildRequires: python3-module-testscenarios >= 0.4

%description
The OpenStack Oslo database handling library. Provides database connectivity
to the different backends and helper utils.

%package doc
Summary: Documentation for the Oslo database handling library
Group: Development/Documentation
Provides: python-module-oslo-db-doc = %EVR

%description doc
Documentation for the Oslo database handling library.

%package tests
Summary: Tests for the Oslo database handling library
Group: Development/Python3
Requires: %name = %EVR

%description tests
Tests for the Oslo database handling library.

%prep
%setup -n %oname-%version

%build
%python3_build

# generate html docs
#python setup.py build_sphinx
# remove the sphinx-build leftovers
#rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%python3_install

%files
%doc CONTRIBUTING.rst HACKING.rst LICENSE PKG-INFO README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*

%changelog
* Thu Jan 09 2020 Grigory Ustinov <grenka@altlinux.org> 6.0.0-alt1
- Automatically updated to 6.0.0.
- Added watch file.
- Renamed spec file.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 5.0.2-alt1
- Automatically updated to 5.0.2.
- Build without python2.

* Sun Aug 18 2019 Grigory Ustinov <grenka@altlinux.org> 5.0.1-alt1
- Automatically updated to 5.0.1

* Mon Apr 22 2019 Alexey Shabalin <shaba@altlinux.org> 4.40.1-alt1
- 4.40.1

* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 4.40.0-alt1
- 4.40.0

* Thu May 24 2018 Andrey Bychkov <mrdrew@altlinux.org> 4.17.1-alt2
- rebuild with python3.6

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.17.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jul 18 2017 Alexey Shabalin <shaba@altlinux.ru> 4.17.1-alt1
- 4.17.1

* Thu May 25 2017 Alexey Shabalin <shaba@altlinux.ru> 4.17.0-alt1
- 4.17.0

* Wed Feb 01 2017 Alexey Shabalin <shaba@altlinux.ru> 4.13.5-alt1
- 4.13.5

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 4.13.3-alt1
- 4.13.3

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 4.7.0-alt1
- 4.7.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.6.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.6.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Mon Aug 24 2015 Alexey Shabalin <shaba@altlinux.ru> 1.7.2-alt1
- 1.7.2

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 1.7.1-alt1
- 1.7.1

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Mon Feb 16 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.3-alt1
- Initial release
