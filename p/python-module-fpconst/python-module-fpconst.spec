Name: python-module-fpconst
Version: 0.7.3
Release: alt1

Summary: Utilities for handling IEEE 754 floating point special values
License: Apache-2.0
Group: Development/Python
Url: http://pypi.python.org/pypi/fpconst
Packager: Egor Glukhov <kaman@altlinux.org>
BuildArch: noarch
BuildPreReq: python-module-setuptools
BuildRequires: python-devel

Source: fpconst-%version.tgz

%description
This python module implements constants and functions for working with
IEEE754 double-precision special values.  It provides constants for
Not-a-Number (NaN), Positive Infinity (PosInf), and Negative Infinity
(NegInf), as well as functions to test for these values.

%prep
%setup -n fpconst-%version

%build
%python_build

%install
%python_install

%files
%doc README CHANGELOG COPYING pep-0754.txt
%python_sitelibdir/*

%changelog
* Thu Mar 22 2018 Andrey Bychkov <mrdrew@altlinux.ru> 0.7.3-alt1
- Version 0.7.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.2-alt1.1
- Rebuild with Python-2.7

* Sun Oct 24 2010 Egor Glukhov <kaman@altlinux.org> 0.7.2-alt1
- Initial build for Sisyphus
