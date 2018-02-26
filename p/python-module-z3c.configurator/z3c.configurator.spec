%define oname z3c.configurator
Name: python-module-%oname
Version: 1.3.0
Release: alt2.1
Summary: Dynamic configuration for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.configurator/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.component zope.i18nmessageid zope.interface
%py_requires zope.schema

%description
This package provides a configurator which is designed to extend a
component after its creation for Zope3.

%package tests
Summary: Tests for Dynamic configuration for Zope3
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.annotation zope.dublincore zope.formlib
%py_requires zope.securitypolicy zope.testbrowser zope.testing
%py_requires zope.app.pagetemplate zope.app.testing zope.app.zcmlfiles

%description tests
This package provides a configurator which is designed to extend a
component after its creation for Zope3.

This package contains tests for Dynamic configuration for Zope3.

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
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/test*
%python_sitelibdir/*/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.0-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus

