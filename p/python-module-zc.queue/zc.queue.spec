%define oname zc.queue

%def_with python3

Name: python-module-%oname
Version: 2.0.0
Release: alt2.a1.1
Summary: Queues that are optimized for persistency via the ZODB.
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.queue/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zc zope.interface ZODB3

%description
Persistent queues are simply queues that are optimized for persistency
via the ZODB. They assume that the ZODB is using MVCC to avoid read
conflicts. They attempt to resolve write conflicts so that transactions
that add and remove objects simultaneously are merged, unless the
transactions are trying to remove the same value from the queue.

An important characteristic of these queues is that they do not expect
to hold more than one reference to any given equivalent item at a time.
For instance, some of the conflict resolution features will not perform
desirably if it is reasonable for your application to hold two copies of
the string "hello" within the same queue at once.

%package -n python3-module-%oname
Summary: Queues that are optimized for persistency via the ZODB
Group: Development/Python3
%py3_requires zc zope.interface ZODB3

%description -n python3-module-%oname
Persistent queues are simply queues that are optimized for persistency
via the ZODB. They assume that the ZODB is using MVCC to avoid read
conflicts. They attempt to resolve write conflicts so that transactions
that add and remove objects simultaneously are merged, unless the
transactions are trying to remove the same value from the queue.

An important characteristic of these queues is that they do not expect
to hold more than one reference to any given equivalent item at a time.
For instance, some of the conflict resolution features will not perform
desirably if it is reasonable for your application to hold two copies of
the string "hello" within the same queue at once.

%package -n python3-module-%oname-tests
Summary: Tests for zc.queue
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
Persistent queues are simply queues that are optimized for persistency
via the ZODB. They assume that the ZODB is using MVCC to avoid read
conflicts. They attempt to resolve write conflicts so that transactions
that add and remove objects simultaneously are merged, unless the
transactions are trying to remove the same value from the queue.

An important characteristic of these queues is that they do not expect
to hold more than one reference to any given equivalent item at a time.
For instance, some of the conflict resolution features will not perform
desirably if it is reasonable for your application to hold two copies of
the string "hello" within the same queue at once.

This package contains tests for zc.queue.

%package tests
Summary: Tests for zc.queue
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
Persistent queues are simply queues that are optimized for persistency
via the ZODB. They assume that the ZODB is using MVCC to avoid read
conflicts. They attempt to resolve write conflicts so that transactions
that add and remove objects simultaneously are merged, unless the
transactions are trying to remove the same value from the queue.

An important characteristic of these queues is that they do not expect
to hold more than one reference to any given equivalent item at a time.
For instance, some of the conflict resolution features will not perform
desirably if it is reasonable for your application to hold two copies of
the string "hello" within the same queue at once.

This package contains tests for zc.queue.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt2.a1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.a1
- Added module for Python 3

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.a1
- Version 2.0.0a1

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1
- Version 1.2.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

