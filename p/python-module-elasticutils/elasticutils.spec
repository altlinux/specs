%define oname elasticutils

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.11
Release: alt1.dev.git20141010.1
Summary: A friendly chainable ElasticSearch interface for python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/elasticutils/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mozilla/elasticutils.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-elasticsearch python-module-six
BuildPreReq: python-module-nose python-module-tox
BuildPreReq: python-module-twine python-module-wheel
BuildPreReq: python-module-django-tests python-module-celery
BuildPreReq: python-module-django-celery
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-elasticsearch python3-module-six
BuildPreReq: python3-module-nose python3-module-tox
BuildPreReq: python3-module-twine python3-module-wheel
BuildPreReq: python3-module-django python3-module-celery
BuildPreReq: python3-module-django-celery
%endif

%py_provides %oname

%description
ElasticUtils is a convenient Django QuerySet-like API for querying
Elasticsearch.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
ElasticUtils is a convenient Django QuerySet-like API for querying
Elasticsearch.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A friendly chainable ElasticSearch interface for python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
ElasticUtils is a convenient Django QuerySet-like API for querying
Elasticsearch.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
ElasticUtils is a convenient Django QuerySet-like API for querying
Elasticsearch.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
ElasticUtils is a convenient Django QuerySet-like API for querying
Elasticsearch.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
ElasticUtils is a convenient Django QuerySet-like API for querying
Elasticsearch.

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
python run_tests.py
%if_with python3
pushd ../python3
python3 setup.py test
python3 run_tests.py
popd
%endif
exit 1

%files
%doc CHANGELOG CONTRIBUTORS LICENSE *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG CONTRIBUTORS LICENSE *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.11-alt1.dev.git20141010.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1.dev.git20141010
- Initial build for Sisyphus

