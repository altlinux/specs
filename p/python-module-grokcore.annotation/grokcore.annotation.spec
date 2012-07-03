%define oname grokcore.annotation
Name: python-module-%oname
Version: 1.2
Release: alt2.1
Summary: Grok-like configuration for Zope annotations
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/grokcore.annotation/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires grokcore ZODB3 grokcore.component martian zope.annotation 
%py_requires zope.component zope.container zope.interface

%description
This package provides a support to simplify the use of annotations in
Zope.

%package tests
Summary: Test for grokcore.annotation
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides a support to simplify the use of annotations in
Zope.

This package contains test for grokcore.annotation.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt2.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2
- Added necessary requirements
- Excludes *.pth

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Initial build for Sisyphus

