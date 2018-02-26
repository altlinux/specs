%define oname repoze.vhm
Name: python-module-%oname
Version: 0.13
Release: alt1.git20110322.1.1
Summary: Commit / abort transactions via WSGI middleware
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.vhm
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.vhm.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze

%description
This package provides middleware and utilities for doing virtual
hosting within a WSGI/Repoze environment.  It is particularly useful
within a ``repoze.zope2`` environment, where it may be used as an
alternative to the classic `VirtualHostMonster` method of doing
virtual hosting.

%package tests
Summary: Tests for repoze.vhm
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides middleware and utilities for doing virtual
hosting within a WSGI/Repoze environment.  It is particularly useful
within a ``repoze.zope2`` environment, where it may be used as an
alternative to the classic `VirtualHostMonster` method of doing
virtual hosting.

This package contains tests for repoze.vhm.

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
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.13-alt1.git20110322.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1.git20110322.1
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1.git20110322
- Initial build for Sisyphus

