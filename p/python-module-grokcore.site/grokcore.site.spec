%define oname grokcore.site
Name: python-module-%oname
Version: 1.5
Release: alt2.1
Summary: Grok-like configuration for Zope local site and utilities
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/grokcore.site/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires grokcore ZODB3 grokcore.component martian zope.annotation
%py_requires zope.component zope.container zope.interface
%py_requires zope.lifecycleevent zope.site

%description
This package provides support to write local site and utilities for Zope
directly in Python (without ZCML).

%package tests
Summary: Tests for grokcore.site
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.appsetup zope.component zope.configuration
%py_requires zope.location zope.testing

%description tests
This package provides support to write local site and utilities for Zope
directly in Python (without ZCML).

This pacckage contains tests for grokcore.site.

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

%files tests
%python_sitelibdir/*/*/*test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5-alt2.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt2
- Added nececssary requirements
- Excluded *.pth

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1
- Initial build for Sisyphus

