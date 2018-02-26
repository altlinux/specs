%define oname repoze.obob
Name: python-module-%oname
Version: 0.4
Release: alt2.1
Summary: Zope-like publisher as WSGI application
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.obob/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze paste.script WSGIUtils

%description
repoze.obob is a reconstruction of the "bobo" precursor of Zope (the
"object publisher" portion), stripped down to be used as a possible
application endpoint in the 'repoze' stack.

%package tests
Summary: Tests for repoze.obob
Group: Development/Python
Requires: %name = %version-%release

%description tests
repoze.obob is a reconstruction of the "bobo" precursor of Zope (the
"object publisher" portion), stripped down to be used as a possible
application endpoint in the 'repoze' stack.

This package contains tests for repoze.obob.

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
%doc *.txt doc/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/*/*/tests*

%files tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/*/*/tests*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4-alt2.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Initial build for Sisyphus

