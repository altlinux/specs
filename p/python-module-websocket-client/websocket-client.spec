%define oname websocket-client

%def_disable check

Name: python-module-%oname
Version: 0.56.0
Release: alt1
Summary: WebSocket client for python. hybi13 is supported
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/websocket-client/

# https://github.com/liris/websocket-client.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-backports.ssl_match_hostname
BuildRequires: python-module-six

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-six

%py_provides websocket
%py_requires backports.ssl_match_hostname

%description
websocket-client module is WebSocket client for python. This provide the
low level APIs for WebSocket. All APIs are the synchronous functions.

websocket-client supports only hybi-13.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
websocket-client module is WebSocket client for python. This provide the
low level APIs for WebSocket. All APIs are the synchronous functions.

websocket-client supports only hybi-13.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: WebSocket client for python. hybi13 is supported
Group: Development/Python3
%py3_provides websocket

%description -n python3-module-%oname
websocket-client module is WebSocket client for python. This provide the
low level APIs for WebSocket. All APIs are the synchronous functions.

websocket-client supports only hybi-13.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
websocket-client module is WebSocket client for python. This provide the
low level APIs for WebSocket. All APIs are the synchronous functions.

websocket-client supports only hybi-13.

This package contains tests for %oname.

%prep
%setup

cp -fR . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i ${i}.py2
done
popd

pushd ../python3
%python3_install
popd

%check
python setup.py test

pushd ../python3
python3 setup.py test
popd

%files
%doc ChangeLog *.rst
%_bindir/*.py2
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%oname
%doc ChangeLog *.rst
%_bindir/*
%exclude %_bindir/*.py2
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%changelog
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

