%define oname Persistence
Name: python-module-%oname
Version: 2.13.2
Release: alt2.1.1
Summary: Persistent ExtensionClass
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/Persistence/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires ExtensionClass ZODB3

%description
This package provides a variant of the persistent base class that's an
ExtensionClass. Unless you need ExtensionClass semantics, you probably
want to use persistent.Persistent from ZODB3.

%package tests
Summary: Tests for Persistent ExtensionClass
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides a variant of the persistent base class that's an
ExtensionClass. Unless you need ExtensionClass semantics, you probably
want to use persistent.Persistent from ZODB3.

This package contains tests for Persistent ExtensionClass.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.13.2-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.13.2-alt2.1
- Rebuild with Python-2.7

* Tue Jun 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.2-alt2
- Added necessary requirements

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.2-alt1
- Initial build for Sisyphus

