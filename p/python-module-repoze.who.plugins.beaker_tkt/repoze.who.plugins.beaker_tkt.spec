%define oname repoze.who.plugins.beaker_tkt
Name: python-module-%oname
Version: 0.1
Release: alt3.1
Summary: Identifier (auth_tkt) plugin with beaker.session cache implementation
License: Free
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.who.plugins.beaker_tkt/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze.who.plugins paste.script beaker

%description
BeakerAuthTktPlugin acts the same way as CookieAuthTktPlugin, but
instead of caching identity through cookie, it stores it in Beaker
session.

%package tests
Summary: Tests for repoze.who.plugins.beaker_tkt
Group: Development/Python
Requires: %name = %version-%release
%py_requires webob webtest nose

%description tests
BeakerAuthTktPlugin acts the same way as CookieAuthTktPlugin, but
instead of caching identity through cookie, it stores it in Beaker
session.

This package contains tests for repoze.who.plugins.beaker_tkt.

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
%exclude %python_sitelibdir/*/__init__.*
%exclude %python_sitelibdir/*/*/__init__.*
%exclude %python_sitelibdir/*/*/*/__init__.*
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt3.1
- Rebuild with Python-2.7

* Wed Jul 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3
- Avoid conflict with python-module-repoze.who (previous stage doesn't
  completed)

* Tue Jul 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Avoid conflict with python-module-repoze.who

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

