%define oname websocket-client

%def_disable check

Name: python3-module-%oname
Version: 0.56.0
Release: alt2
Summary: WebSocket client for python. hybi13 is supported
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/websocket-client/

# https://github.com/liris/websocket-client.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-six

%py3_provides websocket

%description
websocket-client module is WebSocket client for python. This provide the
low level APIs for WebSocket. All APIs are the synchronous functions.

websocket-client supports only hybi-13.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
websocket-client module is WebSocket client for python. This provide the
low level APIs for WebSocket. All APIs are the synchronous functions.

websocket-client supports only hybi-13.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
python3 setup.py test

%files
%doc ChangeLog *.rst
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 0.56.0-alt2
- Drop python2 support.

* Wed Dec 18 2019 Vladimir Didenko <cow@altlinux.org> 0.56.0-alt1
- 0.56.0

* Mon Jan 14 2019 Alexey Shabalin <shaba@altlinux.org> 0.54.0-alt1
- 0.54.0

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.32.0-alt1.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.32.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.32.0-alt1.1
- NMU: Use buildreq for BR.

* Mon Sep 14 2015 Vladimir Didenko <cow@altlinux.org> 0.32.0-alt1
- new version

* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.0-alt1.git20141211
- Initial build for Sisyphus

