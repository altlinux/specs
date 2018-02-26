%define oname repoze.cssutils
Name: python-module-%oname
Version: 1.0a6
Release: alt1.1
Summary: CSS parsing and utilities
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.cssutils/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze nose

%description
repoze.cssutils provides css parsing and utilities for CSS 2.1 and CSS3.

%package tests
Summary: Tests for repoze.cssutils
Group: Development/Python
Requires: %name = %version-%release

%description tests
repoze.cssutils provides css parsing and utilities for CSS 2.1 and CSS3.

This package contains tests for repoze.cssutils.

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
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0a6-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0a6-alt1
- Initial build for Sisyphus

