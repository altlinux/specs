%define oname repoze.bfg.skins
Name: python-module-%oname
Version: 0.22
Release: alt2.1
Summary: Skin support for BFG
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.bfg.skins/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze.bfg chameleon zope.interface zope.component
%py_requires zope.configuration zope.testing

%description
This package provides a simple framework to integrate code with
templates and resources.

%package tests
Summary: Tests for repoze.bfg.skins
Group: Development/Python
Requires: %name = %version-%release
%py_requires pyinotify manuel

%description tests
This package provides a simple framework to integrate code with
templates and resources.

This package contains tests for repoze.bfg.skins.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.22-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.22-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.22-alt1
- Initial build for Sisyphus

