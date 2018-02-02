%define _unpackaged_files_terminate_build 1
%define oname monotonic

%def_with python3

Name: python-module-%oname
Version: 1.2
Release: alt1.1
Summary: An implementation of time.monotonic() for Python 2 & Python 3
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/monotonic/

# https://github.com/atdt/monotonic.git
Source0: https://pypi.python.org/packages/08/35/9e06c881c41962d7367e9466724beda2b1101439b149b7ff708d708890de/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
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
%setup -q -n %{oname}-%{version}

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
%doc LICENSE PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1
- automated PyPI update

* Fri Apr 08 2016 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt1
- 1.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 0.4-alt1
- 0.4

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20141129
- Initial build for Sisyphus

