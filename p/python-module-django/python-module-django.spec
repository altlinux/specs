%define branch 1.8
%define version %branch.17
%define release alt1
%define origname Django
%define oname django
%define py3_name python3-module-%oname

%def_with python3
%def_with check

%setup_python_module django
%add_python_req_skip cx_Oracle
%add_findreq_skiplist %python_sitelibdir/%modulename/contrib/gis/db/backends/*/*
%if_with python3
%add_python3_req_skip cx_Oracle
%add_findreq_skiplist %python3_sitelibdir/%oname/contrib/gis/db/backends/*/*
%endif

Summary: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
Name: python-module-%oname
Version: %version
Release: %release
Source0: %origname-%version.tar
License: BSD
Group: Development/Python
BuildArch: noarch
URL: http://www.djangoproject.com/
Provides: Django = %EVR
Provides: %name%branch = %EVR
Obsoletes: python-module-django1.5 <= 1.5.0-alt3
Conflicts: python-module-django1.0 python-module-django1.1
Conflicts: python-module-django1.2

#BuildPreReq: %py_dependencies setuptools
#BuildPreReq: python-module-memcached python-module-mock

# Automatically added by buildreq on Fri Jan 29 2016 (-bi)
# optimized out: python-base python-devel python-module-funcsigs python-module-pbr python-module-setuptools python-module-six python-module-unittest2 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-unittest python-modules-xml python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-setuptools tzdata
BuildRequires: python-module-mock python-modules-sqlite3 python-modules-wsgiref python3-module-html5lib python3-module-pbr python3-module-unittest2 python3-modules-sqlite3 rpm-build-python3

#BuildRequires: python-modules-encodings python-modules-sqlite3
#BuildRequires: python-modules-xml
#BuildRequires: python-modules-ctypes

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-distribute
#BuildPreReq: python3-module-memcached python3-module-mock
#BuildPreReq: python-tools-2to3

%add_python3_req_skip hotshot StringIO
%endif

%if_with check
#BuildPreReq: python-modules-json
#BuildPreReq: python-modules-wsgiref
%if_with python3
#BuildPreReq: python3-modules-sqlite3
%endif
%endif

%description
%summary

%package tests
Summary: Tests for Django
Group: Development/Python
BuildArch: noarch
Requires: %name = %EVR
Provides: %name%branch = %EVR
Obsoletes: python-module-django1.5-tests <= 1.5.0-alt3
Conflicts: python-module-django1.0-tests
Conflicts: python-module-django1.1-tests
Conflicts: python-module-django1.2-tests

%description tests
%summary

This package contains tests for Django.

%package mod_python
Summary: mod_python support for Django.
Group: Development/Python
Requires: %name = %EVR
Requires: apache2-mod_python
Provides: %name%branch = %EVR
Obsoletes: python-module-django1.5-mod_python <= 1.5.0-alt3
Conflicts: python-module-django1.0-mod_python
Conflicts: python-module-django1.1-mod_python
Conflicts: python-module-django1.2-mod_python

%description mod_python
%summary

%package dbbackend-mysql
Summary: MySQLSQL support for Django.
Group: Development/Python
Requires: %name = %EVR
%py_requires MySQLdb
Provides: %name%branch = %EVR
Obsoletes: python-module-django1.5-dbbackend-mysql <= 1.5.0-alt3
Conflicts: python-module-django1.0-dbbackend-mysql
Conflicts: python-module-django1.1-dbbackend-mysql
Conflicts: python-module-django1.2-dbbackend-mysql

%description dbbackend-mysql
%summary

%package dbbackend-psycopg
Summary: PostgreSQL support for Django. (via psycopg)
Group: Development/Python
Requires: %name = %EVR
%py_requires psycopg
Provides: %name%branch = %EVR
Obsoletes: python-module-django1.5-dbbackend-psycopg <= 1.5.0-alt3
Conflicts: python-module-django1.0-dbbackend-psycopg
Conflicts: python-module-django1.1-dbbackend-psycopg
Conflicts: python-module-django1.2-dbbackend-psycopg

%description dbbackend-psycopg
%summary

%package dbbackend-psycopg2
Summary: PostgreSQL support for Django. (via psycopg2)
Group: Development/Python
Requires: %name = %EVR
%py_requires psycopg2
Provides: %name%branch = %EVR
Obsoletes: python-module-django1.5-dbbackend-psycopg2 <= 1.5.0-alt3
Conflicts: python-module-django1.0-dbbackend-psycopg2
Conflicts: python-module-django1.1-dbbackend-psycopg2
Conflicts: python-module-django1.2-dbbackend-psycopg2

%description dbbackend-psycopg2
%summary

%package dbbackend-sqlite3
Summary: SQLite3 support for Django.
Group: Development/Python
Requires: %name = %EVR
%py_requires sqlite3
Provides: %name%branch = %EVR
Obsoletes: python-module-django1.5-dbbackend-sqlite3 <= 1.5.0-alt3
Conflicts: python-module-django1.0-dbbackend-sqlite3
Conflicts: python-module-django1.1-dbbackend-sqlite3
Conflicts: python-module-django1.2-dbbackend-sqlite3

%description dbbackend-sqlite3
%summary

%if_with python3
%package -n %py3_name
Summary: A high-level Python 3 Web framework that encourages rapid development and clean, pragmatic design.
Group: Development/Python3
BuildArch: noarch
Provides: %py3_name%branch = %EVR
%py3_provides django.utils.six.moves
%py3_provides django.utils.six.moves.urllib.parse
%py3_provides django.utils.six.moves.urllib.request
Obsoletes: python3-module-django1.5 <= 1.5.0-alt3

%description -n %py3_name
%summary

%package -n %py3_name-tests
Summary: Tests for Django (Python 3)
Group: Development/Python3
BuildArch: noarch
Requires: %py3_name = %EVR
Provides: %py3_name%branch-tests = %EVR
Obsoletes: python3-module-django1.5-tests <= 1.5.0-alt3
%add_python3_req_skip new

%description -n %py3_name-tests
%summary

This package contains tests for Django.

%package -n %py3_name-mod_python
Summary: mod_python support for Django (Python 3)
Group: Development/Python3
Requires: %py3_name = %EVR
Requires: apache2-mod_python
Provides: %py3_name%branch-mod_python = %EVR
Obsoletes: python3-module-django1.5-mod_python <= 1.5.0-alt3

%description -n %py3_name-mod_python
%summary

%package -n %py3_name-dbbackend-mysql
Summary: MySQLSQL support for Django (Python 3)
Group: Development/Python3
Requires: %py3_name = %EVR
Provides: %py3_name%branch-dbbackend-mysql = %EVR
Obsoletes: python3-module-django1.5-dbbackend-mysql <= 1.5.0-alt3
%py3_requires MySQLdb

%description -n %py3_name-dbbackend-mysql
%summary

%package -n %py3_name-dbbackend-psycopg
Summary: PostgreSQL support for Django. (via psycopg) (Python 3)
Group: Development/Python3
Requires: %py3_name = %EVR
Provides: %py3_name%branch-dbbackend-psycopg = %EVR
Obsoletes: python3-module-django1.5-dbbackend-psycopg <= 1.5.0-alt3
%py3_requires psycopg

%description -n %py3_name-dbbackend-psycopg
%summary

%package -n %py3_name-dbbackend-psycopg2
Summary: PostgreSQL support for Django. (via psycopg2) (Python 3)
Group: Development/Python3
Requires: %py3_name = %EVR
Provides: %py3_name%branch-dbbackend-psycopg2 = %EVR
Obsoletes: python3-module-django1.5-dbbackend-psycopg2 <= 1.5.0-alt3
%py3_requires psycopg2

%description -n %py3_name-dbbackend-psycopg2
%summary

%package -n %py3_name-dbbackend-sqlite3
Summary: SQLite3 support for Django (Python 3)
Group: Development/Python3
Requires: %py3_name = %EVR
Provides: %py3_name%branch-dbbackend-sqlite3 = %EVR
Obsoletes: python3-module-django1.5-dbbackend-sqlite3 <= 1.5.0-alt3
%py3_requires sqlite3

%description -n %py3_name-dbbackend-sqlite3
%summary

%endif

%package doc
Summary: Django documentation
Group: Development/Python
Provides: %name%branch-doc = %EVR
Provides: %py3_name%branch-doc = %EVR
Provides: %py3_name%branch-doc = %EVR
Obsoletes: python-module-django1.5-doc <= 1.5.0-alt3
Obsoletes: python3-module-django-doc <= 1.5.0-alt1.alpha
Conflicts: python-module-django1.0-doc
Conflicts: python-module-django1.1-doc
Conflicts: python-module-django1.2-doc

%description doc
%summary

%prep
%setup -n %origname-%version
%if_with python3
rm -rf ../python3
cp -a . ../python3
pushd ../python3
find -type f -name '*.py' -exec sed -i 's|%_bindir/env python|%_bindir/python3|' -- '{}' +
find -type f -name '*.py' -exec sed -i 's|.*from future_builtins import zip.*||' -- '{}' +
popd
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
export LC_ALL=en_US.UTF-8

%if_with python3
pushd ../python3
%python3_install
mv %buildroot%_bindir/django-admin.py %buildroot%_bindir/django-admin.py3
for i in $(find %buildroot%python3_sitelibdir -name '*test*'); do
	echo $i |sed 's|%buildroot\(.*\)|%%exclude \1\*|' >>%oname.notests
	echo $i |sed 's|%buildroot\(.*\)|\1\*|' >>%oname.tests
done
popd
%endif

mkdir -p %buildroot/%_sysconfdir/bash_completion.d

%python_install
for i in $(find %buildroot%python_sitelibdir -name '*test*'); do
	echo $i |sed 's|%buildroot\(.*\)|%%exclude \1\*|' >>%oname.notests
	echo $i |sed 's|%buildroot\(.*\)|\1\*|' >>%oname.tests
done

install -m 0755 extras/django_bash_completion %buildroot/%_sysconfdir/bash_completion.d/django.sh

%if_with check
%check
# Run tests
pushd tests
LANG="en_US.UTF-8" PYTHONPATH=%buildroot/%python_sitelibdir ./runtests.py --settings=test_sqlite
popd
%if_with python3
pushd ../python3/tests
LANG="en_US.UTF-8" PYTHONPATH=%buildroot/%python_sitelibdir ./runtests.py --settings=test_sqlite
popd
%endif
# End tests
%endif


%files -f %oname.notests
#%%exclude %python_sitelibdir/%modulename/core/handlers/modpython.py*
#%%exclude %python_sitelibdir/%modulename/contrib/auth/handlers/modpython.py*

%_bindir/django-admin
%_bindir/django-admin.py
%python_sitelibdir/*

%exclude %python_sitelibdir/%modulename/db/backends/mysql/
#exclude %python_sitelibdir/%modulename/db/backends/postgresql/
%exclude %python_sitelibdir/%modulename/db/backends/postgresql_psycopg2/
%exclude %python_sitelibdir/%modulename/db/backends/sqlite3/

%exclude %python_sitelibdir/%modulename/__pycache__
%exclude %python_sitelibdir/%modulename/*/__pycache__
%exclude %python_sitelibdir/%modulename/*/*/__pycache__
%exclude %python_sitelibdir/%modulename/*/*/*/__pycache__
%exclude %python_sitelibdir/%modulename/*/*/*/*/__pycache__
%exclude %python_sitelibdir/%modulename/*/*/*/*/*/__pycache__

%config %_sysconfdir/bash_completion.d/django.sh

%files tests -f %oname.tests

%if_with python3
%files -n %py3_name -f ../python3/%oname.notests
%_bindir/django-admin.py3
%python3_sitelibdir/*
#exclude %python3_sitelibdir/%oname/core/handlers/modpython.py*
#exclude %python3_sitelibdir/%oname/contrib/auth/handlers/modpython.py*

%exclude %python3_sitelibdir/%oname/db/backends/mysql/
#exclude %python3_sitelibdir/%oname/db/backends/postgresql/
%exclude %python3_sitelibdir/%oname/db/backends/postgresql_psycopg2/
%exclude %python3_sitelibdir/%oname/db/backends/sqlite3/

%exclude %python3_sitelibdir/%oname/*/*/*/test*
%exclude %python3_sitelibdir/%oname/*/*/*/*/test*

%files -n %py3_name-tests -f ../python3/%oname.tests
%python3_sitelibdir/%oname/*/*/*/test*
%python3_sitelibdir/%oname/*/*/*/*/test*
%endif

%files doc
%doc docs

#%%files mod_python
#%%python_sitelibdir/%modulename/core/handlers/modpython.py*
#%%python_sitelibdir/%modulename/contrib/auth/handlers/modpython.py*

%files dbbackend-mysql
%python_sitelibdir/%modulename/db/backends/mysql/

#files dbbackend-psycopg
#python_sitelibdir/%modulename/db/backends/postgresql/

%files dbbackend-psycopg2
%python_sitelibdir/%modulename/db/backends/postgresql_psycopg2/

%files dbbackend-sqlite3
%python_sitelibdir/%modulename/db/backends/sqlite3/

%if_with python3
#files -n %py3_name-mod_python
#python3_sitelibdir/%oname/core/handlers/modpython.py*
#python3_sitelibdir/%oname/contrib/auth/handlers/modpython.py*

%files -n %py3_name-dbbackend-mysql
%python3_sitelibdir/%oname/db/backends/mysql/

#files -n %py3_name-dbbackend-psycopg
#python3_sitelibdir/%oname/db/backends/postgresql/

%files -n %py3_name-dbbackend-psycopg2
%python3_sitelibdir/%oname/db/backends/postgresql_psycopg2/

%files -n %py3_name-dbbackend-sqlite3
%python3_sitelibdir/%oname/db/backends/sqlite3/
%endif

%changelog
* Thu Feb 02 2017 Alexey Shabalin <shaba@altlinux.ru> 1.8.17-alt1
- 1.8.17
- fixed CVE-2016-9013,CVE-2016-9014 

* Mon Oct 24 2016 Alexey Shabalin <shaba@altlinux.ru> 1.8.15-alt1
- 1.8.15
- fixed CVE-2016-2512,CVE-2016-2513,CVE-2016-6186,CVE-2016-7401

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.8.7-alt1.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.8.7-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1.8.7-alt1.1
- NMU: Use buildreq for BR.

* Fri Nov 27 2015 Alexey Shabalin <shaba@altlinux.ru> 1.8.7-alt1
- 1.8.7
- fixed CVE-2015-8213

* Tue Oct 13 2015 Alexey Shabalin <shaba@altlinux.ru> 1.8.5-alt1
- 1.8.5
- fixed CVE-2015-5143, CVE-2015-5144, CVE-2015-5145, CVE-2015-5964, CVE-2015-5963

* Thu Apr 02 2015 Alexey Shabalin <shaba@altlinux.ru> 1.8-alt2
- Version 1.8

* Wed Apr 01 2015 Alexey Shabalin <shaba@altlinux.ru> 1.8-alt1.c1
- Version 1.8c1

* Thu Feb 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt1.b1
- Version 1.8b1

* Wed Oct 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1
- Version 1.7

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.6-alt1
- Version 1.6.6

* Sat Jul 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.5-alt1
- Version 1.6.5

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1.1
- Use 'find... -exec...' instead of 'for ... $(find...'

* Wed Apr 03 2013 Aleksey Avdeev <solo@altlinux.ru> 1.5.1-alt1
- Version 1.5.1
- Fix python3-module-django

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.5.0-alt4.1
- Rebuild with Python-3.3

* Wed Feb 27 2013 Aleksey Avdeev <solo@altlinux.ru> 1.5.0-alt4
- Rename package to python-module-django

* Wed Feb 27 2013 Aleksey Avdeev <solo@altlinux.ru> 1.5.0-alt3
- Version 1.5.0

* Tue Feb 26 2013 Aleksey Avdeev <solo@altlinux.ru> 1.5.0-alt2.rc2
- Version 1.5.0-rc2
- Rename package to python-module-django1.5
- Remove %%name-mod_python subpackage

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
