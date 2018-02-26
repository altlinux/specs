%define oname grokcore.rest
Name: python-module-%oname
Version: 1.2
Release: alt2.1
Summary: REST View component for Grok
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/grokcore.rest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires grokcore grokcore.component grokcore.security grokcore.view
%py_requires grokcore.traverser martian zope.component zope.interface
%py_requires zope.publisher

%description
This packages provides base classes and a advanced traversal mechanism
for Grok based REST-Views.

%package tests
Summary: Tests for grokcore.rest
Group: Development/Python
Requires: %name = %version-%release
%py_requires grokcore.content grokcore.view zope.app.appsetup
%py_requires zope.app.wsgi zope.errorview zope.testing

%description tests
This packages provides base classes and a advanced traversal mechanism
for Grok based REST-Views.

This package contains tests for grokcore.rest.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt2.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Initial build for Sisyphus

