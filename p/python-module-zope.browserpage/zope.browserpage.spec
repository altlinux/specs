%define oname zope.browserpage
Name: python-module-%oname
Version: 3.12.2
Release: alt4.1
Summary: ZCML directives for configuring browser views for Zope
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.browserpage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.pagetemplate zope.component zope.configuration
%py_requires zope.interface zope.publisher zope.schema zope.security
%py_requires zope.traversing

%description
This package is at present not reusable without depending on a large
chunk of the Zope Toolkit and its assumptions.

%package tests
Summary: Tests for zope.browserpage
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.browsermenu

%description tests
This package is at present not reusable without depending on a large
chunk of the Zope Toolkit and its assumptions.

This package contains tests for zope.browserpage.

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
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.12.2-alt4.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.2-alt4
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.2-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.2-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.2-alt1
- Initial build for Sisyphus

