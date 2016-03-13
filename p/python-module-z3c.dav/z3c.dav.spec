%define oname z3c.dav

%def_with python3

Name: python-module-%oname
Version: 1.0b2
Release: alt3.1
Summary: Implementation of the WebDAV protocol for Zope3
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.dav/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

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

%package -n python3-module-%oname
Summary: Implementation of the WebDAV protocol for Zope3
Group: Development/Python3
%py3_requires z3c.etree z3c.conditionalviews zope.app.zcmlfiles
%py3_requires zope.securitypolicy

%description -n python3-module-%oname
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

%package -n python3-module-%oname-tests
Summary: Tests for z3c.dav
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
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

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%exclude %python_sitelibdir/*/*/*test*
%exclude %python_sitelibdir/*/*/*/*test*

%files tests
%python_sitelibdir/*/*/*test*
%python_sitelibdir/*/*/*/*test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*test*
%exclude %python3_sitelibdir/*/*/*/*test*
%exclude %python3_sitelibdir/*/*/*/*/*test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*test*
%python3_sitelibdir/*/*/*/*test*
%python3_sitelibdir/*/*/*/*/*test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0b2-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b2-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0b2-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b2-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b2-alt1
- Initial build for Sisyphus

