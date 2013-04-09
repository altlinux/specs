%define oname zope.copypastemove
Name: python-module-%oname
Version: 4.0.0
Release: alt1.a1
Summary: Copy, Paste and Move support for content components
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.copypastemove/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope zope.annotation zope.component zope.container
%py_requires zope.copy zope.event zope.exceptions zope.interface
%py_requires zope.lifecycleevent zope.location

%description
This package provides Copy, Paste and Move support for content
components in Zope.

%package tests
Summary: Tests for zope.copypastemove
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.principalannotation zope.testing zope.traversing
%py_requires zope.dublincore

%description tests
This package provides Copy, Paste and Move support for content
components in Zope.

This package contains tests for zope.copypastemove.

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
* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a1
- Version 4.0.0a1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.8.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.0-alt1
- Initial build for Sisyphus

