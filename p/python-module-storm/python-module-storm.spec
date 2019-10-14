Name: python-module-storm
Version: 0.21
Release: alt2
Summary: An object-relational mapper (ORM) for Python

Group: Development/Python
License: LGPLv2+
Url: https://storm.canonical.com/
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar.gz
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-fixtures
BuildRequires: python-module-pysqlite2

%description
Storm is an object-relational mapper (ORM) for Python. It offers a clean and
lightweight API offers a short learning curve and long-term maintainability and
it is easy to written backends for it.

%package -n python-module-storm-mysql
Summary: MySQL backend for %name
Group: Development/Python
Requires: python-module-storm = %version
Requires: python-module-mysqlclient

%description -n python-module-storm-mysql
The %name-mysql package contains the MySQL database backend for
%name.

%package -n python-module-storm-postgresql
Summary: PostgreSQL backend for %name
Group: Development/Python
Requires: python-module-storm = %version
Requires: python-module-psycopg2

%description -n python-module-storm-postgresql
The %name-postgresql package contains the PostgreSQL database
backend for %name.

%package -n python-module-storm-django
Summary: Support for using %name as Django ORM
Group: Development/Python
Requires: python-module-django python-module-django-dbbackend-mysql python-module-django-dbbackend-psycopg2 python-module-django-dbbackend-sqlite3
Requires: python-module-storm-zope = %version

%description -n python-module-storm-django
The %name-django package contains an alternative ORM implementation
for Django.

%package -n python-module-storm-zope
Summary: Zope integration for %name
Group: Development/Python
Requires: python-module-storm = %version
Requires: python-module-zope.interface python-module-transaction

%description -n python-module-storm-zope
The %name-zope package provides Zope integration for %name.

%package -n python-module-storm-twisted
Summary: Twisted integration for %name
Group: Development/Python
Requires: python-module-storm = %version
Requires: python-module-twisted-conch python-module-twisted-core python-module-twisted-core-gui python-module-twisted-core-gui-gnome python-module-twisted-core-gui-tk python-module-twisted-core-gui-wx python-module-twisted-core-test python-module-twisted-logger python-module-twisted-names python-module-twisted-pair python-module-twisted-positioning python-module-twisted-web

%description -n python-module-storm-twisted
The %name-twisted package provides Twisted integration for %name.

%prep
%setup

rm -rf storm.egg-info

%build
%python_build

%install
%python_install

%files
%doc LICENSE NEWS README TODO
%doc storm/tests/tutorial.txt
%exclude %python_sitelibdir/storm/django
%exclude %python_sitelibdir/storm/zope
%exclude %python_sitelibdir/storm/cextensions.c
%exclude %python_sitelibdir/storm/databases
%exclude %python_sitelibdir/storm/twisted
%python_sitelibdir/storm*

%files -n python-module-storm-django
%python_sitelibdir/storm/django

%files -n python-module-storm-zope
%python_sitelibdir/storm/zope

%files -n python-module-storm-mysql
%python_sitelibdir/storm/databases/

%files -n python-module-storm-postgresql
%python_sitelibdir/storm/databases/postgres.*

%files -n python-module-storm-twisted
%python_sitelibdir/storm/twisted

%changelog
* Mon Sep 23 2019 Artyom Bystrov <arbars@altlinux.org> 0.21-alt2
- initial build for ALT Sisyphus


