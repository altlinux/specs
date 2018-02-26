%define oname repoze.who.plugins.formcookie
Name: python-module-%oname
Version: 0.3.0
Release: alt1.1
Summary: Stores came_from in cookie instead of url query string
License: Free
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.who.plugins.formcookie/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze.who.plugins paste

%description
Similar to RedirectingFormPlugin, but stores came_from in cookie instead
of url query string

%package tests
Summary: Tests for repoze.who.plugins.formcookie
Group: Development/Python
Requires: %name = %version-%release
%py_requires webob webtest nose

%description tests
Similar to RedirectingFormPlugin, but stores came_from in cookie instead
of url query string

This package contains tests for repoze.who.plugins.formcookie.

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
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.0-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

