%define _unpackaged_files_terminate_build 1

%define oname celery

%add_python3_req_skip celery.utils.nodenames
%add_python3_req_skip celery.utils.time

%def_without s3
# wait for new botocore, pytest
%def_disable check
# AttributeError: module 'sphinx.ext.autodoc' has no attribute 'AutoDirective'
%def_without doc

Name: python3-module-%oname
Version: 5.3.4
Release: alt1

Summary: Celery is an open source asynchronous task queue/job queue based on distributed message passing

Group: Development/Python3
License: BSD License
URL: https://github.com/celery/celery

# https://github.com/celery/celery.git
# Source-url: https://pypi.io/packages/source/c/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

#Patch1: %oname-%version-alt-tests.patch

# Patches from Debian
Patch10: 0005-Disable-pytest-3.3-log-capturing-to-avoid-changing-l.patch
Patch11: 0007-Set-shell-in-su-invocation.patch
Patch12: privacy.patch

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3
BuildRequires: dvipng

BuildRequires: python3-module-html5lib
BuildRequires: python3(Crypto)
BuildRequires: python3-module-django python3-module-ecdsa python3-module-pytz python3(requests)
BuildRequires: python3(eventlet)
BuildRequires: python3(redis)

%if_with doc
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3(sphinx_celery)
BuildRequires: python3-module-sphinx
%endif

%py3_use kombu >= 4.6.10
%py3_use billiard >= 3.6.3
%py3_use vine >= 1.3.0

%if_enabled check
# /proc is required for some tests
BuildRequires: /proc
BuildRequires: python3-module-botocore >= 1.10.29
BuildRequires: python3-module-botocore < 1.11.0
BuildRequires: python3-module-mock
BuildRequires: python3-module-pytest >= 4.3.1
BuildRequires: python3-module-pytest < 4.4.0
%endif

%if_with s3
BuildRequires: python3-module-moto >= 1.3.7
%endif

Conflicts: python-module-celery

# due /usr/bin/celery
Obsoletes: python-module-celery

%description
Celery is an open source asynchronous task queue/job queue based on
distributed message passing.  It is focused on real-time operation,
but supports scheduling as well.

The execution units, called tasks, are executed concurrently on one or
more worker nodes using multiprocessing, `Eventlet`_ or `gevent`_.  Tasks can
execute asynchronously (in the background) or synchronously
(wait until ready).

Celery is used in production systems to process millions of tasks a day.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Celery is an open source asynchronous task queue/job queue based on
distributed message passing.  It is focused on real-time operation,
but supports scheduling as well.

The execution units, called tasks, are executed concurrently on one or
more worker nodes using multiprocessing, `Eventlet`_ or `gevent`_.  Tasks can
execute asynchronously (in the background) or synchronously
(wait until ready).

Celery is used in production systems to process millions of tasks a day.

This package contains documentation for %oname.

%package sphinx
Summary: Sphinx documentation plugin used to document tasks
Group: Development/Python3
Requires: %name = %EVR

%description sphinx
Sphinx documentation plugin used to document tasks.

%prep
%setup
#patch1 -p1
#patch10 -p1
%patch11 -p1
#patch12 -p1

# disable moto using (needed for S3 tests)
subst "s|moto==.*||" requirements/test.txt

%build
# skip using moto
rm -fv celery/t/unit/backends/test_s3.py

%python3_build_debug

%install
%python3_install

# FIXME: hack
%if "%_target_libdir_noarch" != "%_libdir"
mv %buildroot%_target_libdir_noarch %buildroot%_libdir
%endif

%if_with doc
%make -C docs html SPHINXBUILD=sphinx-build-3
%endif

%check
rm -f t/unit/contrib/test_sphinx.py
%python3_test

%files
%doc *.txt *.rst TODO
%_bindir/*
%python3_sitelibdir/celery*
%exclude %python3_sitelibdir/celery/contrib/sphinx.py

%files sphinx
%python3_sitelibdir/celery/contrib/sphinx.py

%if_with doc
%files docs
%doc docs/_build/html/*
%endif

%changelog
* Sun Oct 01 2023 Vitaly Lipatov <lav@altlinux.ru> 5.3.4-alt1
- new version 5.3.4 (with rpmrb script)

* Sun Jul 17 2022 Vitaly Lipatov <lav@altlinux.ru> 5.2.7-alt1
- new version 5.2.7 (with rpmrb script)

* Wed Jun 29 2022 Grigory Ustinov <grenka@altlinux.org> 5.2.3-alt2
- Fixed BuildRequires.

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 5.2.3-alt1
- new version 5.2.3 (with rpmrb script)

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 5.1.2-alt1
- new version 5.1.2 (with rpmrb script)

* Tue Apr 27 2021 Vitaly Lipatov <lav@altlinux.ru> 4.4.7-alt2
- separate sphinx plugin

* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 4.4.7-alt1
- new version (4.4.7) with rpmgs script

* Wed Oct 28 2020 Vitaly Lipatov <lav@altlinux.ru> 4.3.0-alt5
- add Obsoletes: python-module-celery (due /usr/bin/celery command)

* Wed Oct 07 2020 Vitaly Lipatov <lav@altlinux.ru> 4.3.0-alt4
- add Conflicts: python-module-celery

* Thu Sep 10 2020 Vitaly Lipatov <lav@altlinux.ru> 4.3.0-alt3
- build standalone python3 module
- temp. disable doc ()

* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 4.3.0-alt2
- update requires

* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 4.3.0-alt1
- new version 4.3.0 (with rpmrb script)
- switch to build from tarball
- temp. disable check due obsoleted moto module

* Thu Sep 13 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.1-alt1
- Updated to upstream version 4.2.1.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.1.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Nov 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.1.0-alt1
- Updated to upstream version 4.1.0.
- Enabled tests.

* Thu Jun 01 2017 Lenar Shakirov <snejok@altlinux.ru> 3.1.24-alt1
- Version 3.1.24
- Revert real@ patches

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.1.18-alt1.git20150422.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.1.18-alt1.git20150422.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.1.18-alt1.git20150422.1
- NMU: Use buildreq for BR.

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.18-alt1.git20150422
- Version 3.1.18
- Extracted tests into separate package

* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.17-alt1.git20141119
- Version 3.1.17

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.16-alt1.git20141003
- Version 3.1.16

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.13-alt1.git20140710
- Version 3.1.13
- Added module for Python 3

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.3-alt2
- Added module for Python 3

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.3-alt1.1
- Fixed build

* Thu May 03 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.5.3-alt1
- build for ALT
