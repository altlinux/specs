%define oname gmpy

Name: python3-module-%oname
Version: 1.17
Release: alt2

Summary: General MultiPrecision arithmetic for Python
License: LGPL
Group: Development/Python3
Url: http://code.google.com/p/gmpy/

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: libgmp-devel


%description
A C-coded Python extension module that wraps the GMP library to provide
to Python code fast multiprecision arithmetic (integer, rational, and
float), random number generation, advanced number-theoretical functions,
and more.

%package docs
Summary: Documentation and tests for GMPY
Group: Development/Documentation
BuildArch: noarch

%description docs
A C-coded Python extension module that wraps the GMP library to provide
to Python code fast multiprecision arithmetic (integer, rational, and
float), random number generation, advanced number-theoretical functions,
and more.

This package contains documentation and tests for GMPY.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 test/gmpy_test.py
rm -f test/*.pyc

%files
%python3_sitelibdir/*

%files docs
%doc doc test


%changelog
* Wed Feb 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.17-alt2
- Build for python2 disabled.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.17-alt1.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.17-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.17-alt1.1
- NMU: Use buildreq for BR.

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.17-alt1
- Version 1.17

* Tue Mar 26 2013 Aleksey Avdeev <solo@altlinux.ru> 1.16-alt1.1
- Rebuild with Python-3.3

* Thu Feb 14 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.16-alt1
- Version 1.16

* Wed Aug 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.15-alt3
- Rebuilt with gmp 5.0.5

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.15-alt2
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.15-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Jan 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.15-alt1
- Version 1.15

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.14-alt1.1
- Rebuild with Python-2.7

* Wed Apr 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14-alt1
- Initial build for Sisyphus

