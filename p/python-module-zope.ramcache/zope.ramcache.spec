%define oname zope.ramcache
Name: python-module-%oname
Version: 1.0
Release: alt2.1
Summary: Zope RAM Cache
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.ramcache/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope zope.interface zope.location zope.testing ZODB3

%description
This package provides a RAM cache implementation for Zope.

%package tests
Summary: Tests for Zope RAM Cache
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides a RAM cache implementation for Zope.

This package contains tests for Zope RAM Cache.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

