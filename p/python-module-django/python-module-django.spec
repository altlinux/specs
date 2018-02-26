%define version 1.4
%define release alt1
%define origname Django
%setup_python_module django
%add_python_req_skip cx_Oracle
%add_findreq_skiplist %python_sitelibdir/%modulename/contrib/gis/db/backends/*/*

Summary: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
Name: %packagename
Version: %version
Release: %release
Source0: %origname-%version.tar.gz
License: BSD
Group: Development/Python
BuildArch: noarch
URL: http://www.djangoproject.com/
Provides: Django = %version-%release 
Conflicts: python-module-django1.0 python-module-django1.1
Conflicts: python-module-django1.2

BuildPreReq: %py_dependencies setuptools

# Automatically added by buildreq on Tue Jul 29 2008 (-ba)
BuildRequires: python-module-setuptools python-modules-email
BuildRequires: python-modules-encodings python-modules-sqlite3
BuildRequires: python-modules-xml
BuildRequires: python-modules-ctypes

%description
%summary

%package tests
Summary: Tests for Django
Group: Development/Python
BuildArch: noarch
Requires: %name = %version-%release

%description tests
%summary

This package contains tests for Django.

%package mod_python
Summary: mod_python support for Django.
Group: Development/Python
Requires: %name = %version-%release 
Requires: apache2-mod_python
Conflicts: python-module-django1.0-mod_python

%description mod_python
%summary

%package dbbackend-mysql
Summary: MySQLSQL support for Django.
Group: Development/Python
Requires: %name = %version-%release 
%py_requires MySQLdb
Conflicts: python-module-django1.0-dbbackend-mysql
Conflicts: python-module-django1.1-dbbackend-mysql

%description dbbackend-mysql
%summary

%package dbbackend-psycopg
Summary: PostgreSQL support for Django. (via psycopg)
Group: Development/Python
Requires: %name = %version-%release 
%py_requires psycopg
Conflicts: python-module-django1.0-dbbackend-psycopg
Conflicts: python-module-django1.1-dbbackend-psycopg

%description dbbackend-psycopg
%summary

%package dbbackend-psycopg2
Summary: PostgreSQL support for Django. (via psycopg2)
Group: Development/Python
Requires: %name = %version-%release 
%py_requires psycopg2
Conflicts: python-module-django1.0-dbbackend-psycopg2
Conflicts: python-module-django1.1-dbbackend-psycopg2

%description dbbackend-psycopg2
%summary

%package dbbackend-sqlite3
Summary: SQLite3 support for Django.
Group: Development/Python
Requires: %name = %version-%release 
%py_requires sqlite3
Conflicts: python-module-django1.0-dbbackend-sqlite3
Conflicts: python-module-django1.1-dbbackend-sqlite3

%description dbbackend-sqlite3
%summary

%package doc
Summary: Django documentation
Group: Development/Python

%description doc
%summary

%prep
%setup -n %origname-%version

%build
%python_build

%install
mkdir -p %buildroot/%_sysconfdir/bash_completion.d

%python_install --record=INSTALLED_FILES
#sed -i -e '/\/test/d' INSTALLED_FILES

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

%files -f INSTALLED_FILES
%exclude %python_sitelibdir/%modulename/core/handlers/modpython.py*
%exclude %python_sitelibdir/%modulename/contrib/auth/handlers/modpython.py*

%exclude %python_sitelibdir/%modulename/db/backends/mysql/
#exclude %python_sitelibdir/%modulename/db/backends/postgresql/
%exclude %python_sitelibdir/%modulename/db/backends/postgresql_psycopg2/
%exclude %python_sitelibdir/%modulename/db/backends/sqlite3/

%exclude %python_sitelibdir/%modulename/test
%exclude %python_sitelibdir/%modulename/*/*/test*.py*
%exclude %python_sitelibdir/%modulename/*/*/tests
%exclude %python_sitelibdir/%modulename/*/*/*/tests

%config %_sysconfdir/bash_completion.d/django.sh

%files tests
%python_sitelibdir/%modulename/test
%python_sitelibdir/%modulename/*/*/test*.py*
%python_sitelibdir/%modulename/*/*/tests
%python_sitelibdir/%modulename/*/*/*/tests

%files doc
%doc docs

%files mod_python
%python_sitelibdir/%modulename/core/handlers/modpython.py*
%python_sitelibdir/%modulename/contrib/auth/handlers/modpython.py*

%files dbbackend-mysql
%python_sitelibdir/%modulename/db/backends/mysql/

#files dbbackend-psycopg
#python_sitelibdir/%modulename/db/backends/postgresql/

%files dbbackend-psycopg2
%python_sitelibdir/%modulename/db/backends/postgresql_psycopg2/

%files dbbackend-sqlite3
%python_sitelibdir/%modulename/db/backends/sqlite3/

%changelog
* Thu May 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Version 1.4 (ALT #27288)

* Thu Dec 15 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 1.3.1-alt1
- Version 1.3.1. Security fixes:
  https://www.djangoproject.com/weblog/2011/sep/09/security-releases-issued/

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3-alt1.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1
- Version 1.3

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.5-alt1
- Version 1.2.5

* Sat Nov 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1
- Version 1.2.3

* Thu Aug 26 2010 Andrey Rahmatullin <wrar@altlinux.org> 1.2.1-alt2
- do not search for dependencies in django/contrib/gis/db/backends (closes: #23924)

* Mon Aug 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1
- Version 1.2.1
- Added tests (ALT #22479)

* Sun Mar 21 2010 Denis Klimov <zver@altlinux.org> 1.2-alt3.svn12825
- fix inherit with alt gear

* Sun Mar 21 2010 Denis Klimov <zver@altlinux.org> 1.2-alt2.svn12825
- new version
- remove examples subpackage. It was removed from Django.

* Tue Feb 09 2010 Denis Klimov <zver@altlinux.org> 1.2-alt2.svn12398
- new version

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2.svn11756.1
- Rebuilt with python 2.6

* Sat Nov 21 2009 Denis Klimov <zver@altlinux.org> 1.2-alt2.svn11756
- add conflicts

* Sat Nov 21 2009 Denis Klimov <zver@altlinux.org> 1.2-alt1.svn11756
- new version
- use python macros
- add doc and examples subpackages
- remove test files

* Sat Sep 19 2009 Denis Klimov <zver@altlinux.org> 1.1-alt2.svn11581
- change depend for sqlite python module (Closes: #18957)

* Fri Sep 18 2009 Denis Klimov <zver@altlinux.org> 1.1-alt1.svn11581
- new version (Closes: #21617)

* Thu Jun 04 2009 Denis Klimov <zver@altlinux.org> 1.1-alt1.svn10914
- new version (Closes: #20300)

* Thu May 07 2009 Denis Klimov <zver@altlinux.org> 1.1-alt1.svn10702
- new version from trunk
- remove needless -q option from setup macros
- remove commented lines
- turn off test section

* Fri Mar 20 2009 Denis Klimov <zver@altlinux.org> 1.0-alt5.svn10105
- new version from trunk

* Sun Feb 15 2009 Denis Klimov <zver@altlinux.org> 1.0-alt5.svn9832
- new version from trunk

* Thu Sep 04 2008 Andrew Kornilov <hiddenman@altlinux.ru> 1.0-alt5
- 1.0 release

* Mon Sep 01 2008 Andrew Kornilov <hiddenman@altlinux.ru> 1.0-alt4.beta_2
- 1.0 beta 2

* Sun Aug 17 2008 Andrew Kornilov <hiddenman@altlinux.ru> 1.0-alt3.beta_1
- 1.0 beta 1

* Thu Aug 14 2008 Andrew Kornilov <hiddenman@altlinux.ru> 1.0-alt2.alpha_2
- 1.0 alpha 2
- BuildReq updates

* Fri Jul 25 2008 Andrew Kornilov <hiddenman@altlinux.ru> 1.0-alt1.alpha
- First 1.0 alpha
- Spec updates
- Removed ChangeLog.bz2
- Use Django unit tests

* Tue May 20 2008 Andrew Kornilov <hiddenman@altlinux.ru> 0.97-alt1.svn7540
- Latest SVN trunk sources (Closes: #15646)
- Security fixes (http://groups.google.com/group/django-developers/browse_thread/thread/903d7c2af239ec42)
- Spec updates (pack subdirs)

* Fri Apr 11 2008 Andrew Kornilov <hiddenman@altlinux.ru> 0.97-alt1.svn7412
- Latest SVN trunk sources
- Fixed packages description

* Thu Mar 20 2008 Andrew Kornilov <hiddenman@altlinux.ru> 0.97-alt1.svn7152
- SVN trunk

* Sat Feb 09 2008 Andrew Kornilov <hiddenman@altlinux.ru> 0.97-alt1.svn7103
- Latest svn trunk sources

* Mon Dec 10 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.97-alt0.2.svn6903
- Latest svn trunk sources

* Sat Dec 08 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.97-alt0.2.svn6898
- Latest svn trunk sources

* Sun Sep 24 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.97-alt0.1.svn6410
- Latest svn trunk sources
- Temporarily removed cx_Oracle requirement
- ChangeLog added to the docs
- Removed core/handler.py because it's deprecated

* Mon Jul 02 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.97-alt0.1.svn5583
- Near the 0.97 release

* Sat May 26 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.96-alt1
- New version
- Spec cleanups (package names)

* Thu Mar 08 2007 Ivan Fedorov <ns@altlinux.ru> 0.95.1-alt1
- Initial build for ALT Linux Sisyphus.
