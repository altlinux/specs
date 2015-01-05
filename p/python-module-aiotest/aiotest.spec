%define oname aiotest

%def_with python3

Name: python-module-%oname
Version: 0.2
Release: alt1
Summary: Test suite to validate an implementation of the asyncio API, the PEP 3156
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/aiotest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-trollius
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-asyncio
%endif

%py_provides %oname
%py_requires trollius

%description
aiotest is a test suite to validate an implementation of the asyncio
API, the PEP 3156.

%package -n python3-module-%oname
Summary: Test suite to validate an implementation of the asyncio API, the PEP 3156
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio

%description -n python3-module-%oname
aiotest is a test suite to validate an implementation of the asyncio
API, the PEP 3156.

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
./test_trollius.py
%if_with python3
pushd ../python3
python3 setup.py test
./test_asyncio.py
popd
%endif

%files
%doc README
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README
%python3_sitelibdir/*
%endif

%changelog
* Mon Jan 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

