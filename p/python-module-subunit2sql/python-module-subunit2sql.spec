%define oname subunit2sql
%define descr \
subunit2SQL is a tool for storing test results data in a SQL database. Like \
it's name implies it was originally designed around converting `subunit`_ \
streams to data in a SQL database and the packaged utilities assume a subunit \
stream as the input format. However, the data model used for the DB does not \
preclude using any test result format. Additionally the analysis tooling built \
on top of a database is data format agnostic. However if you choose to use a \
different result format as an input for the database additional tooling using \
the DB api would need to be created to parse a different test result output \
format. It's also worth pointing out that subunit has several language library \
bindings available. So as a user you could create a small filter to convert a \
different format to subunit. Creating a filter should be fairly easy and then \
you don't have to worry about writing a tool like :ref:`subunit2sql` to use a \
different format.
# TODO: make dep on python-module-stestr and enable check
%def_disable check

Name: python-module-%oname
Version: 1.10.0
Release: alt1

Summary: Tool for storing test results data in a SQL database

License: ASL 2.0
Group: Development/Python
Url: http://pypi.python.org/pypi/subunit2sql

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python
BuildRequires: python-module-pbr
BuildRequires: python-module-psycopg2
BuildRequires: python-module-pymysql
BuildRequires: python-module-reno
BuildRequires: python-module-testscenarios
BuildRequires: python-module-testresources
BuildRequires: python-module-openstackdocstheme
BuildRequires: python-module-oslo.concurrency >= 3.5.0

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr
BuildRequires: python3-module-psycopg2
BuildRequires: python3-module-pymysql
BuildRequires: python3-module-reno
BuildRequires: python3-module-testscenarios
BuildRequires: python3-module-testresources
BuildRequires: python3-module-openstackdocstheme
BuildRequires: python3-module-oslo.concurrency >= 3.5.0

%description
%descr

%package -n python3-module-%oname
Summary: Tool for storing test results data in a SQL database
Group: Development/Python3

%description -n python3-module-%oname
%descr

%package -n python3-module-%oname-tests
Summary: Tests for python-subunit (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package tests
Summary: Tests for python-subunit
Group: Development/Python
Requires: %name = %version-%release
Provides: python-module-python-%oname-tests = %EVR
Obsoletes: python-module-python-%oname-tests < %EVR

%description tests
This package contains tests for %oname.

%prep
%setup
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install
pushd %buildroot%_bindir
for i in $(ls); do
    mv $i $i.py2
done
popd
pushd ../python3
%python3_install
popd

%check
python setup.py test

pushd ../python3
python3 setup.py test
popd

%files
%_bindir/*.py2
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%oname
%_bindir/*
%exclude %_bindir/*.py2
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%changelog
* Tue Dec 11 2018 Grigory Ustinov <grenka@altlinux.org> 1.10.0-alt1
- Initial build for Sisyphus.
