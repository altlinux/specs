%define oname repoze.bfg.jinja2
Name: python-module-%oname
Version: 0.6
Release: alt2.1
Summary: Jinja2 template bindings for repoze.bfg
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.bfg.jinja2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze.bfg jinja2

%description
These are bindings for the `Jinja2 templating system` for the
``repoze.bfg`` web framework.

%package tests
Summary: Tests for repoze.bfg.jinja2
Group: Development/Python
Requires: %name = %version-%release

%description tests
These are bindings for the `Jinja2 templating system` for the
``repoze.bfg`` web framework.

This package contains tests for repoze.bfg.jinja2.

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
%exclude %python_sitelibdir/*/*/*/*/*/tests*

%files tests
%python_sitelibdir/*/*/*/tests
%python_sitelibdir/*/*/*/*/*/tests*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1
- Initial build for Sisyphus

