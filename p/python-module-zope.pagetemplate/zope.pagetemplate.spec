%define oname zope.pagetemplate
Name: python-module-%oname
Version: 3.6.3
Release: alt1
Summary: Zope Page Templates
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.pagetemplate/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope zope.interface zope.component zope.security zope.tales
%py_requires zope.tal zope.i18n zope.i18nmessageid zope.traversing

%description
Page Templates provide an elegant templating mechanism that achieves a
clean separation of presentation and application logic while allowing
for designers to work with templates in their visual editing tools
(FrontPage, Dreamweaver, GoLive, etc.).

%package tests
Summary: Tests for Page Templates
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.proxy zope.security

%description tests
Page Templates provide an elegant templating mechanism that achieves a
clean separation of presentation and application logic while allowing
for designers to work with templates in their visual editing tools
(FrontPage, Dreamweaver, GoLive, etc.).

This package contains tests for Page Templates.

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
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.3-alt1
- Version 3.6.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.2-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt2
- Set as archdep package

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt1
- Initial build for Sisyphus

