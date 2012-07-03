%define oname repoze.bfg.htmlpage
Name: python-module-%oname
Version: 0.3.2
Release: alt2.1
Summary: Dynamic HTML pages for repoze.bfg
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.bfg.htmlpage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze.bfg repoze.bfg.skins zope.configuration
%py_requires chameleon.html

%description
This package provides a page-level rendering system for the repoze.bfg
web framework.

It uses familiar technologies like HTML and CSS to dynamically use an
existing HTML document as template.

%package tests
Summary: Tests for repoze.bfg.htmlpage
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides a page-level rendering system for the repoze.bfg
web framework.

It uses familiar technologies like HTML and CSS to dynamically use an
existing HTML document as template.

This package contains tests for repoze.bfg.htmlpage.

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
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.2-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1
- Initial build for Sisyphus

