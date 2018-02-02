%define oname django-facebook

%def_disable check

Name: python-module-%oname
Version: 6.0.2
Release: alt1.git20141016.1
Summary: Facebook open graph API client in python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-facebook/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tschellenbach/Django-facebook.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel python-module-sphinx_rtd_theme
BuildPreReq: python-module-django-tests python-modules-sqlite3
BuildPreReq: python-module-django-dbbackend-sqlite3
BuildPreReq: python-module-unidecode python-module-celery
BuildPreReq: python-module-memcached python-module-Pillow
BuildPreReq: python-module-mock python-module-pytest
BuildPreReq: python-module-pytest-django

%description
Facebook open graph API client in python. Enables django applications to
register users using facebook. Fixes issues with the official but
unsupported Facebook python-sdk. Enables mobile facebook authentication.
Canvas page authentication for facebook applications. FQL access via the
server side api.

%package tests
Summary: Tests for Facebook open graph API client in python
Group: Development/Python
Requires: %name = %EVR
%add_python_req_skip test

%description tests
Facebook open graph API client in python. Enables django applications to
register users using facebook. Fixes issues with the official but
unsupported Facebook python-sdk. Enables mobile facebook authentication.
Canvas page authentication for facebook applications. FQL access via the
server side api.

This package contains tests for Facebook open graph API client in
python.

%package pickles
Summary: Pickles for Facebook open graph API client in python
Group: Development/Python

%description pickles
Facebook open graph API client in python. Enables django applications to
register users using facebook. Fixes issues with the official but
unsupported Facebook python-sdk. Enables mobile facebook authentication.
Canvas page authentication for facebook applications. FQL access via the
server side api.

This package contains pickles for Facebook open graph API client in
python.

%package docs
Summary: Pickles for Facebook open graph API client in python
Group: Development/Documentation
BuildArch: noarch

%description docs
Facebook open graph API client in python. Enables django applications to
register users using facebook. Fixes issues with the official but
unsupported Facebook python-sdk. Enables mobile facebook authentication.
Canvas page authentication for facebook applications. FQL access via the
server side api.

This package contains documentation for Facebook open graph API client
in python.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%install
%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test

%files
%doc AUTHORS *.rest
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests.py*
%exclude %python_sitelibdir/*/test_utils

%files tests
%python_sitelibdir/*/tests.py*
%python_sitelibdir/*/test_utils

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 6.0.2-alt1.git20141016.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0.2-alt1.git20141016
- Version 6.0.2

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0.1-alt1.git20140903
- Initial build for Sisyphus

