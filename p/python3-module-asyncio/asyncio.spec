%define oname asyncio
Name: python3-module-%oname
Version: 3.4.3
Release: alt1.1
Summary: Reference implementation of PEP 3156
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/asyncio/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests /dev/pts
BuildPreReq: python3-module-nose python3-module-coverage python3-test

%py3_provides %oname
%add_python3_req_skip _winapi msvcrt

%description
Reference implementation of PEP 3156.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Reference implementation of PEP 3156.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test
%make check
#nosetests3 -v

%files
%doc README AUTHORS examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.4.3-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Apr 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.3-alt1
- Version 3.4.3

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.2-alt1
- Version 3.4.2

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1
- Initial build for Sisyphus

