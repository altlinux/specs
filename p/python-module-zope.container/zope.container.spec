%define oname zope.container
Name: python-module-%oname
Version: 3.12.0
Release: alt3.1.1
Summary: Zope Container
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.container/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

Requires: python-module-zope.i18nmessageid

%py_requires zope.interface zope.dottedname zope.schema 
%py_requires zope.component zope.event zope.location zope.security
%py_requires zope.lifecycleevent

%description
This package define interfaces of container components, and provides
container implementations such as a BTreeContainer and OrderedContainer,
as well as the base class used by zope.site.folder for the Folder
implementation.

%package tests
Summary: Tests for Zope Container
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package define interfaces of container components, and provides
container implementations such as a BTreeContainer and OrderedContainer,
as well as the base class used by zope.site.folder for the Folder
implementation.

This package contains tests for Zope Container.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.12.0-alt3.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.12.0-alt3.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.0-alt3
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.0-alt2
- Added necessary requirements
- Excluded *.th

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.0-alt1
- Initial build for Sisyphus

