%define oname pybald

%def_with python3

Name: python-module-%oname
Version: 0.3.1
Release: alt1.git20150219
Summary: An light weight MVC-style python web framework for learning and hacking
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pybald/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mikepk/pybald.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pybald-routes python-module-FormAlchemy
BuildPreReq: python-module-SQLAlchemy python-module-webob
BuildPreReq: python-module-mako python-module-memcached
BuildPreReq: python-module-webassets python-module-lxml
BuildPreReq: python-module-rjsmin python-module-cssmin
BuildPreReq: python-module-simple-db-migrate python-module-WebHelpers2
BuildPreReq: python-modules-logging python-modules-json
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pybald-routes python3-module-FormAlchemy
BuildPreReq: python3-module-SQLAlchemy python3-module-webob
BuildPreReq: python3-module-mako python3-module-memcached
BuildPreReq: python3-module-webassets python3-module-lxml
BuildPreReq: python3-module-rjsmin python3-module-cssmin
BuildPreReq: python3-module-WebHelpers2
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires pybald-routes formalchemy sqlalchemy webob mako memcache
%py_requires webassets lxml rjsmin cssmin logging json webhelpers2
%add_python_req_skip project newrelic

%description
Pybald is a light weight, python, MVC style web framework. It is
inspired by work done by Ian Bicking, and builds upon the concepts
presented in Another do-it-yourself framework. It is also takes design
inspiration from Ruby on Rails and Django.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Pybald is a light weight, python, MVC style web framework. It is
inspired by work done by Ian Bicking, and builds upon the concepts
presented in Another do-it-yourself framework. It is also takes design
inspiration from Ruby on Rails and Django.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: An light weight MVC-style python web framework for learning and hacking
Group: Development/Python3
%py3_provides %oname
%py3_requires pybald-routes formalchemy sqlalchemy webob mako memcache
%py3_requires webassets lxml rjsmin cssmin logging json webhelpers2
%add_python3_req_skip project newrelic

%description -n python3-module-%oname
Pybald is a light weight, python, MVC style web framework. It is
inspired by work done by Ian Bicking, and builds upon the concepts
presented in Another do-it-yourself framework. It is also takes design
inspiration from Ruby on Rails and Django.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Pybald is a light weight, python, MVC style web framework. It is
inspired by work done by Ian Bicking, and builds upon the concepts
presented in Another do-it-yourself framework. It is also takes design
inspiration from Ruby on Rails and Django.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Pybald is a light weight, python, MVC style web framework. It is
inspired by work done by Ian Bicking, and builds upon the concepts
presented in Another do-it-yourself framework. It is also takes design
inspiration from Ruby on Rails and Django.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Pybald is a light weight, python, MVC style web framework. It is
inspired by work done by Ian Bicking, and builds upon the concepts
presented in Another do-it-yourself framework. It is also takes design
inspiration from Ruby on Rails and Django.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/test.*

%files tests
%python_sitelibdir/*/test.*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test.*
%exclude %python3_sitelibdir/*/*/test.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test.*
%python3_sitelibdir/*/*/test.*
%endif

%changelog
* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20150219
- Initial build for Sisyphus

