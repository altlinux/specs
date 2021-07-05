%define oname mpmath

Name: python3-module-%oname
Version: 1.2.1
Release: alt1

Summary: Python library for arbitrary-precision floating-point arithmetic

License: New BSD License
Group: Development/Python3
Url: http://mpmath.org/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools_scm

%{?!_disable_check:BuildRequires: xvfb-run}
BuildRequires: pytest3


%description
Mpmath is a pure-Python library for multiprecision floating-point
arithmetic. It provides an extensive set of transcendental functions,
unlimited exponent sizes, complex numbers, interval arithmetic,
numerical integration and differentiation, root-finding, linear algebra,
and much more. Almost any calculation can be performed just as well at
10-digit or 1000-digit precision, and in many cases mpmath implements
asymptotically fast algorithms that scale well for extremely high
precision work. Mpmath internally uses Python's builtin long integers by
default, but automatically switches to GMP/MPIR for much faster
high-precision arithmetic if gmpy is installed.

If matplotlib is available, mpmath also provides a convenient plotting
interface.

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune

%check
xvfb-run pytest3

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Mon Jul 05 2021 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version 1.2.1 (with rpmrb script)

* Mon Jul 05 2021 Vitaly Lipatov <lav@altlinux.ru> 0.19-alt1
- build new python3 module separately

* Fri Jun 02 2017 Michael Shigorin <mike@altlinux.org> 0.19-alt1.git20150621.1.1.1.1
- BOOTSTRAP: put xvfb-run under check knob

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.19-alt1.git20150621.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.19-alt1.git20150621.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.19-alt1.git20150621.1
- NMU: Use buildreq for BR.

* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.19-alt1.git20150621
- Version 0.19

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.18-alt1
- Version 0.18

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.17-alt2.1
- Rebuild with Python-3.3

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17-alt2
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.17-alt1.1
- Rebuild with Python-2.7

* Wed Apr 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17-alt1
- Initial build for Sisyphus

