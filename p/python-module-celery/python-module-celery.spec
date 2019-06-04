%define _unpackaged_files_terminate_build 1

%define oname celery

%add_python3_req_skip celery.utils.nodenames
%add_python3_req_skip celery.utils.time

%def_with python3
%def_without s3
# wait for new botocore, pytest
%def_disable check

Name: python-module-%oname
Version: 4.3.0
Release: alt2

Summary: Celery is an open source asynchronous task queue/job queue based on distributed message passing

Group: Development/Python
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
BuildRequires: dvipng
# /proc is required for some tests
BuildRequires: /proc
BuildRequires: python-module-setuptools
%if_enabled check
BuildRequires: python3-module-botocore >= 1.10.29
BuildRequires: python3-module-botocore < 1.11.0
BuildRequires: python-module-mock
BuildRequires: python-module-pytest >= 4.3.1
BuildRequires: python-module-pytest < 4.4.0
%if_with s3
BuildRequires: python-module-moto >= 1.3.7
%endif
%endif
%py_use kombu = 4.4.0
%py_use billiard >= 3.6.0
BuildRequires: python-module-alabaster python-module-objects.inv python2.7(sphinx_celery)
BuildRequires: python-module-html5lib python-module-nose python-module-pbr
BuildRequires: python-module-sphinxcontrib-issuetracker python-module-unittest2
BuildRequires: python2.7(case) python2.7(eventlet)
BuildRequires: python2.7(redis)
BuildRequires(pre): rpm-macros-sphinx

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
%if_enabled check
BuildRequires: python3-module-botocore >= 1.10.29
BuildRequires: python3-module-botocore < 1.11.0
BuildRequires: python3-module-mock
BuildRequires: python3-module-pytest >= 4.3.1
BuildRequires: python3-module-pytest < 4.4.0
%if_with s3
BuildRequires: python3-module-moto >= 1.3.7
%endif
%endif
BuildRequires: python3-module-html5lib python3-module-nose python3-module-pbr
BuildRequires: python3-module-pycrypto
BuildRequires: python3-module-django python3-module-ecdsa python3-module-pytz python3-module-unittest2 python3(requests)
BuildRequires: python3(case) python3(eventlet) python3(billiard)
BuildRequires: python3(redis)
%endif

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

%if_with python3
%package -n python3-module-%oname
Summary: Celery is an open source asynchronous task queue/job queue based on distributed message passing
Group: Development/Python3
%py3_use kombu = 4.4.0
%py3_use billiard >= 3.6.0

%description -n python3-module-%oname
Celery is an open source asynchronous task queue/job queue based on
distributed message passing.  It is focused on real-time operation,
but supports scheduling as well.

The execution units, called tasks, are executed concurrently on one or
more worker nodes using multiprocessing, `Eventlet`_ or `gevent`_.  Tasks can
execute asynchronously (in the background) or synchronously
(wait until ready).

Celery is used in production systems to process millions of tasks a day.
%endif

%prep
%setup
#patch1 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

# disable moto using (needed for S3 tests)
subst "s|moto==.*||" requirements/test.txt

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
# skip using moto
rm -fv celery/t/unit/backends/test_s3.py

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

%if "%_target_libdir_noarch" != "%_libdir"
mv %buildroot%_target_libdir_noarch %buildroot%_libdir
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs html

%check
rm -f t/unit/contrib/test_sphinx.py
python setup.py test

%if_with python3
pushd ../python3
rm -f t/unit/contrib/test_sphinx.py
python3 setup.py test
popd
%endif

%files
%doc Changelog *.txt *.rst TODO
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/celery*

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc Changelog *.txt *.rst TODO
%_bindir/*.py3
%python3_sitelibdir/celery*
%endif

%changelog
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
