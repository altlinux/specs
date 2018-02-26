%define oname repoze.urchin
Name: python-module-%oname
Version: 0.2
Release: alt1
Summary: WSGI middleware for Google analytics
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.urchin/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze webob

%description
This package provides WSGI middleware for injecting the markup required
to use Google Analytics into web pages.

%package tests
Summary: Tests for repoze.urchin
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides WSGI middleware for injecting the markup required
to use Google Analytics into web pages.

This package contains tests for repoze.urchin.

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
%doc *.txt docs/*.rst docs/*.ini
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Tue Dec 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Version 0.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

