%define oname cobs

%def_with check

Name: python3-module-%oname
Version: 1.2.1
Release: alt1

Summary: Consistent Overhead Byte Stuffing (COBS)

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/cobs
VCS: https://github.com/cmcqueen/cobs-python

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

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
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 -m cobs.cobs.test
python3 -m cobs.cobsr.test

%files
%doc *.txt *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/*/*/test.*
%exclude %python3_sitelibdir/*/*/*/test.*

%files tests
%python3_sitelibdir/*/*/test.*
%python3_sitelibdir/*/*/*/test.*

%changelog
* Fri May 24 2024 Grigory Ustinov <grenka@altlinux.org> 1.2.1-alt1
- Build new version.

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

