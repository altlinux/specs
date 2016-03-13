%define module_name celery

%def_with python3
%def_disable check

Name: python-module-%module_name
Version: 3.1.18
Release: alt1.git20150422.1.1
Group: Development/Python
License: BSD License
Summary: Celery is an open source asynchronous task queue/job queue based on distributed message passing
URL: https://github.com/celery/celery
Source: %name-%version.tar

#BuildPreReq: python-module-setuptools-tests python-module-sphinx-devel
#BuildPreReq: python-module-billiard python-module-kombu-tests
#BuildPreReq: python-module-sphinxcontrib-issuetracker python-module-nose
#BuildPreReq: python-module-dateutil texlive-latex-recommended
#BuildPreReq: python-module-amqplib dvipng python-module-anyjson
#BuildPreReq: python-module-pytz python-module-unittest2
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python-tools-2to3 python3-module-anyjson
#BuildPreReq: python3-module-pytz python3-module-unittest2
#BuildPreReq: python3-module-billiard python3-module-kombu-tests
#BuildPreReq: python3-module-amqp python3-module-nose
%endif

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: fontconfig python-base python-devel python-module-OpenSSL python-module-PyStemmer python-module-Pygments python-module-SQLAlchemy python-module-amqp python-module-anyjson python-module-babel python-module-backports python-module-bson python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-django python-module-docutils python-module-ecdsa python-module-enum34 python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-ndg-httpsclient python-module-ntlm python-module-psycopg2 python-module-pyasn1 python-module-pycrypto python-module-pymongo python-module-pytest python-module-pytz python-module-setuptools python-module-simplejson python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-sphinxcontrib python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-curses python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python3 python3-base python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pip python3-module-psycopg2 python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-yaml python3-module-yieldfrom.http.client python3-module-yieldfrom.urllib3 t1lib tex-common texlive-base texlive-base-bin texlive-common texlive-generic-recommended texlive-latex-base texlive-latex-recommended
BuildRequires: dvipng python-module-alabaster python-module-billiard python-module-html5lib python-module-kombu python-module-nose python-module-objects.inv python-module-pbr python-module-setuptools-tests python-module-sphinxcontrib-issuetracker python-module-unittest2 python3-module-django python3-module-ecdsa python3-module-html5lib python3-module-nose python3-module-pbr python3-module-pycrypto python3-module-pytz python3-module-setuptools-tests python3-module-unittest2 python3-module-yieldfrom.requests rpm-build-python3 time

%description
Celery is an open source asynchronous task queue/job queue based on
distributed message passing.  It is focused on real-time operation,
but supports scheduling as well.

The execution units, called tasks, are executed concurrently on one or
more worker nodes using multiprocessing, `Eventlet`_ or `gevent`_.  Tasks can
execute asynchronously (in the background) or synchronously
(wait until ready).

Celery is used in production systems to process millions of tasks a day.

%package tests
Summary: Tests for %module_name
Group: Development/Python
Requires: %name = %EVR

%description tests
Celery is an open source asynchronous task queue/job queue based on
distributed message passing.  It is focused on real-time operation,
but supports scheduling as well.

The execution units, called tasks, are executed concurrently on one or
more worker nodes using multiprocessing, `Eventlet`_ or `gevent`_.  Tasks can
execute asynchronously (in the background) or synchronously
(wait until ready).

Celery is used in production systems to process millions of tasks a day.

This package contains tests for %module_name.

%package docs
Summary: Documentation for %module_name
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

This package contains documentation for %module_name.

%package -n python3-module-%module_name
Summary: Celery is an open source asynchronous task queue/job queue based on distributed message passing
Group: Development/Python3

%description -n python3-module-%module_name
Celery is an open source asynchronous task queue/job queue based on
distributed message passing.  It is focused on real-time operation,
but supports scheduling as well.

The execution units, called tasks, are executed concurrently on one or
more worker nodes using multiprocessing, `Eventlet`_ or `gevent`_.  Tasks can
execute asynchronously (in the background) or synchronously
(wait until ready).

Celery is used in production systems to process millions of tasks a day.

%package -n python3-module-%module_name-tests
Summary: Tests for %module_name
Group: Development/Python3
Requires: python3-module-%module_name = %EVR

%description -n python3-module-%module_name-tests
Celery is an open source asynchronous task queue/job queue based on
distributed message passing.  It is focused on real-time operation,
but supports scheduling as well.

The execution units, called tasks, are executed concurrently on one or
more worker nodes using multiprocessing, `Eventlet`_ or `gevent`_.  Tasks can
execute asynchronously (in the background) or synchronously
(wait until ready).

Celery is used in production systems to process millions of tasks a day.

This package contains tests for %module_name.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

%ifarch x86_64
mv %buildroot%_target_libdir_noarch %buildroot%_libdir
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs html

%check
python setup.py test
%if_with python3
pushd ../python3
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
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files docs
%doc docs/.build/html/*

%if_with python3
%files -n python3-module-%module_name
%doc Changelog *.txt *.rst TODO
%_bindir/*.py3
%python3_sitelibdir/celery*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%module_name-tests
%python3_sitelibdir/*/tests
%endif

%changelog
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
