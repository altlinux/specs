%define oname ParamUnittest

%def_with python3

Name: python-module-%oname
Version: 0.2
Release: alt1.git201210128
Summary: Simple extension to have parametrized unit tests
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/ParamUnittest
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/rik0/ParamUnittest.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides paramunittest
Provides: python-module-paramunittest = %EVR

%description
This package allows to create parametrized unit-tests that work with the
standard unittest package. A parametrized test case is automatically
converted to multiple test cases. Since they are TestCase subclasses,
they work with other test suites that recognize TestCases.

%if_with python3
%package -n python3-module-%oname
Summary: Simple extension to have parametrized unit tests
Group: Development/Python3
%py3_provides paramunittest
Provides: python3-module-paramunittest = %EVR

%description -n python3-module-%oname
This package allows to create parametrized unit-tests that work with the
standard unittest package. A parametrized test case is automatically
converted to multiple test cases. Since they are TestCase subclasses,
they work with other test suites that recognize TestCases.
%endif

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
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc *.rst examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git201210128
- Initial build for Sisyphus

