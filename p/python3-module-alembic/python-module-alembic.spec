%define _unpackaged_files_terminate_build 1
%define oname alembic

%def_without test

Name: python3-module-alembic
Version: 1.10.2
Release: alt1

Summary: Database migration tool for SQLAlchemy

License: MIT
Group: Development/Python3
Url: https://alembic.sqlalchemy.org
VCS: https://github.com/sqlalchemy/alembic

Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildArch: noarch

Conflicts: python-module-alembic
Provides: python-module-alembic = %EVR

BuildRequires: help2man

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-devel python3-module-mako
BuildRequires: python3-module-SQLAlchemy
BuildRequires: python3-module-dateutil
%if_with test
BuildRequires: python3-module-pytest
BuildRequires: python3-module-nose
BuildRequires: python3-module-greenlet
BuildRequires: python3-module-sqlalchemy-tests
%endif

%description
Alembic is a new database migrations tool, written by the author of
SQLAlchemy <http://www.sqlalchemy.org>.  A migrations tool offers the
following functionality:

* Can emit ALTER statements to a database in order to change the structure
of tables and other constructs.
* Provides a system whereby "migration scripts" may be constructed; each script
indicates a particular series of steps that can "upgrade" a target database to
a new version, and optionally a series of steps that can "downgrade"
similarly, doing the same steps in reverse.
* Allows the scripts to execute in some sequential manner.

Documentation and status of Alembic is at http://readthedocs.org/docs/alembic/

%prep
%setup
%patch0 -p1

%build
%pyproject_build

%install
%pyproject_install
rm -rfv %buildroot%python3_sitelibdir/alembic/testing/

%if_with test
%check
%tox_create_default_config
%tox_check_pyproject -- -vra
%endif

%files
%doc README.rst LICENSE CHANGES docs
%_bindir/%oname
%python3_sitelibdir/*

%changelog
* Tue Mar 21 2023 Danil Shein <dshein@altlinux.org> 1.10.2-alt1
- new version 1.10.2
  + migrate to pyproject_installer

* Sat Mar 05 2022 Danil Shein <dshein@altlinux.org> 1.7.6-alt1
- new version 1.7.6

* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 1.6.5-alt1
- new version 1.6.5 (with rpmrb script)

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1.5.8-alt1
- new version 1.5.8 (with rpmrb script)

* Sun Apr 25 2021 Vitaly Lipatov <lav@altlinux.ru> 1.4.3-alt1
- new version 1.4.3 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.4.2-alt1
- build python3 separately, don't pack tests
- new version (1.4.2) with rpmgs script

* Thu Feb 06 2020 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- new version 1.4.0 (with rpmrb script)
- disable python2 module

* Fri Jan 25 2019 Stanislav Levin <slev@altlinux.org> 1.0.5-alt2
- Dropped BR on python argparse.

* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 1.0.5-alt1
- 1.0.5

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.10-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 30 2017 Alexey Shabalin <shaba@altlinux.ru> 0.8.10-alt1
- 0.8.10
- add test packages
- add alembic.migration alembic.environment to provides
- add %%check

* Mon Nov 14 2016 Lenar Shakirov <snejok@altlinux.ru> 0.8.8-alt1
- new version 0.8.8

* Fri Apr 22 2016 Vitaly Lipatov <lav@altlinux.ru> 0.8.6-alt1
- new version 0.8.6 (with rpmrb script)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.3-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.3-alt1.1
- NMU: Use buildreq for BR.

* Sun Jan 03 2016 Vitaly Lipatov <lav@altlinux.ru> 0.8.3-alt1
- new version 0.8.3 (with rpmrb script)

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1
- Version 0.8.1

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.7-alt1
- Version 0.7.7

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.4-alt1
- Version 0.7.4

* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.7-alt1
- Version 0.6.7
- Added module for Python 3

* Tue Sep 02 2014 Vitaly Lipatov <lav@altlinux.ru> 0.6.6-alt1
- new version 0.6.6 (with rpmrb script)

* Wed Apr 02 2014 Vitaly Lipatov <lav@altlinux.ru> 0.6.3-alt1
- new version 0.6.3 (with rpmrb script)

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt1
- new version 0.5.0 (with rpmrb script)

* Mon Apr 08 2013 Vitaly Lipatov <lav@altlinux.ru> 0.4.2-alt2
- initial build for ALT Linux Sisyphus

* Thu Mar 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_1
- update to new release by fcimport

* Thu Mar 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.4-alt2_11
- update to new release by fcimport

* Tue Jan 29 2013 Cronbuild Service <cronbuild@altlinux.org> 0.3.4-alt2_4
- rebuild to get rid of unmets

* Wed Jan 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.4-alt1_4
- initial fc import

