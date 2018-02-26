%define oname zc.ssl
Name: python-module-%oname
Version: 1.2
Release: alt2.1
Summary: An HTTPSConnection implementation with the new ssl module
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.ssl/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc zope.testing

%description
An HTTPSConnection implementation with the new ssl module.

%package tests
Summary: Tests for zc.ssl
Group: Development/Python
Requires: %name = %version-%release

%description tests
An HTTPSConnection implementation with the new ssl module.

This package contains tests for zc.ssl.

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
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2
- Added necessary requirements
- Excluded *.pth

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Initial build for Sisyphus

