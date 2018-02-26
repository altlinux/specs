%define oname z3c.davapp.zopeappfile
Name: python-module-%oname
Version: 1.0b1
Release: alt3.1
Summary: Define the WebDAV data model from the `zope.app.file' module.
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.davapp.zopeappfile/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.davapp z3c.dav zope.app.file

%description
Define the WebDAV data model for the File and Image objects from the
`zope.app.file' module.

%package tests
Summary: Tests for z3c.davapp.zopeappfile
Group: Development/Python
Requires: %name = %version-%release
%py_requires cElementTree

%description tests
Define the WebDAV data model for the File and Image objects from the
`zope.app.file' module.

This package contains tests for z3c.davapp.zopeappfile.

%package -n python-module-z3c.davapp
Summary: Core files for z3c.davapp
Group: Development/Python
%py_provides z3c.davapp

%description -n python-module-z3c.davapp
Core files for z3c.davapp.

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

touch %buildroot%python_sitelibdir/z3c/davapp/__init__.py

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/tests.*
%exclude %python_sitelibdir/z3c/davapp/__init__.py*

%files tests
%python_sitelibdir/*/*/*/tests.*

%files -n python-module-z3c.davapp
%python_sitelibdir/z3c/davapp/__init__.py*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0b1-alt3.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b1-alt3
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b1-alt2
- Added __init__.py into z3c.davapp

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b1-alt1
- Initial build for Sisyphus

