%define branch 5.0
%define origname Django
%define oname django

%def_enable check

%add_python3_req_skip hotshot StringIO
%add_findreq_skiplist %python3_sitelibdir/%oname/contrib/gis/db/backends/*/*

Summary: A high-level Python 3 Web framework that encourages rapid development and clean, pragmatic design.
Name: python3-module-%oname
Version: %branch.7
Release: alt1
Source0: %origname-%version.tar
License: BSD-3-Clause
Group: Development/Python3
BuildArch: noarch
VCS: https://github.com/django/django
URL: http://www.djangoproject.com/
Provides: %name%branch = %EVR
Provides: %name%branch-tests = %EVR
Obsoletes: %name%branch < %EVR
Obsoletes: %name%branch-tests < %EVR
Provides: %name-tests = %EVR
Obsoletes: %name-tests < %EVR

%py3_provides django.core.management.commands.loaddata
%py3_provides django.core.management.commands.test
%py3_provides django.core.management.commands.runserver

Conflicts: python3-module-django1.11
Conflicts: python3-module-django1.11-tests

%add_python3_req_skip django.test.signals

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-setuptools-wheel
BuildRequires: python3-module-asgiref >= 3.6.0
BuildRequires: python3-module-sqlparse >= 0.3.1
BuildRequires: bash-completion

%if_enabled check
BuildRequires: python3(sqlparse)
BuildRequires: python3(pytz)
BuildRequires: python3(sqlite3)
BuildRequires: python3(jinja2)
BuildRequires: python3(numpy)
BuildRequires: python3(pylibmc)
BuildRequires: python3(memcache)
BuildRequires: python3(yaml)
BuildRequires: python3(selenium)
%endif

%description
%summary

%package dbbackend-mysql
Summary: MySQLSQL support for Django
Group: Development/Python3
Requires: %name = %EVR
Provides: %name%branch-dbbackend-mysql = %EVR
Obsoletes: %name%branch-dbbackend-mysql < %EVR
Conflicts: python3-module-django1.11-dbbackend-mysql
%py3_requires MySQLdb

%description dbbackend-mysql
%summary

%package dbbackend-postgresql
Summary: PostgreSQL support for Django.
Group: Development/Python3
Requires: %name = %EVR
Provides: %name%branch-dbbackend-psycopg = %EVR
Obsoletes: %name%branch-dbbackend-psycopg < %EVR
Provides: %name%branch-dbbackend-psycopg2 = %EVR
Obsoletes: %name%branch-dbbackend-psycopg2 < %EVR
Conflicts: python3-module-django1.11-dbbackend-psycopg
Conflicts: python3-module-django1.11-dbbackend-psycopg2
%py3_requires psycopg2

%description dbbackend-postgresql
%summary

%package dbbackend-sqlite3
Summary: SQLite3 support for Django (Python 3)
Group: Development/Python3
Requires: %name = %EVR
Provides: %name%branch-dbbackend-sqlite3 = %EVR
Obsoletes: %name%branch-dbbackend-sqlite3 < %EVR
Conflicts: python3-module-django1.11-dbbackend-sqlite3
%py3_requires sqlite3

%description dbbackend-sqlite3
%summary

%package dbbackend-oracle
Summary: Oracle support for Django (Python 3)
Group: Development/Python3
Requires: %name = %EVR
Provides: %name%branch-dbbackend-oracle = %EVR
Obsoletes: %name%branch-dbbackend-oracle < %EVR
%add_python3_req_skip cx_Oracle

%description dbbackend-oracle
%summary

%package doc
Summary: Django documentation
Group: Development/Python3
Provides: %name%branch-doc = %EVR
Obsoletes: %name%branch-doc < %EVR
Conflicts: python3-module-django1.11-doc

%description doc
%summary

%prep
%setup -n %origname-%version

# Use system six instead of bundled
find -type f -name '*.py*' -exec sed -i 's|django.utils.six|six|'  -- '{}' +

find -type f -name '*.py*' -exec sed -i 's|%_bindir/env python|%_bindir/python3|' -- '{}' +
find -type f -name '*.py' -exec sed -i 's|.*from future_builtins import zip.*||' -- '{}' +

%build
%python3_build

%install
export LC_ALL=en_US.UTF-8
%python3_install

# install man pages (for the main executable only)
mkdir -p %buildroot%_man1dir
cp -p docs/man/* %buildroot%_man1dir

# install bash completion script
bashcompdir=$(pkg-config --variable=completionsdir bash-completion)
mkdir -p %{buildroot}$bashcompdir
install -m 0644 -p extras/django_bash_completion \
  %{buildroot}$bashcompdir/django-admin

ln -s django-admin %{buildroot}$bashcompdir/django-admin-3
ln -s django-admin %{buildroot}$bashcompdir/python3-django-admin

# Add backward compatible links to %%{_bindir}
ln -s ./django-admin %buildroot%_bindir/django-admin-3
ln -s ./django-admin %buildroot%_bindir/python3-django-admin

# remove .po files
find %buildroot -name "*.po" | xargs rm -f

%check
export PYTHONPATH=$(pwd)
cd tests
LANG="en_US.UTF-8" python3 runtests.py --settings=test_sqlite --verbosity=2 --parallel 1

%files
%_bindir/*
%_man1dir/*
%_datadir/bash-completion/completions/*
%python3_sitelibdir/*
#exclude %%python3_sitelibdir/%%oname/core/handlers/modpython.py*
#exclude %%python3_sitelibdir/%%oname/contrib/auth/handlers/modpython.py*

%exclude %python3_sitelibdir/%oname/db/backends/mysql
%exclude %python3_sitelibdir/%oname/db/backends/postgresql
%exclude %python3_sitelibdir/%oname/db/backends/sqlite3
%exclude %python3_sitelibdir/%oname/db/backends/oracle

%files doc
%doc docs

%files dbbackend-mysql
%python3_sitelibdir/%oname/db/backends/mysql

%files dbbackend-postgresql
%python3_sitelibdir/%oname/db/backends/postgresql

%files dbbackend-oracle
%python3_sitelibdir/%oname/db/backends/oracle

%files dbbackend-sqlite3
%python3_sitelibdir/%oname/db/backends/sqlite3

%changelog
* Mon Jul 15 2024 Alexander Burmatov <thatman@altlinux.org> 5.0.7-alt1
- New version 5.0.7.
- Fixes for the following security vulnerabilities:
  + CVE-2024-24680: Potential denial-of-service in intcomma template filter
  + CVE-2024-27351: Potential regular expression denial-of-service in django.utils.text.Truncator.words()
  + CVE-2024-38875: Potential denial-of-service vulnerability in django.utils.html.urlize()
  + CVE-2024-39329: Username enumeration through timing difference for users with unusable passwords
  + CVE-2024-39330: Potential directory-traversal via Storage.save()
  + CVE-2024-39614: Potential denial-of-service vulnerability in get_supported_language_variant()
- Some bugfixes.

* Mon May 20 2024 Alexander Burmatov <thatman@altlinux.org> 4.2.13-alt1
- New version 4.2.13.
- Fixed a crash in Django 4.2 when validating email max line lengths with
content decoded using the surrogateescape error handling scheme.
- Fixes a packaging error in 4.2.12.

* Fri Mar 22 2024 Alexander Burmatov <thatman@altlinux.org> 4.2.11-alt1
- New version 4.2.11.
- Fixes a security issue with severity "moderate" and a regression in 4.2.10.
- Fixes for the following security vulnerabilities:
  + CVE-2024-24680: Potential denial-of-service in intcomma template filter
  + CVE-2024-27351: Potential regular expression denial-of-service in django.utils.text.Truncator.words()

* Mon Jan 29 2024 Alexander Burmatov <thatman@altlinux.org> 4.2.9-alt1
- New version 4.2.9.
- Fixed a regression in Django 4.2.8.

* Tue Dec 26 2023 Alexander Burmatov <thatman@altlinux.org> 4.2.8-alt1
- New version 4.2.8.

* Fri Oct 06 2023 Alexey Shabalin <shaba@altlinux.org> 4.2.6-alt1
- New version 4.2.6.
- Fixes for the following security vulnerabilities:
  + CVE-2023-41164 Potential denial of service vulnerability in django.utils.encoding.uri_to_iri()
  + CVE-2023-43665 Denial-of-service possibility in django.utils.text.Truncator

* Thu Aug 31 2023 Alexey Shabalin <shaba@altlinux.org> 4.2.4-alt2
- Update BR.

* Mon Aug 28 2023 Alexey Shabalin <shaba@altlinux.org> 4.2.4-alt1
- New version 4.2.4 (new 4.2 LTS release).

* Wed Jul 12 2023 Anton Farygin <rider@altlinux.ru> 3.2.20-alt1
- New version 3.2.19.
- Fixes for the following security vulnerabilities:
  + CVE-2023-36053 Potential regular expression denial of service vulnerability in EmailValidator/URLValidator

* Sat May 27 2023 Alexey Shabalin <shaba@altlinux.org> 3.2.19-alt1
- New version 3.2.19.
- Fixes for the following security vulnerabilities:
  + CVE-2023-31047 Potential bypass of validation when uploading multiple files using one form field

* Fri Mar 24 2023 Alexey Shabalin <shaba@altlinux.org> 3.2.18-alt1
- New version 3.2.18.
- Fixes for the following security vulnerabilities:
  + CVE-2023-23969 Potential denial-of-service via ``Accept-Language`` headers
  + CVE-2023-24580 Potential denial-of-service vulnerability in file uploads

* Tue Oct 11 2022 Alexey Shabalin <shaba@altlinux.org> 3.2.16-alt1
- new version 3.2.16
- Fixes for the following security vulnerabilities:
  + CVE-2022-41323 Potential denial-of-service vulnerability in internationalized URLs

* Mon Aug 22 2022 Alexey Shabalin <shaba@altlinux.org> 3.2.15-alt1
- new version 3.2.15
- Fixes for the following security vulnerabilities:
  + CVE-2022-34265 Potential SQL injection via Trunc(kind) and Extract(lookup_name) arguments.
  + CVE-2022-36359 Potential reflected file download vulnerability in FileResponse.

* Mon Apr 11 2022 Anton Farygin <rider@altlinux.ru> 3.2.13-alt1
- 3.2.12 -> 3.2.13
- Fixes:
  * CVE-2022-28346: Potential SQL injection in QuerySet.annotate(), aggregate(), and extra()
  * CVE-2022-28347: Potential SQL injection via QuerySet.explain(**options) on PostgreSQL

* Sun Feb 20 2022 Anton Farygin <rider@altlinux.ru> 3.2.12-alt1
- 3.2.11 -> 3.2.12
- Fixes for the following security vulnerabilities:
  + CVE-2022-22818: Possible XSS via {%% debug %%} template tag.
  + CVE-2022-23833: Denial-of-service possibility in file uploads.

* Tue Jan 18 2022 Alexey Shabalin <shaba@altlinux.org> 3.2.11-alt1
- new version 3.2.11
- Fixes for the following security vulnerabilities:
  + CVE-2021-45115 Prevented DoS vector in UserAttributeSimilarityValidator.
  + CVE-2021-45116 Fixed potential information disclosure in dictsort template filter.
  + CVE-2021-45452 Fixed potential path traversal in storage subsystem.

* Fri Dec 17 2021 Alexey Shabalin <shaba@altlinux.org> 3.2.10-alt1
- new version 3.2.10
- Fixes for the following security vulnerabilities:
  + CVE-2021-44420 Fixed potential bypass of an upstream access control based on URL paths.

* Fri Nov 05 2021 Alexey Shabalin <shaba@altlinux.org> 3.2.9-alt1
- new version 3.2.9

* Wed Aug 18 2021 Alexey Shabalin <shaba@altlinux.org> 3.2.6-alt1
- new version 3.2.6
- Rename dbbackend-psycopg2 to dbbackend-postgresql
- Add dbbackend-oracle package
- Fixes for the following security vulnerabilities:
  + CVE-2021-35042 Potential SQL injection via unsanitized QuerySet.order_by() input

* Tue Jul 13 2021 Alexey Shabalin <shaba@altlinux.org> 2.2.24-alt1
- new version 2.2.24
- Fixes for the following security vulnerabilities:
  + CVE-2021-28658 Potential directory-traversal via uploaded files
  + CVE-2021-31542 Potential directory-traversal via uploaded files
  + CVE-2021-32052 Header injection possibility since URLValidator accepted newlines in input on Python 3.9.5+
  + CVE-2021-33203 Potential directory traversal via admindocs
  + CVE-2021-33571 Possible indeterminate SSRF, RFI, and LFI attacks since validators accepted leading zeros in IPv4 addresses

* Wed Feb 24 2021 Alexey Shabalin <shaba@altlinux.org> 2.2.19-alt2
- Drop Provides: Django

* Wed Feb 24 2021 Alexey Shabalin <shaba@altlinux.org> 2.2.19-alt1
- 2.2.19
- rename package to python3-module-django back
- Fixes for the following security vulnerabilities:
  + CVE-2021-3281 Potential directory-traversal via archive.extract()
  + CVE-2021-23336 Web cache poisoning via django.utils.http.limited_parse_qsl()

* Tue Feb 09 2021 Grigory Ustinov <grenka@altlinux.org> 2.2.17-alt2
- Disable check for bootstrap of python3.9.

* Fri Dec 11 2020 Alexey Shabalin <shaba@altlinux.org> 2.2.17-alt1
- new version 2.2.17
- Fixes for the following security vulnerabilities:
  + CVE-2020-13254 Potential data leakage via malformed memcached keys
  + CVE-2020-13596 Possible XSS via admin ForeignKeyRawIdWidget
  + CVE-2020-24583: Incorrect permissions on intermediate-level directories on Python 3.7+
  + CVE-2020-24584: Permission escalation in intermediate-level directories of the file system cache on Python 3.7+

* Tue Apr 14 2020 Alexey Shabalin <shaba@altlinux.org> 2.2.12-alt3
- add more provides

* Sun Apr 12 2020 Alexey Shabalin <shaba@altlinux.org> 2.2.12-alt2
- merge tests package to main
- move bash-completions to %%_datadir
- add man pages to package
- enable tests

* Sun Apr 12 2020 Alexey Shabalin <shaba@altlinux.org> 2.2.12-alt1
- 2.2.12
- Fixes for the following security vulnerabilities:
  + CVE-2019-19118 Privilege escalation in the Django admin.
  + CVE-2019-19844 Potential account hijack via password reset form
  + CVE-2020-7471 Potential SQL injection via StringAgg(delimiter)
  + CVE-2020-9402 Potential SQL injection via tolerance parameter in GIS functions and aggregates on Oracle

* Fri Aug 23 2019 Alexey Appolonov <alexey@altlinux.org> 2.2.4-alt2
- Build with flagged conflict with python-module-django1.11
  (due to file '/etc/bash_completion.d/django.sh').

* Mon Aug 05 2019 Alexey Shabalin <shaba@altlinux.org> 2.2.4-alt1
- 2.2.4
- Fixes for the following security vulnerabilities:
  + CVE-2019-14232 Adjusted regex to avoid backtracking issues when truncating HTML
  + CVE-2019-14233 Prevented excessive HTMLParser recursion in strip_tags() when handling incomplete HTML entities
  + CVE-2019-14234 Protected JSONField/HStoreField key and index lookups against SQL injection
  + CVE-2019-14235 Fixed potential memory exhaustion in django.utils.encoding.uri_to_iri()

* Tue Jul 16 2019 Alexey Shabalin <shaba@altlinux.org> 2.2.3-alt2
- tear circular dependencies python3-module-django2.2 and python3-module-django2.2-tests

* Mon Jul 15 2019 Alexey Shabalin <shaba@altlinux.org> 2.2.3-alt1
- 2.2.3
- build python3 only
- rename package to python3-module-django2.2
- Fixes for the following security vulnerabilities:
  + CVE-2019-12781 Incorrect HTTP detection with reverse-proxy connecting via HTTPS
  + CVE-2019-12308 AdminURLFieldWidget XSS
  + CVE-2019-6975 Memory exhaustion in django.utils.numberformat.format()
  + CVE-2019-3498 Content spoofing possibility in the default 404 page
  + CVE-2018-16984 Password hash disclosure to view only admin users
  + CVE-2018-14574 Open redirect possibility in CommonMiddleware
  + CVE-2018-7536 Denial-of-service possibility in urlize and urlizetrunc template filters
  + CVE-2018-7537 Denial-of-service possibility in truncatechars_html and truncatewords_html template filters
  + CVE-2018-6188 Information leakage in AuthenticationForm

* Mon Dec 17 2018 Grigory Ustinov <grenka@altlinux.org> 1.11.17-alt1
- Build new version (Closes: #35861).
- Transfer to python3.
- Temporary disabled check.

* Wed Apr 12 2017 Alexey Shabalin <shaba@altlinux.ru> 1.8.18-alt1
- 1.8.18
- fixed CVE-2017-7233,CVE-2017-7234

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

* Mon Sep 24 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.97-alt0.1.svn6410
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
