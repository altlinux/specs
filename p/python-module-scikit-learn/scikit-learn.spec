%define oname scikit-learn

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.16
Release: alt1.git20150115
Summary: A set of python modules for machine learning and data mining
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/scikit-learn/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/scikit-learn/scikit-learn.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython python-module-coverage
BuildPreReq: python-module-nose python-module-scipy
BuildPreReq: libnumpy-devel python-module-Pillow liblapack-devel
BuildPreReq: gcc-c++ python-module-sphinx-devel python-module-numpydoc
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython python3-module-coverage
BuildPreReq: python3-module-nose python3-module-scipy
BuildPreReq: libnumpy-py3-devel
%endif

%py_provides sklearn

%description
scikit-learn is a Python module for machine learning built on top of
SciPy and distributed under the 3-Clause BSD license.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
scikit-learn is a Python module for machine learning built on top of
SciPy and distributed under the 3-Clause BSD license.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A set of python modules for machine learning and data mining
Group: Development/Python3
%py3_provides sklearn

%description -n python3-module-%oname
scikit-learn is a Python module for machine learning built on top of
SciPy and distributed under the 3-Clause BSD license.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
scikit-learn is a Python module for machine learning built on top of
SciPy and distributed under the 3-Clause BSD license.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
scikit-learn is a Python module for machine learning built on top of
SciPy and distributed under the 3-Clause BSD license.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
scikit-learn is a Python module for machine learning built on top of
SciPy and distributed under the 3-Clause BSD license.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
export BLAS=openblas
%add_optflags -fno-strict-aliasing -I%_includedir/numpy-py3
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

# build of docs is infinite; need help
#export PYTHONPATH=%buildroot%python_sitelibdir
#make -C doc pickle
#make -C doc html

%check
export PYTHONPATH=%buildroot%python_sitelibdir
py.test
%if_with python3
pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-%_python3_version
popd
%endif

%files
%doc *.md *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/test*
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/test*
%python_sitelibdir/*/*/*/test*

%files docs
%doc examples doc 

%if_with python3
%files -n python3-module-%oname
%doc *.md *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%endif

%changelog
* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.16-alt1.git20150115
- New snapshot

* Sat Nov 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.16-alt1.git20141113
- Initial build for Sisyphus

