%define oname pytest-remove-stale-bytecode

%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt1.1
Summary: py.test plugin to remove stale byte code files
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-remove-stale-bytecode
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%description
This plugin removes all stale bytecode files before running tests. This
makes sure that removed python files are no longer visible for the test
runner as their bytecode file (*.pyc, *.pyo) is removed as well.

%package -n python3-module-%oname
Summary: py.test plugin to remove stale byte code files
Group: Development/Python3

%description -n python3-module-%oname
This plugin removes all stale bytecode files before running tests. This
makes sure that removed python files are no longer visible for the test
runner as their bytecode file (*.pyc, *.pyo) is removed as well.

%prep
%setup

%if_with python3
cp -fR . ../python3
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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

