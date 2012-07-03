%define oname grokcore.formlib
Name: python-module-%oname
Version: 1.8
Release: alt2.1
Summary: Grok-like configuration for zope.formlib components
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/grokcore.formlib/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires grokcore grokcore.component grokcore.security
%py_requires grokcore.view martian pytz zope.container zope.event
%py_requires zope.formlib zope.interface zope.lifecycleevent
%py_requires zope.publisher zope.schema

%description
This package provides support for writing forms using the Zope Formlib
library and registering them directly in Python (without ZCML).

%package tests
Summary: Tests for grokcore.formlib
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides support for writing forms using the Zope Formlib
library and registering them directly in Python (without ZCML).

This package contains tests for grokcore.formlib.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8-alt2.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt2
- Added necessary requirements
- Excluded *.pth

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt1
- Initial build for Sisyphus

