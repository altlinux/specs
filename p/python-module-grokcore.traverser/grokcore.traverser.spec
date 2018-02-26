%define oname grokcore.traverser
Name: python-module-%oname
Version: 1.0
Release: alt2.1
Summary: Traverser for the Grok Framework
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/grokcore.traverser/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires grokcore grokcore.component grokcore.security
%py_requires grokcore.view grokcore.rest martian zope.component
%py_requires zope.interface zope.publisher

%description
Traverser for the Grok Framework.

%package tests
Summary: Tests for grokcore.traverser
Group: Development/Python
Requires: %name = %version-%release
%py_requires grokcore.view grokcore.content zope.app.wsgi
%py_requires zope.app.appsetup zope.testing

%description tests
Traverser for the Grok Framework.

This package contains tests for grokcore.traverser.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

