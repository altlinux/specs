%define oname zope.intid
Name: python-module-%oname
Version: 3.7.2
Release: alt2.1
Summary: Integer Id Utility
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.intid
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope ZODB3 zope.lifecycleevent zope.component zope.event
%py_requires zope.interface zope.keyreference zope.location zope.security

%description
This package provides an API to create integer ids for any object. Later
objects can be looked up by their id as well. This functionality is
commonly used in situations where dealing with objects is undesirably,
such as in search indices or any code that needs an easy hash of an
object.

%package tests
Summary: Tests for zope.intid
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.site zope.traversing zope.container

%description tests
This package provides an API to create integer ids for any object. Later
objects can be looked up by their id as well. This functionality is
commonly used in situations where dealing with objects is undesirably,
such as in search indices or any code that needs an easy hash of an
object.

This package contains tests for zope.intid.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.2-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.2-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.2-alt1
- Initial build for Sisyphus

