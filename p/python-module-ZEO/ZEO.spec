%define oname ZEO

%def_with python3

Name: python-module-%oname
Version: 4.0.0
Release: alt1
Summary: ZEO provides a client-server storage implementation for ZODB
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/ZEO
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
ZEO is a client-server system for sharing a single storage among many
clients. When you use ZEO, the storage is opened in the ZEO server
process. Client programs connect to this process using a ZEO
ClientStorage. ZEO provides a consistent view of the database to all
clients. The ZEO client and server communicate using a custom RPC
protocol layered on top of TCP.

%package tests
Summary: Tests for ZEO
Group: Development/Python
Requires: %name = %EVR

%description tests
ZEO is a client-server system for sharing a single storage among many
clients. When you use ZEO, the storage is opened in the ZEO server
process. Client programs connect to this process using a ZEO
ClientStorage. ZEO provides a consistent view of the database to all
clients. The ZEO client and server communicate using a custom RPC
protocol layered on top of TCP.

This package contains tests for ZEO.

%package -n python3-module-%oname
Summary: ZEO provides a client-server storage implementation for ZODB
Group: Development/Python3

%description -n python3-module-%oname
ZEO is a client-server system for sharing a single storage among many
clients. When you use ZEO, the storage is opened in the ZEO server
process. Client programs connect to this process using a ZEO
ClientStorage. ZEO provides a consistent view of the database to all
clients. The ZEO client and server communicate using a custom RPC
protocol layered on top of TCP.

%package -n python3-module-%oname-tests
Summary: Tests for ZEO
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
ZEO is a client-server system for sharing a single storage among many
clients. When you use ZEO, the storage is opened in the ZEO server
process. Client programs connect to this process using a ZEO
ClientStorage. ZEO provides a consistent view of the database to all
clients. The ZEO client and server communicate using a custom RPC
protocol layered on top of TCP.

This package contains tests for ZEO.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
mv $i $i.py3
done
popd
%endif

%python_install

%files
%doc *.txt
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests.py*

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests.py*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests.py*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests.py*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Initial build for Sisyphus

