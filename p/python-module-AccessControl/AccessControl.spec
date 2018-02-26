%define oname AccessControl
Name: python-module-%oname
Version: 2.13.4
Release: alt2.1.1
Summary: Security framework for Zope2
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/AccessControl/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires Acquisition DateTime ExtensionClass Persistence Record
%py_requires RestrictedPython transaction zExceptions ZODB3
%py_requires zope.component zope.configuration zope.deferredimport
%py_requires zope.interface zope.publisher zope.schema zope.security
%py_requires zope.testing

%description
AccessControl provides a general security framework for use in Zope2.

%package tests
Summary: Tests for Security framework for Zope2
Group: Development/Python
Requires: %name = %version-%release

%description tests
AccessControl provides a general security framework for use in Zope2.

This package contains tests for Security framework for Zope2.

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
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.13.4-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.13.4-alt2.1
- Rebuild with Python-2.7

* Tue Jun 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.4-alt2
- Added necessary requirements

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.4-alt1
- Initial build for Sisyphus

