%define oname z3c.profiler
Name: python-module-%oname
Version: 0.10.0
Release: alt2.1
Summary: Profiler skin for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.profiler/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.layer.pagelet z3c.macro z3c.pagelet z3c.template
%py_requires z3c.zrtresource zope.app.wsgi zope.browserpage
%py_requires zope.component zope.componentvocabulary zope.configuration
%py_requires zope.contentprovider zope.i18n zope.i18nmessageid
%py_requires zope.contentprovider zope.i18n zope.i18nmessageid
%py_requires zope.interface zope.login zope.principalregistry
%py_requires zope.schema zope.security zope.securitypolicy zope.testing
%py_requires zope.traversing zope.viewlet

%description
This package provides a profiler skin which allows you to profile pages.

%package tests
Summary: Tests for Profiler skin for Zope3
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.etestbrowser zope.app.testing

%description tests
This package provides a profiler skin which allows you to profile pages.

This package contains tests for Profiler skin for Zope3.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.10.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt1
- Initial build for Sisyphus

