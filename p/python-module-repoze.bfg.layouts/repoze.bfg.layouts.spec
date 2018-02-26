%define oname repoze.bfg.layouts
Name: python-module-%oname
Version: 0.2
Release: alt2.1
Summary: Dynamic layouts for repoze.bfg
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.bfg.layouts/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze.bfg repoze.bfg.skins zope.configuration
%py_requires chameleon.html

%description
repoze.bfg.layouts provides a site layout story for the repoze.bfg
framework. It uses familiar technologies like CSS3 to dynamically inject
dynamic content into static HTML.

%package tests
Summary: Tests for repoze.bfg.layouts
Group: Development/Python
Requires: %name = %version-%release

%description tests
repoze.bfg.layouts provides a site layout story for the repoze.bfg
framework. It uses familiar technologies like CSS3 to dynamically inject
dynamic content into static HTML.

This package contains tests for repoze.bfg.layouts.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

