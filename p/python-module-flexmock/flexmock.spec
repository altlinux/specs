%define oname flexmock

%def_with python3

Name: python-module-%oname
Version: 0.9.7
Release: alt1.git20140924
Summary: Mock/Stub/Spy library for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/flexmock/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/has207/flexmock.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose python-module-twisted-core-test
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose python3-module-twisted-core-test
%endif

%py_provides %oname

%description
flexmock is a testing library for Python that makes it easy to create
mocks, stubs and fakes.

%package -n python3-module-%oname
Summary: Mock/Stub/Spy library for Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
flexmock is a testing library for Python that makes it easy to create
mocks, stubs and fakes.

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
tests/run_tests.sh
%if_with python3
pushd ../python3
tests/run_tests.sh
popd
%endif

%files
%doc CHANGELOG *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG *.md
%python3_sitelibdir/*
%endif

%changelog
* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt1.git20140924
- Initial build for Sisyphus

