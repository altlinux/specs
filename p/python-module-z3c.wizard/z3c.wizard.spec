%define oname z3c.wizard
Name: python-module-%oname
Version: 0.9.1
Release: alt1
Summary: Wizard based on z3c.form for for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.wizard/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.form z3c.formui z3c.pagelet zope.browserpage
%py_requires zope.component zope.configuration zope.event
%py_requires zope.i18nmessageid zope.interface zope.lifecycleevent
%py_requires zope.location zope.publisher zope.schema zope.security
%py_requires zope.traversing

%description
This package provides a form wizard concept based on z3c.form for Zope3.

%package tests
Summary: Tests for z3c.wizard
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.macro z3c.testing zope.app.pagetemplate
%py_requires zope.app.testing zope.publisher zope.testing
%py_requires zope.browserresource

%description tests
This package provides a form wizard concept based on z3c.form for Zope3.

This package contains tests for z3c.wizard.

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
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%changelog
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1
- Version 0.9.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus

