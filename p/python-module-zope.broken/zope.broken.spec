%define oname zope.broken
Name: python-module-%oname
Version: 3.6.0
Release: alt2.1
Summary: Zope Broken Object Interfaces
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.broken/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope zope.interface

%description
This package is obsolete and its functionality has been merged into the
ZODB3 distribution itself. If you use version 3.10 or later of ZODB3,
please change your imports of the IBroken interface to a direct:

  from ZODB.interfaces import IBroken

You can use this package with older versions of the ZODB3, which didn't
have the IBroken interface yet.

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

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt1
- Initial build for Sisyphus

