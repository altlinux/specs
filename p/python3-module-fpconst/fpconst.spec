%define modulename fpconst

Name: python3-module-%modulename
Version: 0.7.2
Release: alt2.1

Summary: Utilities for handling IEEE 754 floating point special values
License: Apache Licence v. 2.0
Group: Development/Python3
Url: http://pypi.python.org/pypi/fpconst
BuildArch: noarch
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-module-setuptools
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python3 python3-base
BuildRequires: rpm-build-python3

#BuildRequires: python3-devel
Source: %name-%version.tar

%description
This python module implements constants and functions for working with
IEEE754 double-precision special values.  It provides constants for
Not-a-Number (NaN), Positive Infinity (PosInf), and Negative Infinity
(NegInf), as well as functions to test for these values.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README
%python3_sitelibdir/*

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 0.7.2-alt2
- NMU: Use buildreq for BR.

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1
- Initial build for Sisyphus

