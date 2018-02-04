%define oname pytest-benchmark

%def_with python3

Name: python-module-%oname
Version: 3.1.1
Release: alt1.1
Summary: py.test fixture for benchmarking code
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/pytest-benchmark/

# https://github.com/ionelmc/pytest-benchmark.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-tests.patch

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-pytest-cov
BuildRequires: python-module-sphinx-devel
BuildRequires: python-module-sphinxcontrib-napoleon
BuildRequires: python-module-sphinx_py3doc_enhanced_theme
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv
BuildRequires: python2.7(cpuinfo) python2.7(pathlib) python2.7(statistics)
BuildRequires: python2.7(elasticsearch) python2.7(freezegun) python2.7(pygal) python2.7(aspectlib) python2.7(xdist)
BuildRequires: git-core
BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest-cov
BuildRequires: python3(cpuinfo)
BuildRequires: python3(elasticsearch) python3(freezegun) python3(pygal) python3(aspectlib) python3(xdist)
%endif

%py_provides pytest_benchmark
%py_requires pytest cpuinfo docutils

%description
A py.test fixture for benchmarking code.

%package -n python3-module-%oname
Summary: py.test fixture for benchmarking code
Group: Development/Python3
%py3_provides pytest_benchmark
%py3_requires pytest cpuinfo docutils

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
%patch1 -p1

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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i ${i}.py3
done
popd
%endif

%python_install

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
PATH=$PATH:%buildroot%_bindir py.test
%if_with python3
pushd ../python3
python3 setup.py test
rm -fR src build
export PYTHONPATH=%buildroot%python3_sitelibdir
PATH=$PATH:%buildroot%_bindir py.test3
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.1.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1.1-alt1
- Updated to upstream version 3.1.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt1.git20141219.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.0.0-alt1.git20141219.1
- NMU: Use buildreq for BR.

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.git20141219
- Initial build for Sisyphus

