%define oname monotonic

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt1.git20141129
Summary: An implementation of time.monotonic() for Python 2 & Python 3
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/monotonic/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/atdt/monotonic.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
This module provides a monotonic() function which returns the value (in
fractional seconds) of a clock which never goes backwards.

%package -n python3-module-%oname
Summary: An implementation of time.monotonic() for Python 2 & Python 3
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This module provides a monotonic() function which returns the value (in
fractional seconds) of a clock which never goes backwards.

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
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20141129
- Initial build for Sisyphus

