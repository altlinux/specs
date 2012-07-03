%define oname ZODB3
Name: python-module-%oname
Version: 3.10.5
Release: alt1.1
Summary: Zope Object Database: object database and persistence
License: ZPL
Group: Sciences/Mathematics
Url: http://pypi.python.org/pypi/ZODB3/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_provides %oname
%py_requires transaction zc.lockfile ZConfig zdaemon zope.event
%py_requires zope.interface

%description
The Zope Object Database provides an object-oriented database for Python
that provides a high-degree of transparency. Applications can take
advantage of object database features with few, if any, changes to
application logic. ZODB includes features such as a plugable storage
interface, rich transaction support, and undo.

%package tests
Summary: Tests for Zope Object Database
Group: Development/Python
Requires: %name = %version-%release

%description tests
The Zope Object Database provides an object-oriented database for Python
that provides a high-degree of transparency. Applications can take
advantage of object database features with few, if any, changes to
application logic. ZODB includes features such as a plugable storage
interface, rich transaction support, and undo.

This package contains tests for Zope Object Database.

%package docs
Summary: Documentation for Zope Object Database
Group: Development/Documentation
BuildArch: noarch

%description docs
The Zope Object Database provides an object-oriented database for Python
that provides a high-degree of transparency. Applications can take
advantage of object database features with few, if any, changes to
application logic. ZODB includes features such as a plugable storage
interface, rich transaction support, and undo.

This package contains documentation for Zope Object Database.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc COPYING *.txt
%_bindir/*
%_includedir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/*test*

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/*test*

%files docs
%doc doc/*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.10.5-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Dec 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.5-alt1
- Version 3.10.5

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.10.3-alt3.1
- Rebuild with Python-2.7

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.3-alt3
- Added necessary requirements

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.3-alt2
- Moved all tests into tests package

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.3-alt1
- Initial build for Sisyphus

