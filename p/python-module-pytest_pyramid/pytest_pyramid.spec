%define oname pytest_pyramid

%def_with python3

Name: python-module-%oname
Version: 0.1.1
Release: alt1.git20140516
Summary: Basic fixtures for testing pyramid applications with pytest test suite
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest_pyramid/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/fizyk/pytest_pyramid.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid-tests python-module-pytest
BuildPreReq: python-module-webtest python-module-pytest-cov
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid-tests python3-module-pytest
BuildPreReq: python3-module-webtest python3-module-pytest-cov
%endif

%py_provides %oname
%py_requires pyramid.testing

%description
pytest_pyramid provides basic fixtures for testing pyramid applications
with pytest test suite.

By default, pytest_pyramid will create two fixtures: pyramid_config,
which creates configurator based on config.ini file, and pyramid_app,
which creates TestApp based on Configurator returned by pyramid_config.

%package -n python3-module-%oname
Summary: Basic fixtures for testing pyramid applications with pytest test suite
Group: Development/Python3
%py3_provides %oname
%py3_requires pyramid.testing

%description -n python3-module-%oname
pytest_pyramid provides basic fixtures for testing pyramid applications
with pytest test suite.

By default, pytest_pyramid will create two fixtures: pyramid_config,
which creates configurator based on config.ini file, and pyramid_app,
which creates TestApp based on Configurator returned by pyramid_config.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
pytest_pyramid provides basic fixtures for testing pyramid applications
with pytest test suite.

By default, pytest_pyramid will create two fixtures: pyramid_config,
which creates configurator based on config.ini file, and pyramid_app,
which creates TestApp based on Configurator returned by pyramid_config.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
pytest_pyramid provides basic fixtures for testing pyramid applications
with pytest test suite.

By default, pytest_pyramid will create two fixtures: pyramid_config,
which creates configurator based on config.ini file, and pyramid_app,
which creates TestApp based on Configurator returned by pyramid_config.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

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

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

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
%exclude %python_sitelibdir/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests
%endif

%changelog
* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20140516
- Initial build for Sisyphus

