%define oname pytest-benchmark

%def_with python3

Name: python-module-%oname
Version: 2.0.0
Release: alt1.git20141219.1
Summary: py.test fixture for benchmarking code
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-benchmark/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ionelmc/pytest-benchmark.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-pytest-cov
#BuildPreReq: python-module-sphinx-devel
#BuildPreReq: python-module-sphinxcontrib-napoleon
#BuildPreReq: python-module-sphinx_py3doc_enhanced_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-pytest-cov
#BuildPreReq: python-tools-2to3
%endif

%py_provides pytest_benchmark
%py_requires pytest

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: bzr python-base python-devel python-module-Paver python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-coverage python-module-cryptography python-module-cssselect python-module-enum34 python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-mimeparse python-module-pbr python-module-pluggy python-module-py python-module-pyasn1 python-module-pytest python-module-pytz python-module-serial python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-sphinxcontrib python-module-twisted-core python-module-unittest2 python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python-tools-2to3 python3 python3-base python3-module-coverage python3-module-pluggy python3-module-py python3-module-pytest python3-module-setuptools xz
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-pytest-cov python-module-setuptools-tests python-module-sphinx_py3doc_enhanced_theme python-module-sphinxcontrib-napoleon python3-module-pytest-cov python3-module-setuptools-tests rpm-build-python3 time

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
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.0.0-alt1.git20141219.1
- NMU: Use buildreq for BR.

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.git20141219
- Initial build for Sisyphus

