%define oname monotonic

%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt1
Summary: An implementation of time.monotonic() for Python 2 & Python 3
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/monotonic/

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
%python_build

%if_with python3
pushd ../python3
%python3_build
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
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Apr 08 2016 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt1
- 1.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 0.4-alt1
- 0.4

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20141129
- Initial build for Sisyphus

