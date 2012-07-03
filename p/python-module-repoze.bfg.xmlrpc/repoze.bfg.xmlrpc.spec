%define oname repoze.bfg.xmlrpc
Name: python-module-%oname
Version: 0.4
Release: alt2.1
Summary: XML-RPC support for repoze.bfg
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.bfg.xmlrpc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze.bfg

%description
XML-RPC support for repoze.bfg.

%package tests
Summary: Tests for repoze.bfg.xmlrpc
Group: Development/Python
Requires: %name = %version-%release

%description tests
XML-RPC support for repoze.bfg.

This package contains tests for repoze.bfg.xmlrpc.

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
%doc *.txt docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4-alt2.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt2
- Excluded *.pth

* Wed Jun 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Initial build for Sisyphus

