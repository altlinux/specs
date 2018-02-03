%define _unpackaged_files_terminate_build 1
%define oname jdcal

%def_with python3

Name: python-module-%oname
Version: 1.3
Release: alt1.1
Summary: Julian dates from proleptic Gregorian and Julian calendars
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/jdcal/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/phn/jdcal.git
Source0: https://pypi.python.org/packages/9b/fa/40beb2aa43a13f740dd5be367a10a03270043787833409c61b79e69f1dfd/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
This module contains functions for converting between Julian dates and
calendar dates.

%package -n python3-module-%oname
Summary: Julian dates from proleptic Gregorian and Julian calendars
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This module contains functions for converting between Julian dates and
calendar dates.

%prep
%setup -q -n %{oname}-%{version}

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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt2.git20111008.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Feb 08 2016 Sergey Alembekov <rt@altlinux.ru> 1.0-alt2.git20111008
- Disabled unnecessary dependents

* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20111008
- Initial build for Sisyphus

