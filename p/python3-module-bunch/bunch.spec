%define oname bunch

Name: python3-module-%oname
Version: 1.0.1
Release: alt4.git20120312
Summary: A dot-accessible dictionary (a la JavaScript objects)
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/bunch/

# https://github.com/dsc/bunch.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
%py3_provides %oname

%description
Bunch is a dictionary that supports attribute-style access, a la
JavaScript.

%package test
Summary: Test for %oname
Group: Development/Python3
Requires: %name = %EVR

%description test
Bunch is a dictionary that supports attribute-style access, a la
JavaScript.

This package contains test for %oname.

%prep
%setup
sed -i 's/rU/r/' setup.py

%build
%python3_build

%install
%python3_install

%files
%doc README*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test.py
%exclude %python3_sitelibdir/*/*/test.*

%files test
%python3_sitelibdir/*/test.py
%python3_sitelibdir/*/*/test.*

%changelog
* Tue Sep 12 2023 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt4.git20120312
- Fixed FTBFS.

* Sun Jul 25 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt3.git20120312
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0.1-alt2.git20120312.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt2.git20120312.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2.git20120312
- Added provides for Python 3 module

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20120312
- Initial build for Sisyphus

