%define oname zope.app.zptpage
Name: python-module-%oname
Version: 3.5.1
Release: alt2.1
Summary: ZPT page content component
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.zptpage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app zope.container zope.app.publication
%py_requires zope.filerepresentation zope.formlib zope.i18nmessageid
%py_requires zope.index zope.interface zope.pagetemplate zope.publisher
%py_requires zope.schema zope.security zope.site zope.size
%py_requires zope.traversing ZODB3

%description
ZPT page content component.

%package tests
Summary: Tests for ZPT page content component
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.securitypolicy zope.app.zcmlfiles
%py_requires zope.login zope.tal

%description tests
ZPT page content component.

This package contains tests for ZPT page content component.

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
%exclude %python_sitelibdir/*/*/*/*/test*

%files tests
%python_sitelibdir/*/*/*/test*
%python_sitelibdir/*/*/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1
- Initial build for Sisyphus

