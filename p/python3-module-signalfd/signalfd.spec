%define oname signalfd

Name: python3-module-%oname
Version: 0.1
Release: alt2
Summary: Python bindings for sigprocmask(2) and signalfd(2)
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/python-signalfd/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest

%py3_provides %oname

%description
Python bindings for sigprocmask(2) and signalfd(2).

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Python bindings for sigprocmask(2) and signalfd(2).

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
rm build -fR
python3 setup.py build_ext -i
py.test3 -vv

%files
%doc PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files tests
%python3_sitelibdir/*/test

%changelog
* Mon May 24 2021 Grigory Ustinov <grenka@altlinux.org> 0.1-alt2
- Drop python2 support.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1-alt1.3.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1-alt1.3
- Fixed build.

* Mon Mar 28 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.2.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Mar 28 2016 Denis Medvedev <nbr@altlinux.org> 0.1-alt1.2
- Fix test for python3.5

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.1
- NMU: Use buildreq for BR.

* Fri Jan 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

