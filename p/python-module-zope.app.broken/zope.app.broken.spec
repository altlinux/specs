%define oname zope.app.broken
Name: python-module-%oname
Version: 3.6.0
Release: alt2.1
Summary: Zope Broken (ZODB) Object Support
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.broken/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app zope.interface zope.location zope.security
%py_requires zope.annotation zope.broken zope.processlifetime ZODB3

%description
When an object cannot be correctly loaded from the ZODB, this package
allows this object still to be instantiated, but as a "Broken" object.
This allows for gracefully updating the database without interuption.

%package tests
Summary: Tests for Zope Broken (ZODB) Object Support
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
When an object cannot be correctly loaded from the ZODB, this package
allows this object still to be instantiated, but as a "Broken" object.
This allows for gracefully updating the database without interuption.

This package contains tests for Zope Broken (ZODB) Object Support.

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
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt1
- Initial build for Sisyphus

