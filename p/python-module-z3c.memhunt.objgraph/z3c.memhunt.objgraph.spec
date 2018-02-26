%define oname z3c.memhunt.objgraph
Name: python-module-%oname
Version: 0.1dev.r118724
Release: alt2.1
Summary: Help locate and diagnose memory leaks in zope applications
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.memhunt.objgraph/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires guppy objgraph

%description
z3c.memhunt.objgraph was created to help locate and diagnose memory
leaks in zope applications. This package uses objgraph and guppy to help
with this task.

%package tests
Summary: Tests for z3c.memhunt.objgraph
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
z3c.memhunt.objgraph was created to help locate and diagnose memory
leaks in zope applications. This package uses objgraph and guppy to help
with this task.

This package contains tests for z3c.memhunt.objgraph.

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

touch %buildroot%python_sitelibdir/z3c/memhunt/__init__.py

%files
%doc *.txt docs/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1dev.r118724-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1dev.r118724-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1dev.r118724-alt1
- Initial build for Sisyphus

