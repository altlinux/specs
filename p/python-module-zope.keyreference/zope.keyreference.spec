%define oname zope.keyreference
Name: python-module-%oname
Version: 3.6.4
Release: alt1
Summary: Zope Key References
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.keyreference/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope ZODB3 zope.component zope.i18nmessageid
%py_requires zope.interface zope.schema

%description
Object references that support stable comparison and hashes.

%package tests
Summary: Tests for zope.keyreference
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
Object references that support stable comparison and hashes.

This package contains tests for zope.keyreference.

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
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.4-alt1
- Version 3.6.4

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.2-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt1
- Initial build for Sisyphus

