%define oname simple-db-migrate

%def_without python3
%def_disable check

Name: python-module-%oname
Version: 2.2.0
Release: alt2.git20150114.1
Summary: Database versioning and migration tool inspired on Rails Migrations
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/simple-db-migrate/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/guilhermechapiewski/simple-db-migrate.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-nose python-module-coverage
BuildPreReq: python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nose python3-module-coverage
BuildPreReq: python3-module-mock
BuildPreReq: python-tools-2to3
%endif

%py_provides simple_db_migrate

%description
simple-db-migrate is a database versioning and migration tool inspired
on Rails Migrations. This tool helps you easily refactor, manage and
track your database schema. The main difference is that Rails migrations
are intended to be used only on Ruby projects while simple-db-migrate
makes it possible to have migrations in any language (Java, Python,
Ruby, PHP, whatever). This is possible because simple-db-migrate uses
database's DDL (Data Definition Language) to do the database operations,
while Rails Migrations are written in a Ruby internal DSL.

%if_with python3
%package -n python3-module-%oname
Summary: Database versioning and migration tool inspired on Rails Migrations
Group: Development/Python3
%py3_provides simple_db_migrate

%description -n python3-module-%oname
simple-db-migrate is a database versioning and migration tool inspired
on Rails Migrations. This tool helps you easily refactor, manage and
track your database schema. The main difference is that Rails migrations
are intended to be used only on Ruby projects while simple-db-migrate
makes it possible to have migrations in any language (Java, Python,
Ruby, PHP, whatever). This is possible because simple-db-migrate uses
database's DDL (Data Definition Language) to do the database operations,
while Rails Migrations are written in a Ruby internal DSL.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
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

%check
python setup.py test
%make test
%if_with python3
pushd ../python3
python3 setup.py test
sed -i 's|nosetests|nosetests3|' Makefile
%make test
popd
%endif

%files
%doc ChangeLog *.txt *.textile example
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/tests

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog *.txt *.textile example
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.2.0-alt2.git20150114.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt2.git20150114
- Fixed build

* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1.git20150114
- Initial build for Sisyphus

