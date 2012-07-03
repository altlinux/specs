%define oname repoze.errorlog
Name: python-module-%oname
Version: 0.9.1
Release: alt1.git20110322.1.1
Summary: WSGI middleware: intercept / log / browse exceptions
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.errorlog
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.errorlog.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze meld3 paste

%description
This package implements a WSGI middleware filter which intercepts
exceptions and writes them to a Python logging module channel (or the
``wsgi.errors`` filehandle, if no channel is configured).  It also
allows the browsing of limited exception history via a browser UI.

%package tests
Summary: Tests for repoze.errorlog
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package implements a WSGI middleware filter which intercepts
exceptions and writes them to a Python logging module channel (or the
``wsgi.errors`` filehandle, if no channel is configured).  It also
allows the browsing of limited exception history via a browser UI.

This package contains tests for repoze.errorlog.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.1-alt1.git20110322.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.git20110322.1
- Added necessary requirements
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.git20110322
- Initial build for Sisyphus

