%define oname pytest-benchmark

%def_with python3

Name: python-module-%oname
Version: 2.0.0
Release: alt1.git20141219
Summary: py.test fixture for benchmarking code
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-benchmark/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ionelmc/pytest-benchmark.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pytest-cov
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-sphinxcontrib-napoleon
BuildPreReq: python-module-sphinx_py3doc_enhanced_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pytest-cov
BuildPreReq: python-tools-2to3
%endif

%py_provides pytest_benchmark
%py_requires pytest

%description
A py.test fixture for benchmarking code.

%package -n python3-module-%oname
Summary: py.test fixture for benchmarking code
Group: Development/Python3
%py3_provides pytest_benchmark
%py3_requires pytest

%description -n python3-module-%oname
A py.test fixture for benchmarking code.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
A py.test fixture for benchmarking code.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
A py.test fixture for benchmarking code.

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

export PYTHONPATH=%buildroot%python_sitelibdir
pushd docs
sphinx-build -b pickle -d _build/doctrees . _build/pickle
sphinx-build -b html -d _build/doctrees . _build/html
popd

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
rm -fR src build
export PYTHONPATH=%buildroot%python_sitelibdir
py.test
%if_with python3
pushd ../python3
python3 setup.py test
rm -fR src build
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-%_python3_version
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
* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.git20141219
- Initial build for Sisyphus

