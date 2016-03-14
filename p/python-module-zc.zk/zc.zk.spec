%define oname zc.zk

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.1.0
Release: alt1.git20141020.1.1
Summary: Service registration and discovery with ZooKeeper
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/zc.zk/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/zc.zk.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-zc.thread python-module-kazoo
#BuildPreReq: python-module-zope.testing python-module-mock
#BuildPreReq: python-module-manuel python-module-zope.event
#BuildPreReq: python-module-netifaces python-module-zope.component
#BuildPreReq: python-module-zc.monitor
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-zc.thread python3-module-kazoo
#BuildPreReq: python3-module-zope.testing python3-module-mock
#BuildPreReq: python3-module-manuel python3-module-zope.event
#BuildPreReq: python3-module-netifaces python3-module-zope.component
#BuildPreReq: python3-module-zc.monitor python-tools-2to3
%endif

%py_provides %oname
%py_requires zc zc.thread zope.event

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-persistent python-module-setuptools python-module-zc.ngi python-module-zope.component python-module-zope.event python-module-zope.exceptions python-module-zope.hookable python-module-zope.interface python-module-zope.testing python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-setuptools python3-module-zc.ngi python3-module-zope python3-module-zope.component python3-module-zope.event python3-module-zope.exceptions python3-module-zope.interface python3-module-zope.testing
BuildRequires: python-module-pbr python-module-pytest python-module-unittest2 python-module-zc.monitor python-module-zc.thread python3-module-html5lib python3-module-pbr python3-module-pytest python3-module-unittest2 python3-module-zc.monitor python3-module-zc.thread rpm-build-python3 time

%description
The zc.zk package provides support for registering and discovering
services with ZooKeeper. It also provides support for defining services
with a tree-based model and syncing the model with ZooKeeper.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing zope.event zope.component zc.monitor

%description tests
The zc.zk package provides support for registering and discovering
services with ZooKeeper. It also provides support for defining services
with a tree-based model and syncing the model with ZooKeeper.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Service registration and discovery with ZooKeeper
Group: Development/Python3
%py3_provides %oname
%py3_requires zc zc.thread zope.event

%description -n python3-module-%oname
The zc.zk package provides support for registering and discovering
services with ZooKeeper. It also provides support for defining services
with a tree-based model and syncing the model with ZooKeeper.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires zope.testing zope.event zope.component zc.monitor

%description -n python3-module-%oname-tests
The zc.zk package provides support for registering and discovering
services with ZooKeeper. It also provides support for defining services
with a tree-based model and syncing the model with ZooKeeper.

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
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/zc/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/zc/*/test*

%files tests
%python_sitelibdir/zc/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/zc/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/zc/*/test*
%exclude %python3_sitelibdir/zc/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/zc/*/test*
%python3_sitelibdir/zc/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.0-alt1.git20141020.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.1.0-alt1.git20141020.1
- NMU: Use buildreq for BR.

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1.git20141020
- Initial build for Sisyphus

