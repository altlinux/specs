
%global modname alembic

%def_with python3

Name: python-module-alembic
Version: 0.8.10
Release: alt1.1

Summary: Database migration tool for SQLAlchemy

License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/alembic

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pypi.python.org/packages/source/a/%modname/%modname-%version.tar.gz

BuildArch: noarch

%py_provides alembic.migration alembic.environment

BuildRequires(pre): rpm-build-python

BuildRequires: help2man
BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-mako
BuildRequires: python-module-argparse
BuildRequires: python-module-SQLAlchemy >= 0.7.6
BuildRequires: python-module-editor >= 0.3

BuildRequires: python-module-nose
BuildRequires: python-module-mock
BuildRequires: python-module-SQLAlchemy-tests

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-mako python3-module-nose
BuildRequires: python3-module-SQLAlchemy python3-module-setuptools
BuildRequires: python3-module-argparse
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

%package tests
Summary: Tests for %modname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %modname.

%package -n python3-module-%modname
Summary: Database migration tool for SQLAlchemy
Group: Development/Python3
%py3_provides alembic.migration alembic.environment

%description -n python3-module-%modname
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

%package -n python3-module-%modname-tests
Summary: Tests for %modname
Group: Development/Python3
Requires: python3-module-%modname = %EVR

%description -n python3-module-%modname-tests
This package contains tests for %modname.

%prep
%setup -n %modname-%version

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

mkdir bin
echo 'python -c "import alembic.config; alembic.config.main()" $*' > bin/alembic
chmod 0755 bin/alembic
help2man --version-string %{version} --no-info -s 1 bin/alembic > alembic.1

%if_with python3
pushd ../python3
%python3_build
mkdir bin
echo 'python3 -c "import alembic.config; alembic.config.main()" $*' > bin/alembic
chmod 0755 bin/alembic
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install
mkdir -p %buildroot%_man1dir/
install -m 0644 alembic.1 %buildroot%_man1dir/alembic.1

%check
python setup.py test

%files
%doc README.rst LICENSE CHANGES docs
%_bindir/%modname
%_man1dir/alembic.1*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/testing

%files tests
%python_sitelibdir/*/testing

%if_with python3
%files -n python3-module-%modname
%doc README.rst LICENSE CHANGES docs
%_bindir/%modname.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/testing

%files -n python3-module-%modname-tests
%python3_sitelibdir/*/testing
%endif

%changelog
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

