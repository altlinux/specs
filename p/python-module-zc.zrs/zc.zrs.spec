%define oname zc.zrs

%def_without python3
%def_disable check

Name: python-module-%oname
Version: 2.5.3
Release: alt2.git20150216
Summary: ZODB Replicated Storage
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/zc.zrs/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zc/zrs.git
Source: %name-%version.tar
BuildRequires: python-module-pbr python-module-pytest python-module-unittest2 python-module-zc.zkzeo

#BuildPreReq: python-module-setuptools-tests python-module-mock
#BuildPreReq: python-module-zope.testing python-module-zodbpickle
#BuildPreReq: python-module-zc.zk-tests python-modules-json
#BuildPreReq: python-module-ZODB3
#BuildPreReq: python-module-twisted-core
#BuildPreReq: python-module-ZEO-tests
#BuildPreReq: python-module-zc.zkzeo
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-module-setuptools-tests python3-module-mock
#BuildPreReq: python3-module-zope.testing python3-module-zodbpickle
#BuildPreReq: python3-module-zc.zk-tests
#BuildPreReq: python3-module-ZODB3
#BuildPreReq: python3-module-twisted-core
#BuildPreReq: python3-module-ZEO-tests
BuildPreReq: python-tools-2to3
#BuildPreReq: python3-module-zc.zkzeo
BuildRequires: python3
%endif

%py_provides %oname
#%py_requires zc ZODB3 twisted.python zope.interface zc.zkzeo json

%description
ZODB replicated storage (ZRS) provides database replication for ZODB.
For each database, a primary storage and one or more secondary storages
may be defined. The secondary storages will automatically replicate data
from the primary storage.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
#%py_requires zope.testing zc.zk ZEO.tests zc.zk.testing mock

%description tests
ZODB replicated storage (ZRS) provides database replication for ZODB.
For each database, a primary storage and one or more secondary storages
may be defined. The secondary storages will automatically replicate data
from the primary storage.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: ZODB Replicated Storage
Group: Development/Python3
%py3_provides %oname
#%py3_requires zc ZODB3 twisted.python zope.interface zc.zkzeo

%description -n python3-module-%oname
ZODB replicated storage (ZRS) provides database replication for ZODB.
For each database, a primary storage and one or more secondary storages
may be defined. The secondary storages will automatically replicate data
from the primary storage.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
#%py3_requires zope.testing zc.zk ZEO.tests zc.zk.testing mock

%description -n python3-module-%oname-tests
ZODB replicated storage (ZRS) provides database replication for ZODB.
For each database, a primary storage and one or more secondary storages
may be defined. The secondary storages will automatically replicate data
from the primary storage.

This package contains tests for %oname.

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
%python3_build_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_build_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

cp -fR src/zc/zrs/xformstorage \
	%buildroot%python_sitelibdir/zc/zrs/
%if_with python3
pushd ../python3
cp -fR src/zc/zrs/xformstorage \
	%buildroot%python3_sitelibdir/zc/zrs/
popd
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/zc/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/zc/*/tests.*

%files tests
%python_sitelibdir/zc/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%_bindir/*.py3
%python3_sitelibdir/zc/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/zc/*/tests.*
%exclude %python3_sitelibdir/zc/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/zc/*/tests.*
%python3_sitelibdir/zc/*/*/tests.*
%endif

%changelog
* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 2.5.3-alt2.git20150216
- Cleanup buildreq

* Sat Feb 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.3-alt1.git20150216
- Version 2.5.3

* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.2-alt1.git20150207
- Version 2.5.2

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.4-alt1.dev.git20130815
- Initial build for Sisyphus

