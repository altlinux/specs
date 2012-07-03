%define oname Zope2
Name: python-module-%oname
Version: 2.13.7
Release: alt2.1
Summary: Zope2 application server / web framework
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/Zope2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
# http://cvs.zope.org/*checkout*/Python-2.2.3/Lib/regsub.py?rev=1.1.1.1&cvsroot=Zope.org&sortby=author&content-type=text/plain
Source1: regsub.py
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute
BuildPreReq: python-module-sphinx-devel

%add_python_req_skip ntsecuritycon pywintypes win32api win32con win32event

%description
Zope2 is an open-source web application server.

%package tests
Summary: Tests for Zope2
Group: Development/Python
Requires: %name = %version-%release

%add_python_req_skip http_date

%description tests
Zope2 is an open-source web application server.

This package contains tests for Zope2.

%package pickles
Summary: Pickles for Zope2
Group: Development/Python

%description pickles
Zope2 is an open-source web application server.

This package contains pickles for Zope2.

%package docs
Summary: Documentation for Zope2
Group: Development/Documentation
BuildArch: noarch

%description docs
Zope2 is an open-source web application server.

This package contains documentation for Zope2.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build

pushd doc
export PYTHONPATH=$PWD/../build/lib
%make pickle
%make html
popd

%install
%python_install

touch %buildroot%python_sitelibdir/Shared/__init__.py
touch %buildroot%python_sitelibdir/Products/__init__.py
touch %buildroot%python_sitelibdir/Testing/__init__.py

install -p -m644 %SOURCE1 %buildroot%python_sitelibdir

cp -fR doc/.build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/*test*
%exclude %python_sitelibdir/*/*/*/test*
%exclude %python_sitelibdir/*/*/*/*/tests
%exclude %python_sitelibdir/*/Test*
%exclude %python_sitelibdir/Test*
%exclude %python_sitelibdir/%oname/pickle

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/*test*
%python_sitelibdir/*/*/*/test*
%python_sitelibdir/*/*/*/*/tests
%python_sitelibdir/*/Test*
%python_sitelibdir/Test*

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc doc/.build/html/*

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.13.7-alt2.1
- Rebuild with Python-2.7

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.7-alt2
- Moved all tests into tests package

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.7-alt1
- Initial build for Sisyphus

