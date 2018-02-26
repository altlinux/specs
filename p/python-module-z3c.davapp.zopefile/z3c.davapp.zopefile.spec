%define oname z3c.davapp.zopefile
Name: python-module-%oname
Version: 1.0b1
Release: alt2.1
Summary: Define the WebDAV data model for the File and Image objects from the `zope.file' module
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.davapp.zopefile/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.dav z3c.conditionalviews zope.file z3c.davapp

%description
Define the WebDAV data model for the File and Image objects from the
`zope.file' module.

%package tests
Summary: Tests for z3c.davapp.zopefile
Group: Development/Python
Requires: %name = %version-%release
%py_requires cElementTree

%description tests
Define the WebDAV data model for the File and Image objects from the
`zope.file' module.

This package contains tests for z3c.davapp.zopefile.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0b1-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b1-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b1-alt1
- Initial build for Sisyphus

