%def_disable check

%define oname ZEO

%def_with python3
#def_disable check

Name: python-module-%oname
Version: 4.2.0
Release: alt3.dev0.git20150605.1.1.1
Summary: ZEO provides a client-server storage implementation for ZODB
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/ZEO
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/ZEO.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-manuel
BuildPreReq: python-module-transaction
BuildPreReq: python-module-persistent
BuildPreReq: python-module-zc.lockfile
BuildPreReq: python-module-zconfig
BuildPreReq: python-module-zdaemon
BuildPreReq: python-module-zope.interface
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-zope.testing
BuildPreReq: python3-module-manuel
BuildPreReq: python3-module-transaction
BuildPreReq: python3-module-persistent
BuildPreReq: python3-module-zc.lockfile
BuildPreReq: python3-module-zconfig
BuildPreReq: python3-module-zdaemon
BuildPreReq: python3-module-zope.interface
%endif

%py_requires ZODB persistent zc.lockfile ZConfig zdaemon zope.interface

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
%py_requires zope.testing ZODB.tests

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
%py3_requires ZODB persistent zc.lockfile ZConfig zdaemon zope.interface
%add_python3_req_skip ZODB.Transaction

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
%py3_requires zope.testing ZODB.tests

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
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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

%check
python setup.py test
#if_with python3
%if 0
pushd ../python3
python3 setup.py test
popd
%endif

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
* Mon Feb 05 2018 Stanislav Levin <slev@altlinux.org> 4.2.0-alt3.dev0.git20150605.1.1.1
- (NMU) Fix Requires to ZODB.Transaction

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.2.0-alt3.dev0.git20150605.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.2.0-alt3.dev0.git20150605.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 05 2016 Sergey Alembekov <rt@altlinux.ru> 4.2.0-alt3.dev0.git20150605
- Disabled tests and unnecessary buildreq

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.0-alt2.dev0.git20150605
- Enabled check

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.0-alt1.dev0.git20150605
- Version 4.2.0.dev0

* Tue Jan 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1.git20150106
- Version 4.1.0

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1.dev0.git20141216
- Version 4.1.0.dev0

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.git20140813
- Snapshot from git
- Enabled testing

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Initial build for Sisyphus

