%define oname testscenarios

%def_with python3

Name: python-module-%oname
Version: 0.4
Release: alt1
Summary: Testscenarios, a pyunit extension for dependency injection
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/testscenarios/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
testscenarios provides clean dependency injection for python unittest
style tests. This can be used for interface testing (testing many
implementations via a single test suite) or for classic dependency
injection (provide tests with dependencies externally to the test code
itself, allowing easy testing in different situations).

%package -n python3-module-%oname
Summary: Testscenarios, a pyunit extension for dependency injection
Group: Development/Python3

%description -n python3-module-%oname
testscenarios provides clean dependency injection for python unittest
style tests. This can be used for interface testing (testing many
implementations via a single test suite) or for classic dependency
injection (provide tests with dependencies externally to the test code
itself, allowing easy testing in different situations).

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

%files
%doc Apache-2.0 BSD COPYING GOALS HACKING NEWS README doc
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc Apache-2.0 BSD COPYING GOALS HACKING NEWS README doc
%python3_sitelibdir/*
%endif

%changelog
* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Initial build for Sisyphus

