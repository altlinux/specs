%define oname z3c.davapp.zopeappfile

%def_with python3

Name: python-module-%oname
Version: 1.0b1
Release: alt4.1
Summary: Define the WebDAV data model from the `zope.app.file' module.
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.davapp.zopeappfile/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires z3c.davapp z3c.dav zope.app.file

%description
Define the WebDAV data model for the File and Image objects from the
`zope.app.file' module.

%package -n python3-module-%oname
Summary: Define the WebDAV data model from the `zope.app.file' module
Group: Development/Python3
%py3_requires z3c.davapp z3c.dav zope.app.file

%description -n python3-module-%oname
Define the WebDAV data model for the File and Image objects from the
`zope.app.file' module.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.davapp.zopeappfile
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
#py_requires cElementTree

%description -n python3-module-%oname-tests
Define the WebDAV data model for the File and Image objects from the
`zope.app.file' module.

This package contains tests for z3c.davapp.zopeappfile.

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

%package -n python3-module-z3c.davapp
Summary: Core files for z3c.davapp
Group: Development/Python3
%py3_provides z3c.davapp

%description -n python3-module-z3c.davapp
Core files for z3c.davapp.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif
touch %buildroot%python_sitelibdir/z3c/davapp/__init__.py

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
touch %buildroot%python3_sitelibdir/z3c/davapp/__init__.py
%endif

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

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/tests.*
%exclude %python3_sitelibdir/z3c/davapp/__init__.py
%exclude %python3_sitelibdir/z3c/davapp/__pycache__/__init__.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/tests.*

%files -n python3-module-z3c.davapp
%python3_sitelibdir/z3c/davapp/__init__.py
%python3_sitelibdir/z3c/davapp/__pycache__/__init__.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0b1-alt4.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b1-alt4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0b1-alt3.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b1-alt3
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b1-alt2
- Added __init__.py into z3c.davapp

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b1-alt1
- Initial build for Sisyphus

