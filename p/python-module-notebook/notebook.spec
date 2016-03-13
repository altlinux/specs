%define oname notebook

%def_with python3
#def_disable check
%def_with docs

Name: python-module-%oname
Version: 4.0.4
Release: alt2.1
Summary: Jupyter Interactive Notebook
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/notebook/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests pandoc
BuildPreReq: python-module-zmq python-module-jinja2
BuildPreReq: python-module-tornado python-module-ipython_genutils-tests
BuildPreReq: python-module-traitlets-tests python-module-jupyter_core
BuildPreReq: python-module-jupyter_client python-module-nbformat
BuildPreReq: python-module-nbconvert python-module-ipykernel
BuildPreReq: python-module-mock python-module-terminado
BuildPreReq: python-module-nose python-module-requests
BuildPreReq: python-module-coverage
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests pandoc
BuildPreReq: python3-module-zmq python3-module-jinja2
BuildPreReq: python3-module-tornado python3-module-ipython_genutils-tests
BuildPreReq: python3-module-traitlets-tests python3-module-jupyter_core
BuildPreReq: python3-module-jupyter_client python3-module-nbformat
BuildPreReq: python3-module-nbconvert python3-module-ipykernel
BuildPreReq: python3-module-mock python3-module-terminado
BuildPreReq: python3-module-nose python3-module-requests
BuildPreReq: python3-module-coverage
BuildPreReq: python3-module-sphinx-devel
%endif

%py_provides %oname
%py_requires zmq jinja2 tornado ipython_genutils traitlets jupyter_core
%py_requires jupyter_client nbformat nbconvert ipykernel

%description
The Jupyter HTML notebook is a web-based notebook environment for
interactive computing.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The Jupyter HTML notebook is a web-based notebook environment for
interactive computing.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Jupyter Interactive Notebook
Group: Development/Python3
%py3_provides %oname
%py3_requires zmq jinja2 tornado ipython_genutils traitlets jupyter_core
%py3_requires jupyter_client nbformat nbconvert ipykernel

%description -n python3-module-%oname
The Jupyter HTML notebook is a web-based notebook environment for
interactive computing.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
The Jupyter HTML notebook is a web-based notebook environment for
interactive computing.

This package contains tests for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
The Jupyter HTML notebook is a web-based notebook environment for
interactive computing.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
The Jupyter HTML notebook is a web-based notebook environment for
interactive computing.

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

%if_with docs
export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%check
export LC_ALL=en_US.UTF-8
nosetests -vv --with-coverage --cover-package=%oname %oname
#if_with python3
%if 0
pushd ../python3
nosetests3 -vv --with-coverage --cover-package=%oname %oname
popd
%endif

%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests
%python3_sitelibdir/*/*/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt2
- Enabled check
- Added documentation

* Sat Aug 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1
- Initial build for Sisyphus

