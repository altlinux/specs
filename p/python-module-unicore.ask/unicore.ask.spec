%define mname unicore
%define oname %mname.ask

%def_with python3

Name: python-module-%oname
Version: 0.1.0
Release: alt1.git20150319
Summary: Universal Core REST service for Questions and Surveys
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/unicore.ask/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/universalcore/unicore.ask.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid-tests python-module-pyramid_beaker
BuildPreReq: python-module-raven python-module-colander
BuildPreReq: python-module-cornice python-module-webtest
BuildPreReq: python-module-SQLAlchemy python-module-SQLAlchemy-Utils
BuildPreReq: python-module-alembic python-module-psycopg2
BuildPreReq: python-module-pytest-cov python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid-tests python3-module-pyramid_beaker
BuildPreReq: python3-module-raven python3-module-colander
BuildPreReq: python3-module-cornice python3-module-webtest
BuildPreReq: python3-module-SQLAlchemy python3-module-SQLAlchemy-Utils
BuildPreReq: python3-module-alembic python3-module-psycopg2
BuildPreReq: python3-module-pytest-cov python3-module-mock
%endif

%py_provides %oname
%py_requires %mname pyramid pyramid_beaker raven colander cornice
%py_requires sqlalchemy sqlalchemy_utils alembic psycopg2

%description
Universal Core REST service for Questions and Surveys.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires pyramid.config.testing

%description tests
Universal Core REST service for Questions and Surveys.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Universal Core REST service for Questions and Surveys
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname pyramid pyramid_beaker raven colander cornice
%py3_requires sqlalchemy sqlalchemy_utils alembic psycopg2

%description -n python3-module-%oname
Universal Core REST service for Questions and Surveys.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires pyramid.config.testing

%description -n python3-module-%oname-tests
Universal Core REST service for Questions and Surveys.

This package contains tests for %oname.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
#py.test --verbose --cov ./unicore/ask unicore/ask
%if_with python3
pushd ../python3
python3 setup.py test
#py.test-%_python3_version --verbose --cov ./unicore/ask unicore/ask
popd
%endif

%files
%doc *.rst
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/*/tests

%files tests
%python_sitelibdir/%mname/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%mname/*/*/tests
%endif

%changelog
* Sat Mar 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20150319
- Initial build for Sisyphus

