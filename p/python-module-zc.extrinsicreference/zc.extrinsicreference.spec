%define oname zc.extrinsicreference
Name: python-module-%oname
Version: 0.3.0
Release: alt2.1
Summary: Extrinsic reference registries
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.extrinsicreference/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires ZODB3 zc.shortcut zope.app.keyreference zope.component
%py_requires zope.interface zope.testing

%description
Extrinsic reference registries record a key and one or more values to
which they refer. The key and all values must be adaptable to
zope.app.keyreference.interfaces.IKeyReference.

%package tests
Summary: Tests for Extrinsic reference registries
Group: Development/Python
Requires: %name = %version-%release

%description tests
Extrinsic reference registries record a key and one or more values to
which they refer. The key and all values must be adaptable to
zope.app.keyreference.interfaces.IKeyReference.

This package contains tests for Extrinsic reference registries.

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
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

