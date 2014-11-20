%define module_name celery

%def_with python3
%def_disable check

Name: python-module-%module_name
Version: 3.1.17
Release: alt1.git20141119
Group: Development/Python
License: BSD License
Summary: Celery is an open source asynchronous task queue/job queue based on distributed message passing
URL: https://github.com/celery/celery
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-sphinx-devel
BuildPreReq: python-module-billiard python-module-kombu-tests
BuildPreReq: python-module-sphinxcontrib-issuetracker python-module-nose
BuildPreReq: python-module-dateutil texlive-latex-recommended
BuildPreReq: python-module-amqplib dvipng python-module-anyjson
BuildPreReq: python-module-pytz python-module-unittest2
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python-tools-2to3 python3-module-anyjson
BuildPreReq: python3-module-pytz python3-module-unittest2
BuildPreReq: python3-module-billiard python3-module-kombu-tests
BuildPreReq: python3-module-amqp python3-module-nose
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

%files docs
%doc docs/.build/html/*

%if_with python3
%files -n python3-module-%module_name
%doc Changelog *.txt *.rst TODO
%_bindir/*.py3
%python3_sitelibdir/celery*
%endif

%changelog
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
