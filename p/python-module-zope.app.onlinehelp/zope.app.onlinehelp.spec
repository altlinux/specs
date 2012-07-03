%define oname zope.app.onlinehelp
Name: python-module-%oname
Version: 3.5.2
Release: alt2.1
Summary: Framework for Context-Sensitive Help Pages
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.onlinehelp/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires ZODB3 zope.app.component zope.app.file
%py_requires zope.app.pagetemplate zope.app.publication
%py_requires zope.app.security zope.app.testing zope.component
%py_requires zope.configuration zope.container zope.contenttype
%py_requires zope.i18n zope.interface zope.location zope.publisher
%py_requires zope.schema zope.security zope.testing zope.traversing

%description
This package provides a framework for creating help pages for Zope 3
applications. ZCML directives are used to minimize the overhead of
creating new help pages.

%package tests
Summary: Tests for zope.app.onlinehelp
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.preference zope.app.apidoc
%py_requires zope.site zope.login zope.app.securitypolicy
%py_requires zope.app.zcmlfiles zope.securitypolicy

%description tests
This package provides a framework for creating help pages for Zope 3
applications. ZCML directives are used to minimize the overhead of
creating new help pages.

This package contains tests for zope.app.onlinehelp.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.2-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt1
- Initial build for Sisyphus

