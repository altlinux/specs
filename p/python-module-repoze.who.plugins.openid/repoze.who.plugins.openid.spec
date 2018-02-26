%define oname repoze.who.plugins.openid
Name: python-module-%oname
Version: 0.5.3
Release: alt1.1
Summary: An OpenID plugin for repoze.who
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.who.plugins.openid/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze.who.plugins openid webob zope.interface

%description
repoze.who.plugins.openid is a plugin for the repoze.who framework
enabling OpenID logins.

%package tests
Summary: Tests for repoze.who.plugins.openid
Group: Development/Python
Requires: %name = %version-%release

%description tests
repoze.who.plugins.openid is a plugin for the repoze.who framework
enabling OpenID logins.

This package contains tests for repoze.who.plugins.openid.

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
%exclude %python_sitelibdir/*/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.3-alt1.1
- Rebuild with Python-2.7

* Fri Jul 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt1
- Initial build for Sisyphus

