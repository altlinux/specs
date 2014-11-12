%define oname pyramid_es

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.2.2
Release: alt1.git20141109
Summary: Elasticsearch integration for Pyramid
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_es/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/cartlogic/pyramid_es.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid-tests python-module-SQLAlchemy
BuildPreReq: python-module-six python-module-elasticsearch
BuildPreReq: python-module-nose python-module-nose-cover3
BuildPreReq: python-module-webtest
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid-tests python3-module-SQLAlchemy
BuildPreReq: python3-module-six python3-module-elasticsearch
BuildPreReq: python3-module-nose python3-module-nose-cover3
BuildPreReq: python3-module-webtest
%endif

%py_provides %oname

%description
pyramid_es is a pattern and set of utilities for integrating the
elasticsearch search engine with a Pyramid web app. It is intended to
make it easy to index a set of persisted objects and search those
documents inside Pyramid views.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires pyramid.testing

%description tests
pyramid_es is a pattern and set of utilities for integrating the
elasticsearch search engine with a Pyramid web app. It is intended to
make it easy to index a set of persisted objects and search those
documents inside Pyramid views.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Elasticsearch integration for Pyramid
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
pyramid_es is a pattern and set of utilities for integrating the
elasticsearch search engine with a Pyramid web app. It is intended to
make it easy to index a set of persisted objects and search those
documents inside Pyramid views.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires pyramid.testing

%description -n python3-module-%oname-tests
pyramid_es is a pattern and set of utilities for integrating the
elasticsearch search engine with a Pyramid web app. It is intended to
make it easy to index a set of persisted objects and search those
documents inside Pyramid views.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
pyramid_es is a pattern and set of utilities for integrating the
elasticsearch search engine with a Pyramid web app. It is intended to
make it easy to index a set of persisted objects and search those
documents inside Pyramid views.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
pyramid_es is a pattern and set of utilities for integrating the
elasticsearch search engine with a Pyramid web app. It is intended to
make it easy to index a set of persisted objects and search those
documents inside Pyramid views.

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

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif
exit 1

%files
%doc CHANGES *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGES *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.git20141109
- Initial build for Sisyphus

