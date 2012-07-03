%define modulename fpconst

Name: python-module-%modulename
Version: 0.7.2
Release: alt1.1

%setup_python_module %modulename

Summary: Utilities for handling IEEE 754 floating point special values
License: Apache Licence v. 2.0
Group: Development/Python
Url: http://pypi.python.org/pypi/fpconst
Packager: Egor Glukhov <kaman@altlinux.org>
BuildArch: noarch
BuildPreReq: python-module-setuptools
BuildRequires: python-devel
Source: %name-%version.tar

%description
This python module implements constants and functions for working with
IEEE754 double-precision special values.  It provides constants for
Not-a-Number (NaN), Positive Infinity (PosInf), and Negative Infinity
(NegInf), as well as functions to test for these values.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc README
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.2-alt1.1
- Rebuild with Python-2.7

* Sun Oct 24 2010 Egor Glukhov <kaman@altlinux.org> 0.7.2-alt1
- Initial build for Sisyphus
