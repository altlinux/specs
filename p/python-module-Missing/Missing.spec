%define oname Missing
Name: python-module-%oname
Version: 2.13.1
Release: alt1.1.1
Summary: Special Missing objects used in Zope2
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/Missing/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires ExtensionClass

%description
Missing provides special objects used in some Zope2 internals like the
ZCatalog.

%package tests
Summary: Tests for Special Missing objects used in Zope2
Group: Development/Python
Requires: %name = %version-%release

%description tests
Missing provides special objects used in some Zope2 internals like the
ZCatalog.

This package contains tests for Special Missing objects used in Zope2.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.13.1-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.13.1-alt1.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.1-alt1
- Initial build for Sisyphus

