%define _unpackaged_files_terminate_build 1
%define oname jdcal

Name: python3-module-%oname
Version: 1.3
Release: alt1.2
Summary: Julian dates from proleptic Gregorian and Julian calendars
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/jdcal/

# https://github.com/phn/jdcal.git
Source0: https://pypi.python.org/packages/9b/fa/40beb2aa43a13f740dd5be367a10a03270043787833409c61b79e69f1dfd/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname

%description
This module contains functions for converting between Julian dates and
calendar dates.

%prep
%setup -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 1.3-alt1.2
- Drop python2 support.

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

