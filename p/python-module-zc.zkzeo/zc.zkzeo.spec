%define mname zc
%define oname %mname.zkzeo

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.0.1
Release: alt1.git20150111.1
Summary: ZEO support for finding and registering servers with ZooKeeper
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/zc.zkzeo/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/zc.zkzeo.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-manuel-tests python-module-netifaces
#BuildPreReq: python-module-zc.zk-tests python-module-ZEO
#BuildPreReq: python-module-zc.thread python-module-zodbpickle
#BuildPreReq: python-module-zc.monitor
#BuildPreReq: python-module-zope.configuration
#BuildPreReq: python-module-zope.testing
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-manuel-tests python3-module-netifaces
#BuildPreReq: python3-module-zc.zk-tests python3-module-ZEO
#BuildPreReq: python3-module-zc.thread python3-module-zodbpickle
#BuildPreReq: python3-module-zc.monitor
#BuildPreReq: python3-module-zope.configuration
#BuildPreReq: python3-module-zope.testing
%endif

%py_provides %oname
%py_requires %mname zc.zk ZEO zc.thread zc.monitor zope.configuration

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-BTrees python-module-ZODB python-module-persistent python-module-setuptools python-module-transaction python-module-zc.lockfile python-module-zc.ngi python-module-zc.thread python-module-zdaemon python-module-zope.component python-module-zope.event python-module-zope.exceptions python-module-zope.hookable python-module-zope.i18nmessageid python-module-zope.interface python-module-zope.proxy python-module-zope.schema python-module-zope.testing python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-unittest python3 python3-base python3-module-BTrees python3-module-ZODB python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-persistent python3-module-pip python3-module-pycparser python3-module-setuptools python3-module-transaction python3-module-zc.lockfile python3-module-zc.ngi python3-module-zc.thread python3-module-zdaemon python3-module-zope python3-module-zope.component python3-module-zope.event python3-module-zope.exceptions python3-module-zope.i18nmessageid python3-module-zope.interface python3-module-zope.proxy python3-module-zope.schema python3-module-zope.testing
BuildRequires: python-module-ZEO python-module-pbr python-module-pytest python-module-unittest2 python-module-zc.monitor python-module-zc.zk python-module-zope.configuration python3-module-ZEO python3-module-html5lib python3-module-pbr python3-module-pytest python3-module-unittest2 python3-module-zc.monitor python3-module-zc.zk python3-module-zope.configuration rpm-build-python3

%description
Managing addresses, and especially ports is a drag. ZooKeeper can be
used as a service registry. Servers can register themselves and clients
can find services there. The zc.zkzeo package provides support for
registering ZEO servers and a ZEO client storage that gets addresses
from ZooKeeper.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing zc.zk.tests manuel.testing

%description tests
Managing addresses, and especially ports is a drag. ZooKeeper can be
used as a service registry. Servers can register themselves and clients
can find services there. The zc.zkzeo package provides support for
registering ZEO servers and a ZEO client storage that gets addresses
from ZooKeeper.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: ZEO support for finding and registering servers with ZooKeeper
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname zc.zk ZEO zc.thread zc.monitor zope.configuration

%description -n python3-module-%oname
Managing addresses, and especially ports is a drag. ZooKeeper can be
used as a service registry. Servers can register themselves and clients
can find services there. The zc.zkzeo package provides support for
registering ZEO servers and a ZEO client storage that gets addresses
from ZooKeeper.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires zope.testing zc.zk.tests manuel.testing

%description -n python3-module-%oname-tests
Managing addresses, and especially ports is a drag. ZooKeeper can be
used as a service registry. Servers can register themselves and clients
can find services there. The zc.zkzeo package provides support for
registering ZEO servers and a ZEO client storage that gets addresses
from ZooKeeper.

This package contains tests for %oname.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/*/tests.*
%exclude %python3_sitelibdir/%mname/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/%mname/*/tests.*
%python3_sitelibdir/%mname/*/*/tests.*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt1.git20150111.1
- NMU: Use buildreq for BR.

* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20150111
- Initial build for Sisyphus

