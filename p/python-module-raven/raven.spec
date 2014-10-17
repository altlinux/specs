%define oname raven

%def_with python3

Name: python-module-%oname
Version: 5.1.0
Release: alt1.git20141015
Summary: Raven is a client for Sentry
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/raven/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/getsentry/raven-python.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-billiard python-module-pytest
BuildPreReq: python-module-flake8 python-module-unittest2
BuildPreReq: python-module-flask python-module-blinker
BuildPreReq: python-module-flask-login python-module-paste
BuildPreReq: python-module-webpy python-module-certifi
BuildPreReq: python-module-bottle python-module-celery
BuildPreReq: python-module-django-tests python-module-django-celery
BuildPreReq: python-module-exam python-module-logbook
BuildPreReq: python-module-mock python-module-nose python-tools-pep8
BuildPreReq: python-module-pytz python-module-pytest-cov
BuildPreReq: python-module-pytest-django python-module-tornado
BuildPreReq: python-module-webob python-module-webtest
BuildPreReq: python-module-anyjson python-module-kombu
BuildPreReq: python-modules-multiprocessing python-module-sphinx-devel
BuildPreReq: python-module-django-dbbackend-sqlite3
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-billiard python3-module-pytest
BuildPreReq: python3-module-flake8 python3-module-unittest2
BuildPreReq: python3-module-flask python3-module-blinker
BuildPreReq: python3-module-flask-login python3-module-paste
BuildPreReq: python3-module-webpy python3-module-aiohttp
BuildPreReq: python3-module-bottle python3-module-celery
BuildPreReq: python3-module-django-tests python3-module-django-celery
BuildPreReq: python3-module-exam python3-module-logbook
BuildPreReq: python3-module-mock python3-module-nose python3-tools-pep8
BuildPreReq: python3-module-pytz python3-module-pytest-cov
BuildPreReq: python3-module-pytest-django python3-module-tornado
BuildPreReq: python3-module-webob python3-module-webtest
BuildPreReq: python3-module-anyjson python3-module-certifi
BuildPreReq: python3-module-django-dbbackend-sqlite3
BuildPreReq: python3-module-kombu
%endif

%py_provides %oname
%add_findreq_skiplist %python_sitelibdir/raven/transport/aiohttp.py

%description
Raven is a Python client for Sentry. It provides full out-of-the-box
support for many of the popular frameworks, including Django, and Flask.
Raven also includes drop-in support for any WSGI-compatible web
application.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Raven is a Python client for Sentry. It provides full out-of-the-box
support for many of the popular frameworks, including Django, and Flask.
Raven also includes drop-in support for any WSGI-compatible web
application.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Raven is a client for Sentry
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Raven is a Python client for Sentry. It provides full out-of-the-box
support for many of the popular frameworks, including Django, and Flask.
Raven also includes drop-in support for any WSGI-compatible web
application.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Raven is a Python client for Sentry. It provides full out-of-the-box
support for many of the popular frameworks, including Django, and Flask.
Raven also includes drop-in support for any WSGI-compatible web
application.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Raven is a Python client for Sentry. It provides full out-of-the-box
support for many of the popular frameworks, including Django, and Flask.
Raven also includes drop-in support for any WSGI-compatible web
application.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Raven is a Python client for Sentry. It provides full out-of-the-box
support for many of the popular frameworks, including Django, and Flask.
Raven also includes drop-in support for any WSGI-compatible web
application.

This package contains docs for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
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

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/pickle %buildroot%python_sitelibdir/%oname/

%check
rm -fR build
py.test
#if_with python3
%if 0
pushd ../python3
rm -fR build
py.test-%_python3_version
popd
%endif

%files
%doc AUTHORS CHANGES *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGES *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.0-alt1.git20141015
- Initial build for Sisyphus

