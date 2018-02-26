%define oname z3c.zrtresource
Name: python-module-%oname
Version: 1.3.0
Release: alt2.1
Summary: Zope Resource Templates
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.zrtresource/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.site zope.pagetemplate zope.browserresource
%py_requires zope.component zope.configuration zope.interface
%py_requires zope.publisher zope.schema zope.security

%description
This package provides a very simple templating system for non-SGML data
files such as CSS and Javascript.

%package tests
Summary: Tests for Zope Resource Templates
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.traversing

%description tests
This package provides a very simple templating system for non-SGML data
files such as CSS and Javascript.

This package contains tests for Zope Resource Templates.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus

