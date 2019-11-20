%define oname tokenlib

Name: python3-module-%oname
Version: 0.3.1
Release: alt3

Summary: Generic support library for signed-token-based auth schemes
License: MPLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/tokenlib/
# https://github.com/mozilla-services/tokenlib.git
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname


%description
This is generic support library for doing token-based authentication.
You might use it to build a login system using bearer tokens, two-legged
oauth, or MAC Access authentication.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This is generic support library for doing token-based authentication.
You might use it to build a login system using bearer tokens, two-legged
oauth, or MAC Access authentication.

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
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Wed Nov 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.3.1-alt3
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.1-alt2.git20140108.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.1-alt2.git20140108.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 02 2016 Sergey Alembekov <rt@altlinux.ru> 0.3.1-alt2.git20140108
- cleanup buildreq

* Wed Oct 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20140108
- Initial build for Sisyphus

