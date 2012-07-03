%define oname zc.twist
Name: python-module-%oname
Version: 1.3.1
Release: alt2.1.1
Summary: Mixing Twisted and ZODB
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.twist/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

Requires: python-module-twisted-core
%py_requires zc ZODB3 zope.component zope.testing

%description
Twist: Talking to the ZODB in Twisted Reactor Calls.

The twist package contains a few functions and classes, but primarily a
helper for having a deferred call on a callable persistent object, or on
a method on a persistent object. This lets you have a Twisted reactor
call or a Twisted deferred callback affect the ZODB. Everything can be
done within the main thread, so it can be full-bore Twisted usage,
without threads.

%package tests
Summary: Tests for Mixing Twisted and ZODB
Group: Development/Python
Requires: %name = %version-%release

%description tests
Twist: Talking to the ZODB in Twisted Reactor Calls.

The twist package contains a few functions and classes, but primarily a
helper for having a deferred call on a callable persistent object, or on
a method on a persistent object. This lets you have a Twisted reactor
call or a Twisted deferred callback affect the ZODB. Everything can be
done within the main thread, so it can be full-bore Twisted usage,
without threads.

This package contains tests for Mixing Twisted and ZODB.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/__init__.*
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.1-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.1-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt2
- Added necessary requirements

* Mon Jun 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus

