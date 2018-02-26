%define oname z3c.sharedmimeinfo
Name: python-module-%oname
Version: 0.1.0
Release: alt2.1
Summary: MIME type guessing framework for Zope, based on shared-mime-info
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.sharedmimeinfo/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.i18n zope.i18nmessageid zope.interface zope.schema

%description
This package provides an utility for guessing MIME type from file name
and/or actual contents. It's based on freedesktop.org's shared-mime-info
database.

%package tests
Summary: Tests for z3c.sharedmimeinfo
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.component

%description tests
This package provides an utility for guessing MIME type from file name
and/or actual contents. It's based on freedesktop.org's shared-mime-info
database.

This package contains tests for z3c.sharedmimeinfo.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus

