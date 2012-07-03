%define oname z3c.requestlet
Name: python-module-%oname
Version: 0.9.1
Release: alt2.1
Summary: Log and show ram usage of a zope instance per request
License: GPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.requestlet/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%description
Log and show ram usage of a zope instance per request.

By calling @@requestlet, you'll get a nice graph and (if you mark
something in it) a table with ram usage, difference to the last request
and the URI over time.

%package tests
Summary: Tests for z3c.requestlet
Group: Development/Python
Requires: %name = %version-%release

%description tests
Log and show ram usage of a zope instance per request.

By calling @@requestlet, you'll get a nice graph and (if you mark
something in it) a table with ram usage, difference to the last request
and the URI over time.

This package contains tests for z3c.requestlet.

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
%doc *.txt docs/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.1-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt2
- Excluded *.pth

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1
- Initial build for Sisyphus

