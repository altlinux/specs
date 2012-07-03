%define oname Acquisition
Name: python-module-%oname
Version: 2.13.7
Release: alt2.1.1
Summary: Zope implements acquisition with "Extension Class" mix-in classes
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/Acquisition/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires ExtensionClass zope.interface

%description
Acquisition is a mechanism that allows objects to obtain attributes from
the containment hierarchy they're in.

%package tests
Summary: Tests for Acquisition
Group: Development/Python
Requires: %name = %version-%release

%description tests
Acquisition is a mechanism that allows objects to obtain attributes from
the containment hierarchy they're in.

This package contains tests for Acquisition.

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
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.13.7-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.13.7-alt2.1
- Rebuild with Python-2.7

* Tue Jun 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.7-alt2
- Added necessary requirements

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.7-alt1
- Initial build for Sisyphus

