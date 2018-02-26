%define version 1.0
%define release alt2.svn11616.1
%define origname Django
%setup_python_module django1.0
%add_python_req_skip cx_Oracle

Summary: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
Name: %packagename
Version: %version
Release: %release.1
Source0: %origname-%version.tar.gz
License: BSD
Group: Development/Python
BuildArch: noarch
URL: http://www.djangoproject.com/
Packager: Denis Klimov <zver@altlinux.org>
Provides: Django = %version-%release 
Conflicts: python-module-django python-module-django1.1

BuildPreReq: %py_dependencies setuptools

# Automatically added by buildreq on Tue Jul 29 2008 (-ba)
BuildRequires: python-module-setuptools python-modules-email python-modules-encodings python-modules-sqlite3 python-modules-xml
BuildRequires: python-modules-ctypes

%description
%summary

%package mod_python
Summary: mod_python support for Django.
Group: Development/Python
Requires: %name = %version-%release 
Requires: apache2-mod_python

%description mod_python
%summary

%package dbbackend-mysql
Summary: MySQLSQL support for Django.
Group: Development/Python
Requires: %name = %version-%release 
%py_requires MySQLdb

%description dbbackend-mysql
%summary

%package dbbackend-psycopg
Summary: PostgreSQL support for Django. (via psycopg)
Group: Development/Python
Requires: %name = %version-%release 
%py_requires psycopg

%description dbbackend-psycopg
%summary

%package dbbackend-psycopg2
Summary: PostgreSQL support for Django. (via psycopg2)
Group: Development/Python
Requires: %name = %version-%release 
%py_requires psycopg2

%description dbbackend-psycopg2
%summary

%package dbbackend-sqlite3
Summary: SQLite3 support for Django.
Group: Development/Python
Requires: %name = %version-%release 
%py_requires sqlite3

%description dbbackend-sqlite3
%summary

%package doc
Summary: Django documentation
Group: Development/Python

%description doc
%summary

%package examples
Summary: Django examples
Group: Development/Python

%description examples
%summary

%prep
%setup -n %origname-%version

%build
%python_build

%install
mkdir -p %buildroot/%_sysconfdir/bash_completion.d

%python_install --record=INSTALLED_FILES
sed -i -e '/\/test/d' INSTALLED_FILES

install -m 0755 extras/django_bash_completion %buildroot/%_sysconfdir/bash_completion.d/django.sh

# Run tests
#export PYTHONPATH="$PYTHONPATH:%buildroot/%python_sitelibdir/"
#cat >tests/settings.py << EOF
#DATABASE_ENGINE = 'sqlite3'
#DATABASE_NAME = 'demodb'
#ROOT_URLCONF=None 
#EOF
#tests/runtests.py --settings=settings --noinput -v 1
# End tests

%define modulename django

%files -f INSTALLED_FILES
%exclude %python_sitelibdir/%modulename/core/handlers/modpython.py*
%exclude %python_sitelibdir/%modulename/contrib/auth/handlers/modpython.py*

%exclude %python_sitelibdir/%modulename/db/backends/mysql/
%exclude %python_sitelibdir/%modulename/db/backends/postgresql/
%exclude %python_sitelibdir/%modulename/db/backends/postgresql_psycopg2/
%exclude %python_sitelibdir/%modulename/db/backends/sqlite3/

%config %_sysconfdir/bash_completion.d/django.sh

%files doc
%doc docs

%files examples
%doc examples

%files mod_python
%python_sitelibdir/%modulename/core/handlers/modpython.py*
%python_sitelibdir/%modulename/contrib/auth/handlers/modpython.py*

%files dbbackend-mysql
%python_sitelibdir/%modulename/db/backends/mysql/

%files dbbackend-psycopg
%python_sitelibdir/%modulename/db/backends/postgresql/

%files dbbackend-psycopg2
%python_sitelibdir/%modulename/db/backends/postgresql_psycopg2/

%files dbbackend-sqlite3
%python_sitelibdir/%modulename/db/backends/sqlite3/

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2.svn11616.1.1
- Rebuild with Python-2.7

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2.svn11616.1
- Rebuilt with python 2.6

* Sat Nov 21 2009 Denis Klimov <zver@altlinux.org> 1.0-alt2.svn11616
- add conflicts

* Sat Nov 21 2009 Denis Klimov <zver@altlinux.org> 1.0-alt1.svn11616
- Initial build 1.0 django branch for ALT Linux

