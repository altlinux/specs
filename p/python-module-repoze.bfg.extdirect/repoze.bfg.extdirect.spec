%define oname repoze.bfg.extdirect
Name: python-module-%oname
Version: 0.1.3
Release: alt1.1
Summary: ExtDirect Implementation for repoze
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.bfg.extdirect/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze.bfg venusian

%description
This repoze.bfg plugin provides a router for the ExtDirect Sencha API
included in ExtJS 3.x. ExtDirect allows to run server-side callbacks
directly through JavaScript without the extra AJAX boilerplate.

%package tests
Summary: Tests for repoze.bfg.extdirect
Group: Development/Python
Requires: %name = %version-%release

%description tests
This repoze.bfg plugin provides a router for the ExtDirect Sencha API
included in ExtJS 3.x. ExtDirect allows to run server-side callbacks
directly through JavaScript without the extra AJAX boilerplate.

This package contains tests for repoze.bfg.extdirect.

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
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.3-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1
- Initial build for Sisyphus

