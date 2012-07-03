%define oname repoze.whoplugins.zodb
Name: python-module-%oname
Version: 1.0.1
Release: alt2.1
Summary: ZODB authenticator and metadata plugin for repoze.who
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.whoplugins.zodb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze.who.plugins repoze.who repoze.zodbconn transaction
%py_requires ZODB3

%description
A repoze.who plugin to authenticate a userid and attach group
information based on information stored in a ZODB database.

%package tests
Summary: Tests for repoze.whoplugins.zodb
Group: Development/Python
Requires: %name = %version-%release

%description tests
A repoze.who plugin to authenticate a userid and attach group
information based on information stored in a ZODB database.

This package contains tests for repoze.whoplugins.zodb.

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
%exclude %python_sitelibdir/*/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt2.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

