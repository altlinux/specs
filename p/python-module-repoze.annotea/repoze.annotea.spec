%define oname repoze.annotea
Name: python-module-%oname
Version: 0.1
Release: alt2.1
Summary: Implement W3C Annotea server in repoze
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.annotea/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze.bfg rdflib repoze.bfg.restrequest repoze.catalog
%py_requires repoze.errorlog repoze.folder repoze.retry repoze.tm2
%py_requires repoze.zodbconn

%description
repoze.annotea implements the server side of the W3C Annotea
specification for RDF-based annotations on content, using repoze.bfg as
the underlying framework for the application.

%package tests
Summary: Tests for repoze.annotea
Group: Development/Python
Requires: %name = %version-%release

%description tests
repoze.annotea implements the server side of the W3C Annotea
specification for RDF-based annotations on content, using repoze.bfg as
the underlying framework for the application.

This package contains tests for repoze.annotea.

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
%doc *.txt docs/*.rst
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

