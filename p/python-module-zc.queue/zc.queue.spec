%define oname zc.queue
Name: python-module-%oname
Version: 1.2.1
Release: alt1
Summary: Queues that are optimized for persistency via the ZODB.
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.queue/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

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

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1
- Version 1.2.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

