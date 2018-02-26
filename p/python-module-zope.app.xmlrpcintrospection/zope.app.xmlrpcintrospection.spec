%define oname zope.app.xmlrpcintrospection
Name: python-module-%oname
Version: 3.5.1
Release: alt2.1
Summary: XML-RPC Method Introspection Support for Zope 3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.xmlrpcintrospection/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app zope.component zope.interface zope.publisher

%description
This Zope 3 package provides an XML-RPC introspection mechanism.

%package tests
Summary: Tests for zope.app.xmlrpcintrospection
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.site zope.app.securitypolicy
%py_requires zope.app.zcmlfiles zope.login

%description tests
This Zope 3 package provides an XML-RPC introspection mechanism.

This package contains tests for zope.app.xmlrpcintrospection.

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
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1
- Initial build for Sisyphus

