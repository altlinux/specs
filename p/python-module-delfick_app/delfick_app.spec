%define oname delfick_app

%def_with python3

Name: python-module-%oname
Version: 0.6.7
Release: alt1.git20150713
Summary: Customized App mainline helper
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/delfick_app
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/delfick/delfick_app.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-delfick_error
BuildPreReq: python-module-rainbow_logging_handler
BuildPreReq: python-module-noseOfYeti python-module-nose
BuildPreReq: python-module-mock python-module-boto
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-sphinx_rtd_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-delfick_error
BuildPreReq: python3-module-rainbow_logging_handler
BuildPreReq: python3-module-noseOfYeti python3-module-nose
BuildPreReq: python3-module-mock python3-module-boto
%endif

%py_provides %oname
%py_requires delfick_error rainbow_logging_handler

%description
A framework to simplify and remove duplication when creating a new
application. It is opinionated in nature and aims to be declarative.

%if_with python3
%package -n python3-module-%oname
Summary: Customized App mainline helper
Group: Development/Python3
%py3_provides %oname
%py3_requires delfick_error rainbow_logging_handler

%description -n python3-module-%oname
A framework to simplify and remove duplication when creating a new
application. It is opinionated in nature and aims to be declarative.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
A framework to simplify and remove duplication when creating a new
application. It is opinionated in nature and aims to be declarative.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
A framework to simplify and remove duplication when creating a new
application. It is opinionated in nature and aims to be declarative.

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

pushd docs
export PYTHONPATH=%buildroot%python_sitelibdir
sphinx-build -b pickle -d _build/doctrees docs _build/pickle
sphinx-build -b html -d _build/doctrees docs _build/html
install -d %buildroot%python_sitelibdir/%oname
cp -fR _build/pickle %buildroot%python_sitelibdir/%oname/
popd

%check
python setup.py test -v
nosetests --with-noy -v
%if_with python3
pushd ../python3
python3 setup.py test -v
#nosetests3 --with-noy -v
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.7-alt1.git20150713
- Initial build for Sisyphus

