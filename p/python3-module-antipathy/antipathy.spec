%define oname antipathy

%def_disable check

Name: python3-module-%oname
Version: 0.81.04
Release: alt2

Summary: oo view of file paths and names, subclassed from bytes/str/unicode
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/antipathy/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname


%description
oo view of file paths and names, subclassed from bytes/str/unicode.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
oo view of file paths and names, subclassed from bytes/str/unicode.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc CHANGES README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test.*
%exclude %python3_sitelibdir/*/*/test.*

%files tests
%python3_sitelibdir/*/test.*
%python3_sitelibdir/*/*/test.*


%changelog
* Tue Nov 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.81.04-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.81.04-alt1.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.81.04-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.81.04-alt1.1
- NMU: Use buildreq for BR.

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.81.04-alt1
- Version 0.81.04

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.81.03-alt1
- Initial build for Sisyphus

