%define oname radon

%def_with python3

Name: python-module-%oname
Version: 1.2.2
Release: alt1.git20150730
Summary: Code Metrics in Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/radon
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/rubik/radon.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-mando python-module-colorama
BuildPreReq: python-module-tox python-module-paramunittest
BuildPreReq: python-module-coverage python-module-coveralls
BuildPreReq: python-module-nose python-module-mock
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-mando python3-module-colorama
BuildPreReq: python3-module-tox python3-module-paramunittest
BuildPreReq: python3-module-coverage python3-module-coveralls
BuildPreReq: python3-module-nose python3-module-mock
%endif

%py_provides %oname
%py_requires mando colorama

%description
Radon is a Python tool that computes various metrics from the source
code. Radon can compute:
* McCabe's complexity, i.e. cyclomatic complexity
* raw metrics (these include SLOC, comment lines, blank lines, &c.)
* Halstead metrics (all of them)
* Maintainability Index (the one used in Visual Studio)

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Radon is a Python tool that computes various metrics from the source
code. Radon can compute:
* McCabe's complexity, i.e. cyclomatic complexity
* raw metrics (these include SLOC, comment lines, blank lines, &c.)
* Halstead metrics (all of them)
* Maintainability Index (the one used in Visual Studio)

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Code Metrics in Python
Group: Development/Python3
%py3_provides %oname
%py3_requires mando colorama

%description -n python3-module-%oname
Radon is a Python tool that computes various metrics from the source
code. Radon can compute:
* McCabe's complexity, i.e. cyclomatic complexity
* raw metrics (these include SLOC, comment lines, blank lines, &c.)
* Halstead metrics (all of them)
* Maintainability Index (the one used in Visual Studio)

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Radon is a Python tool that computes various metrics from the source
code. Radon can compute:
* McCabe's complexity, i.e. cyclomatic complexity
* raw metrics (these include SLOC, comment lines, blank lines, &c.)
* Halstead metrics (all of them)
* Maintainability Index (the one used in Visual Studio)

This package contains tests for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Radon is a Python tool that computes various metrics from the source
code. Radon can compute:
* McCabe's complexity, i.e. cyclomatic complexity
* raw metrics (these include SLOC, comment lines, blank lines, &c.)
* Halstead metrics (all of them)
* Maintainability Index (the one used in Visual Studio)

This package contains pickles for %oname.

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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test -v
export PYTHONPATH=%buildroot%python_sitelibdir
python radon/tests/run.py -v
%if_with python3
pushd ../python3
python3 setup.py test -v
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 radon/tests/run.py -v
popd
%endif

%files
%doc CHANGELOG *.rst docs/_build/html
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG *.rst docs/_build/html
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.git20150730
- Initial build for Sisyphus

