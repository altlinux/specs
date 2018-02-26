%define oname z3c.dav
Name: python-module-%oname
Version: 1.0b2
Release: alt2.1
Summary: Implementation of the WebDAV protocol for Zope3
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.dav/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.etree z3c.conditionalviews zope.app.zcmlfiles
%py_requires zope.securitypolicy

%description
The *z3c.dav* package is an implementation of the WebDAV protocol for Zope3.
*z3c.dav* supports the *zope.app.folder* content type, within the scope of the
core RFC2518 protocol. *z3c.dav* also contains a number of components that
help developers support WebDAV in their application. These components include
the ability to handle WebDAV specific errors, to generate multi-status
responses, and an implementation of all core WebDAV methods exist that use
zope component to lookup specific adapters that perform the required action.
For example locking parses the request and then looks up a IDAVLockmanager
adapter to perform the locking and unlocking of objects. But if the required
adapter does not exist then a `405 Method Not Allowed` response is returned
to the client.

%package tests
Summary: Tests for z3c.dav
Group: Development/Python
Requires: %name = %version-%release

%description tests
The *z3c.dav* package is an implementation of the WebDAV protocol for Zope3.
*z3c.dav* supports the *zope.app.folder* content type, within the scope of the
core RFC2518 protocol. *z3c.dav* also contains a number of components that
help developers support WebDAV in their application. These components include
the ability to handle WebDAV specific errors, to generate multi-status
responses, and an implementation of all core WebDAV methods exist that use
zope component to lookup specific adapters that perform the required action.
For example locking parses the request and then looks up a IDAVLockmanager
adapter to perform the locking and unlocking of objects. But if the required
adapter does not exist then a `405 Method Not Allowed` response is returned
to the client.

This package contains tests for z3c.dav.

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
%exclude %python_sitelibdir/*/*/*test*
%exclude %python_sitelibdir/*/*/*/*test*

%files tests
%python_sitelibdir/*/*/*test*
%python_sitelibdir/*/*/*/*test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0b2-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b2-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b2-alt1
- Initial build for Sisyphus

