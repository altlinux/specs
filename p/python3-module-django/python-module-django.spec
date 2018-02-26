%define version 1.5.0
%define release alt1.alpha
%define origname Django
%define oname django
%add_python3_req_skip cx_Oracle
%add_findreq_skiplist %python3_sitelibdir/%oname/contrib/gis/db/backends/*/*

Summary: A high-level Python 3 Web framework that encourages rapid development and clean, pragmatic design.
Name: python3-module-%oname
Version: %version
Release: %release
Source0: %origname-%version.tar
License: BSD
Group: Development/Python3
BuildArch: noarch
URL: http://www.djangoproject.com/

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-distribute
BuildPreReq: python-tools-2to3

%add_python3_req_skip hotshot

%description
%summary

%package tests
Summary: Tests for Django (Python 3)
Group: Development/Python3
BuildArch: noarch
Requires: %name = %version-%release
%add_python3_req_skip new

%description tests
%summary

This package contains tests for Django.

%package mod_python
Summary: mod_python support for Django (Python 3)
Group: Development/Python3
Requires: %name = %version-%release 
Requires: apache2-mod_python

%description mod_python
%summary

%package dbbackend-mysql
Summary: MySQLSQL support for Django (Python 3)
Group: Development/Python3
Requires: %name = %version-%release 
%py3_requires MySQLdb

%description dbbackend-mysql
%summary

%package dbbackend-psycopg
Summary: PostgreSQL support for Django. (via psycopg) (Python 3)
Group: Development/Python3
Requires: %name = %version-%release 
%py3_requires psycopg

%description dbbackend-psycopg
%summary

%package dbbackend-psycopg2
Summary: PostgreSQL support for Django. (via psycopg2) (Python 3)
Group: Development/Python3
Requires: %name = %version-%release 
%py3_requires psycopg2

%description dbbackend-psycopg2
%summary

%package dbbackend-sqlite3
Summary: SQLite3 support for Django (Python 3)
Group: Development/Python3
Requires: %name = %version-%release 
%py3_requires sqlite3

%description dbbackend-sqlite3
%summary

%package doc
Summary: Django documentation
Group: Development/Python

%description doc
%summary

%prep
%setup -n %origname-%version

for i in $(find ./ -name '*.py'); do
	sed -i 's|%_bindir/env python|%_bindir/env python3|' $i
	sed -i 's|.*from future_builtins import zip.*||' $i
	2to3 -w -n $i
done

%build
%python3_build

%install
export LC_ALL=en_US.UTF-8
%python3_install
mv %buildroot%_bindir/django-admin.py %buildroot%_bindir/django-admin.py3

%files
%_bindir/django-admin.py3
%python3_sitelibdir/*
#exclude %python3_sitelibdir/%oname/core/handlers/modpython.py*
#exclude %python3_sitelibdir/%oname/contrib/auth/handlers/modpython.py*

%exclude %python3_sitelibdir/%oname/db/backends/mysql/
#exclude %python3_sitelibdir/%oname/db/backends/postgresql/
%exclude %python3_sitelibdir/%oname/db/backends/postgresql_psycopg2/
%exclude %python3_sitelibdir/%oname/db/backends/sqlite3/

%exclude %python3_sitelibdir/%oname/test
%exclude %python3_sitelibdir/%oname/*/*/test*.py*
%exclude %python3_sitelibdir/%oname/*/*/tests
%exclude %python3_sitelibdir/%oname/*/*/*/tests

%files tests
%python3_sitelibdir/%oname/test
%python3_sitelibdir/%oname/*/*/test*.py*
%python3_sitelibdir/%oname/*/*/tests
%python3_sitelibdir/%oname/*/*/*/tests

%files doc
%doc docs

#files mod_python
#python3_sitelibdir/%oname/core/handlers/modpython.py*
#python3_sitelibdir/%oname/contrib/auth/handlers/modpython.py*

%files dbbackend-mysql
%python3_sitelibdir/%oname/db/backends/mysql/

#files dbbackend-psycopg
#python3_sitelibdir/%oname/db/backends/postgresql/

%files dbbackend-psycopg2
%python3_sitelibdir/%oname/db/backends/postgresql_psycopg2/

%files dbbackend-sqlite3
%python3_sitelibdir/%oname/db/backends/sqlite3/

%changelog
* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.alpha
- Version 1.5.0-alpha

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
