%define oname migrate

Name: python3-module-%oname
Version: 0.13.0
Release: alt1

Summary: Schema migration tools for SQLAlchemy

License: MIT
Group: Development/Python3
Url: https://github.com/openstack/sqlalchemy-migrate

Source: %oname-%version.tar

# Local patch to rename /usr/bin/migrate to sqlalchemy-migrate
Patch1: migrate-sqlalchemy-migrate.patch
Patch2: fix-regex.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr

%add_python3_req_skip ibm_db_sa
Provides: python3-module-sqlalchemy-migrate = %EVR

BuildArch: noarch

%description
Schema migration tools for SQLAlchemy designed to support an agile
approach to database design and make it easier to keep development and
production databases in sync as schema changes are required. It allows
you to manage database change sets and database repository versioning.

%package tests
Summary: Tests for Schema migration tools for SQLAlchemy
Group: Development/Python3
Requires: %name = %version-%release

%description tests
Tests for Schema migration tools for SQLAlchemy.

%prep
%setup -n %oname-%version

# suddenly 32bit arches cant process it
sed -i '/pytz/d' test-requirements.txt

%patch1 -p2
%patch2 -p1

%build
export PBR_VERSION=%version
%python3_build

%install
export PBR_VERSION=%version
%python3_install

%check
echo 'sqlite:///__tmp__' > test_db.cfg

%files
%doc README.rst AUTHORS ChangeLog COPYING doc/
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/migrate/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Sat Oct 22 2022 Grigory Ustinov <grenka@altlinux.org> 0.13.0-alt1
- Build new version for oslo.db.

* Fri Apr 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.11.0-alt3
- Build for python2 disabled.

* Thu Jan 31 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.11.0-alt2
- Fix bad regular expression in migrate/versioning/script/sql.py

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.11.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Jun 04 2017 Lenar Shakirov <snejok@altlinux.ru> 0.11.0-alt1
- 0.11.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.10.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Oct 27 2015 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt1
- 0.10.0

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 0.9.5-alt1
- 0.9.5

* Mon Feb 16 2015 Alexey Shabalin <shaba@altlinux.ru> 0.9.4-alt1
- 0.9.4

* Tue Aug 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.1
- Added module for Python 3

* Mon Dec 16 2013 Pavel Shilovsky <piastry@altlinux.org> 0.8.2-alt1
- New version 0.8.2
- Cleanup spec

* Thu Sep 13 2012 Pavel Shilovsky <piastry@altlinux.org> 0.7.2-alt1
- Initial release for Sisyphus (based on Fedora)
