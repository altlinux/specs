%define oname zope.modulealias
Name: python-module-%oname
Version: 3.4.0
Release: alt2.1
Summary: Zope modulealias
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.modulealias/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope zope.interface zope.configuration

%description
This package enables the developer to make one module available under a
different path.

%package tests
Summary: Tests for zope.modulealias
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package enables the developer to make one module available under a
different path.

This package contains tests for zope.modulealias.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.0-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

