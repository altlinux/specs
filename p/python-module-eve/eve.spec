%define oname eve

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.5
Release: alt1.git20150112
Summary: REST API framework powered by Flask, MongoDB and good intentions
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Eve/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/nicolaiarocci/eve.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-cerberus python-module-events
BuildPreReq: python-module-simplejson python-module-werkzeug
BuildPreReq: python-module-markupsafe python-module-jinja2
BuildPreReq: python-module-itsdangerous python-module-flask
BuildPreReq: python-module-pymongo python-module-flask-pymongo
BuildPreReq: python-module-redis-py
BuildPreReq: python-module-sphinx-devel python-module-alabaster
BuildPreReq: python-module-sphinxcontrib-embedly
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-cerberus python3-module-events
BuildPreReq: python3-module-simplejson python3-module-werkzeug
BuildPreReq: python3-module-markupsafe python3-module-jinja2
BuildPreReq: python3-module-itsdangerous python3-module-flask
BuildPreReq: python3-module-pymongo python3-module-flask-pymongo
BuildPreReq: python3-module-redis-py
%endif

%py_provides %oname
%py_requires flask_pymongo

%description
Powered by Flask, MongoDB, Redis and good intentions Eve allows to
effortlessly build and deploy highly customizable, fully featured
RESTful Web Services.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Powered by Flask, MongoDB, Redis and good intentions Eve allows to
effortlessly build and deploy highly customizable, fully featured
RESTful Web Services.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: REST API framework powered by Flask, MongoDB and good intentions
Group: Development/Python3
%py3_provides %oname
%py3_requires flask_pymongo

%description -n python3-module-%oname
Powered by Flask, MongoDB, Redis and good intentions Eve allows to
effortlessly build and deploy highly customizable, fully featured
RESTful Web Services.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Powered by Flask, MongoDB, Redis and good intentions Eve allows to
effortlessly build and deploy highly customizable, fully featured
RESTful Web Services.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Powered by Flask, MongoDB, Redis and good intentions Eve allows to
effortlessly build and deploy highly customizable, fully featured
RESTful Web Services.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Powered by Flask, MongoDB, Redis and good intentions Eve allows to
effortlessly build and deploy highly customizable, fully featured
RESTful Web Services.

This package contains documentation for %oname.

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%make -C docs pickle
%make -C docs html

cp -fR ~/code/eve.docs/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS CHANGES *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc ~/code/eve.docs/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGES *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20150112
- Version 0.5

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20140620
- Initial build for Sisyphus

