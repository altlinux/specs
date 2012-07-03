%define oname z3c.macroviewlet
Name: python-module-%oname
Version: 1.1.0
Release: alt2.1
Summary: Viewlets based on ZPT macros
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.macroviewlet/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app.component zope.browserpage zope.app.publisher
%py_requires zope.app.testing zope.component zope.configuration
%py_requires zope.contentprovider zope.interface zope.pagetemplate
%py_requires zope.publisher zope.schema zope.security zope.traversing

%description
Macro viewlets are Zope 3 UI components. In particular they allow the
developer to specify viewlets based on macros instead of entire
templates.

%package tests
Summary: Tests for Viewlets based on ZPT macros
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.testing zope.viewlet z3c.template
%py_requires z3c.testing

%description tests
Macro viewlets are Zope 3 UI components. In particular they allow the
developer to specify viewlets based on macros instead of entire
templates.

Thiss package contains tests for Viewlets based on ZPT macros.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

