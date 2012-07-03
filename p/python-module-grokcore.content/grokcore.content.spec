%define oname grokcore.content
Name: python-module-%oname
Version: 1.1
Release: alt2.1
Summary: Base content types for Grok
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/grokcore.content/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires grokcore ZODB3 grokcore.component zope.annotation
%py_requires zope.container zope.interface

%description
This package provides base classes of basic content types.

%package tests
Summary: Tests for grokcore.content
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.component

%description tests
This package provides base classes of basic content types.

This package contains tests for grokcore.content.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

