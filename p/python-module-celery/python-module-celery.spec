%define module_name celery

%add_python3_req_skip celery.utils.nodenames
%add_python3_req_skip celery.utils.time
%add_python3_req_skip kombu.utils.objects

%def_with python3
%def_enable check

Name: python-module-%module_name
Version: 4.1.0
Release: alt1.1
Group: Development/Python
License: BSD License
Summary: Celery is an open source asynchronous task queue/job queue based on distributed message passing
URL: https://github.com/celery/celery

Source: %name-%version.tar

BuildRequires: dvipng
# /proc is required for some tests
BuildRequires: /proc
BuildRequires: python-module-setuptools
BuildRequires: python-module-mock
BuildRequires: python-module-alabaster python-module-billiard python-module-kombu python-module-objects.inv python2.7(sphinx_celery)
BuildRequires: python-module-html5lib python-module-nose python-module-pbr
BuildRequires: python-module-sphinxcontrib-issuetracker python-module-unittest2
BuildRequires: python2.7(case) python2.7(eventlet)
BuildRequires(pre): rpm-macros-sphinx
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pytest
BuildRequires: python3-module-html5lib python3-module-nose python3-module-pbr
BuildRequires: python3-module-pycrypto
BuildRequires: python3-module-django python3-module-ecdsa python3-module-pytz python3-module-unittest2 python3(requests)
BuildRequires: python3(case) python3(eventlet) python3(kombu) python3(billiard)
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

%if_with python3
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
%endif

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

%if "%_target_libdir_noarch" != "%_libdir"
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
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%module_name
%doc Changelog *.txt *.rst TODO
%_bindir/*.py3
%python3_sitelibdir/celery*
%endif

%changelog
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
