%define oname cobs

Name: python3-module-%oname
Version: 1.0.0
Release: alt2

Summary: Consistent Overhead Byte Stuffing (COBS)
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/cobs/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-modules-unittest

%py3_provides %oname


%description
The cobs package is provided, which contains modules containing
functions for encoding and decoding according to COBS methods.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
The cobs package is provided, which contains modules containing
functions for encoding and decoding according to COBS methods.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py build_ext -i
pushd python3
%__python3 -m cobs.cobs.test -v
%__python3 -m cobs.cobsr.test -v
popd

%files
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/test.*
%exclude %python3_sitelibdir/*/*/*/test.*

%files tests
%python3_sitelibdir/*/*/test.*
%python3_sitelibdir/*/*/*/test.*


%changelog
* Thu Feb 06 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.0-alt2
- Build for python2 disabled.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt1.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

