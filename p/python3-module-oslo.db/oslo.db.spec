%define oname oslo.db
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 12.2.0
Release: alt1

Summary: OpenStack Oslo Database library

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/oslo.db

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

Provides: python3-module-oslo-db = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-alembic >= 0.9.6
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.context >= 2.19.2
BuildRequires: python3-module-sqlalchemy
BuildRequires: python3-module-migrate
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-testresources >= 2.0.0
BuildRequires: python3-module-testscenarios >= 0.4

%if_with check
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-eventlet >= 0.18.2
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-bandit >= 1.6.0
BuildRequires: python3-module-pifpaf >= 0.10.0
BuildRequires: python3-module-psycopg2 >= 2.8.0
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-pymysql
BuildRequires: python3-module-pre-commit >= 2.6.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-sphinxcontrib-apidoc
%endif

%description
The OpenStack Oslo database handling library. Provides database connectivity
to the different backends and helper utils.

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
Provides: python3-module-oslo-db-doc = %EVR

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
install -pDm 644 man/oslodb.1 %buildroot%_man1dir/oslodb.1
%endif

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%python3_sitelibdir/oslo_db
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/oslo_db/tests

%files tests
%python3_sitelibdir/oslo_db/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/oslodb.1.xz
%endif

%changelog
* Sat Oct 22 2022 Grigory Ustinov <grenka@altlinux.org> 12.2.0-alt1
- Automatically updated to 12.2.0.

* Tue Oct 18 2022 Grigory Ustinov <grenka@altlinux.org> 12.1.0-alt1
- Automatically updated to 12.1.0.

* Mon May 16 2022 Grigory Ustinov <grenka@altlinux.org> 11.3.0-alt1
- Automatically updated to 11.3.0.

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
