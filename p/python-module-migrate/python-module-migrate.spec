%def_with python3

Name:		python-module-migrate
Version:	0.8.2
Release:	alt1.1
Summary:	Schema migration tools for SQLAlchemy

Group:		Development/Python
License:	MIT
URL:		http://code.google.com/p/sqlalchemy-migrate/

Source0:	%{name}-%{version}.tar.gz

# Patch to update to new scripttest API submitted upstream
Patch0:		python-module-migrate-scripttest-update.patch

# Patch to fix a unittest on python-2.7
Patch1:		python-module-migrate-py27.patch

# For Python 3
Patch2: migrate-0.8.2-alt-python3.patch

BuildArch:	noarch
BuildRequires:	python-devel
BuildRequires:	python-module-SQLAlchemy
BuildRequires:	python-module-setuptools
BuildRequires:	python-module-nose
BuildRequires:	python-module-sphinx
BuildRequires:	python-module-decorator
BuildRequires:	python-module-tempita
BuildRequires:	python-module-pbr
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires:	python3-devel
BuildRequires:	python3-module-SQLAlchemy
BuildRequires:	python3-module-setuptools
BuildRequires:	python3-module-nose
BuildRequires:	python3-module-sphinx
BuildRequires:	python3-module-decorator
BuildRequires:	python3-module-tempita
BuildRequires:	python3-module-pbr
BuildPreReq: python-tools-2to3
%endif

# for testsuite
BuildRequires:	python-module-scripttest
BuildRequires:	python-module-pysqlite2
BuildRequires:	python-module-testtools

Requires:	python-module-SQLAlchemy
Requires:	python-module-setuptools
Requires:	python-module-decorator
Requires:	python-module-tempita
Requires:	python-module-pbr

%description
Schema migration tools for SQLAlchemy designed to support an agile
approach to database design and make it easier to keep development and
production databases in sync as schema changes are required. It allows
you to manage atabase change sets and database repository versioning.

%package -n python3-module-migrate
Summary:	Schema migration tools for SQLAlchemy
Group:		Development/Python3
Requires:	python3-module-SQLAlchemy
Requires:	python3-module-setuptools
Requires:	python3-module-decorator
Requires:	python3-module-tempita
Requires:	python3-module-pbr

%description -n python3-module-migrate
Schema migration tools for SQLAlchemy designed to support an agile
approach to database design and make it easier to keep development and
production databases in sync as schema changes are required. It allows
you to manage atabase change sets and database repository versioning.

%prep
%setup
%patch0 -p1 -b .test
%patch1 -p1 -b .py27
%patch2 -p2

# use real unittest in python 2.7 and up
sed -i "s/import unittest2/import unittest as unittest2/g" \
    migrate/tests/fixture/__init__.py \
    migrate/tests/fixture/base.py

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
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
echo 'sqlite:///__tmp__' > test_db.cfg
PATH=/usr/bin/:%{buildroot}%{_bindir} PYTHONPATH=`pwd` nosetests

%add_findreq_skiplist %python_sitelibdir/migrate/versioning/templates/*
%add_findreq_skiplist %python3_sitelibdir/migrate/versioning/templates/*

%files
%defattr(-,root,root,-)
%doc README.rst doc/
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-migrate
%doc README.rst doc/
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Tue Aug 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.1
- Added module for Python 3

* Mon Dec 16 2013 Pavel Shilovsky <piastry@altlinux.org> 0.8.2-alt1
- New version 0.8.2
- Cleanup spec

* Thu Sep 13 2012 Pavel Shilovsky <piastry@altlinux.org> 0.7.2-alt1
- Initial release for Sisyphus (based on Fedora)
