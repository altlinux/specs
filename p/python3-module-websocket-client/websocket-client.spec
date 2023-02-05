%define oname websocket-client

%def_with check

Name: python3-module-%oname
Version: 1.5.1
Release: alt1

Summary: WebSocket client for Python with low level API options

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/websocket-client

# https://github.com/liris/websocket-client.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
%endif

%py3_provides websocket

BuildArch: noarch

%description
websocket-client is a WebSocket client for Python.  It provides access to low
level APIs for WebSockets.  websocket-client implements version hybi-13 of the
WebSocket protocol. This client does not currently support the
permessage-deflate extension from RFC 7692.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
websocket-client is a WebSocket client for Python.  It provides access to low
level APIs for WebSockets.  websocket-client implements version hybi-13 of the
WebSocket protocol. This client does not currently support the
permessage-deflate extension from RFC 7692.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 -v websocket/tests

%files
%doc ChangeLog *.md
%_bindir/wsdump
%python3_sitelibdir/websocket
%python3_sitelibdir/websocket_client-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Sun Feb 05 2023 Grigory Ustinov <grenka@altlinux.org> 1.5.1-alt1
- Automatically updated to 1.5.1.

* Fri Jan 27 2023 Grigory Ustinov <grenka@altlinux.org> 1.5.0-alt1
- Automatically updated to 1.5.0.

* Fri Nov 04 2022 Grigory Ustinov <grenka@altlinux.org> 1.4.2-alt1
- Automatically updated to 1.4.2.

* Mon Sep 12 2022 Grigory Ustinov <grenka@altlinux.org> 1.4.1-alt1
- Automatically updated to 1.4.1.

* Fri Jul 15 2022 Grigory Ustinov <grenka@altlinux.org> 1.3.3-alt1
- Automatically updated to 1.3.3.

* Fri Jun 10 2022 Grigory Ustinov <grenka@altlinux.org> 1.3.2-alt1
- Automatically updated to 1.3.2.

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

