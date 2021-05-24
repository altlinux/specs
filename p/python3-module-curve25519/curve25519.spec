%define _unpackaged_files_terminate_build 1
%define oname curve25519

Name: python3-module-%oname
Version: 1.3
Release: alt3
Summary: Implementations of a fast Elliptic-curve Diffie-Hellman primitive
License: BSD
Group: Development/Python3
Url: https://code.google.com/p/curve25519-donna/

# https://github.com/agl/curve25519-donna.git
Source: %{oname}-donna-%{version}.tar

BuildRequires(pre): rpm-build-python3
BuildRequires:python3-module-pytest

%py3_provides %oname

%description
curve25519 is an elliptic curve, developed by Dan Bernstein, for fast
Diffie-Hellman key agreement. DJB's original implementation was written
in a language of his own devising called qhasm. The original qhasm
source isn't available, only the x86 32-bit assembly output.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
curve25519 is an elliptic curve, developed by Dan Bernstein, for fast
Diffie-Hellman key agreement. DJB's original implementation was written
in a language of his own devising called qhasm. The original qhasm
source isn't available, only the x86 32-bit assembly output.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-donna-%{version}

sed -i 's|@VERSION@|%version|' setup.py
%ifarch x86_64
sed -i 's|m32|m64|g' Makefile
%endif

%build
%python3_build_debug

%install
%python3_install

%check
rm build -fR
python3 setup.py build_ext -i
py.test3 -vv

%files
%doc README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files tests
%python3_sitelibdir/*/test

%changelog
* Mon May 24 2021 Grigory Ustinov <grenka@altlinux.org> 1.3-alt3
- Drop python2 support.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3-alt2.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Mar 05 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3-alt2
- Cleaned up spec and fixed tests.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.1-alt1.git20141020.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.1-alt1.git20141020.1
- NMU: Use buildreq for BR.

* Sun Jan 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.git20141020
- Initial build for Sisyphus

