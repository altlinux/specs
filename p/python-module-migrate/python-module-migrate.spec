Name:		python-module-migrate
Version:	0.7.2
Release:	alt1
Summary:	Schema migration tools for SQLAlchemy

Group:		Development/Python
License:	MIT
URL:		http://code.google.com/p/sqlalchemy-migrate/

Source0:	%{name}-%{version}.tar.gz

# Patch to update to new scripttest API submitted upstream
Patch0:		python-module-migrate-scripttest-update.patch

# Patch to fix a unittest on python-2.7
Patch1:		python-module-migrate-py27.patch

# Patch to fix version number __init__ bug
Patch2:		python-module-migrate-vernum.patch

# Local patch to rename /usr/bin/migrate to sqlalchemy-migrate
Patch100:	python-module-migrate-sqlalchemy-migrate.patch

BuildArch:	noarch
BuildRequires:	python-devel
BuildRequires:	python-module-SQLAlchemy
BuildRequires:	python-module-distribute
BuildRequires:	python-module-nose
BuildRequires:	python-module-sphinx
BuildRequires:	python-module-decorator
BuildRequires:	python-module-tempita

# for testsuite
BuildRequires:	python-module-scripttest
BuildRequires:	python-module-pysqlite2

Requires:	python-module-SQLAlchemy
Requires:	python-module-distribute
Requires:	python-module-decorator
Requires:	python-module-tempita

%description
Schema migration tools for SQLAlchemy designed to support an agile
approach to database design and make it easier to keep development and
production databases in sync as schema changes are required. It allows
you to manage atabase change sets and database repository versioning.

%prep
%setup -q
%patch0 -p1 -b .test
%patch1 -p1 -b .py27
%patch2 -p2 -b .vernum
%patch100 -p1 -b .rename

# use real unittest in python 2.7 and up
sed -i "s/import unittest2/import unittest as unittest2/g" \
    migrate/tests/fixture/__init__.py \
    migrate/tests/fixture/base.py

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%check
# Need to set PATH for two reasons:
# 1) Path isn't being cleared by mock so we have /root/bin/ in the PATH
# 2) Need to be able to find the newly installed migrate binaries
PATH=/bin:/usr/bin:%{buildroot}%{_bindir}
export PATH

PYTHONPATH=`pwd`
export PYTHONPATH
echo 'sqlite:///__tmp__' > test_db.cfg
nosetests

%add_findreq_skiplist %{python_sitelibdir}/migrate/versioning/templates/*

%files
%defattr(-,root,root,-)
%doc README docs/
%{_bindir}/*
%{python_sitelibdir}/*

%changelog
* Thu Sep 13 2012 Pavel Shilovsky <piastry@altlinux.org> 0.7.2-alt1
- Initial release for Sisyphus (based on Fedora)
