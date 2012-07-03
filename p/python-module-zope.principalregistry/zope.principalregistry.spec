%define oname zope.principalregistry
Name: python-module-%oname
Version: 3.7.1
Release: alt2.1
Summary: Global principal registry component for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.principalregistry/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope zope.authentication zope.component zope.interface
%py_requires zope.password zope.security

%description
This package provides an authentication utility for zope.authentication
that uses simple non-persistent principal registry.

%package tests
Summary: Tests for zope.principalregistry
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.component

%description tests
This package provides an authentication utility for zope.authentication
that uses simple non-persistent principal registry.

This package contains tests for zope.principalregistry

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.1-alt1
- Initial build for Sisyphus

