%define _unpackaged_files_terminate_build 1
%define oname gmpy2

%def_without check

Name: python3-module-%oname
Version: 2.2.0
Release: alt0.a2

Summary: GMP/MPIR, MPFR, and MPC interface

License: LGPL-3.0+
Group: Development/Python3
Url: https://github.com/aleaxit/gmpy

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: libmpc-devel

%description
A C-coded Python extension module that wraps the GMP library to provide
to Python code fast multiprecision arithmetic (integer, rational, and
float), random number generation, advanced number-theoretical functions,
and more.

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%python3_build_debug

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 test/gmpy_test.py
python3 test/runtests.py

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Wed Dec 20 2023 Grigory Ustinov <grenka@altlinux.org> 2.2.0-alt0.a2
- Build new version for python3.12.

* Sat Oct 14 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 2.1.5-alt2
- NMU: fixed FTBFS with MPFR 4.2.1

* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 2.1.5-alt1
- new version 2.1.5 (with rpmrb script)

* Sat Aug 27 2022 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt1
- new version 2.1.2 (with rpmrb script)

* Thu Dec 16 2021 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt1
- new version 2.1.1 (with rpmrb script)

* Sun Jul 04 2021 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- build python3 module only

* Mon Jun 21 2021 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt0.1.b5
- New version from https://github.com/aleaxit/gmpy/tree/gmpy2-2.1.0b5.
- Set LGPL version in License tag.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.8-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.8-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.5-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.0.5-alt1.1
- NMU: Use buildreq for BR.

* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.5-alt1
- Version 2.0.5

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt1
- Version 2.0.3

* Thu Sep 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1
- Version 2.0.2

* Tue Mar 26 2013 Aleksey Avdeev <solo@altlinux.ru> 2.0.0-alt2.b1.1
- Rebuild with Python-3.3

* Wed Aug 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.b1
- Rebuilt with gmp 5.0.5

* Sat Jun 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.b1
- Version 2.0.0b1

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

