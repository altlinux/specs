%define oname Record
Name: python-module-%oname
Version: 3.0.1
Release: alt1.git20130504
Summary: Special Record objects used in Zope2
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/Record/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/Record.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Zope2-tests

%py_requires ExtensionClass

%description
Record provides special objects used in some Zope2 internals like ZRDB.

%package tests
Summary: Tests for Special Record objects used in Zope2
Group: Development/Python
Requires: %name = %version-%release

%description tests
Record provides special objects used in some Zope2 internals like ZRDB.

This package contains tests for Special Record objects used in Zope2.

%prep
%setup

%build
%python_build

%install
%python_install

%check
python setup.py test

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt1.git20130504
- Version 3.0.1
- Enabled testing

* Mon Sep 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1
- Version 3.0

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.13.0-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.13.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.0-alt2
- Added necessary requirements

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.0-alt1
- Initial build for Sisyphus

