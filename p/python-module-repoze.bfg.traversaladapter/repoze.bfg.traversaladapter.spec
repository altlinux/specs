%define oname repoze.bfg.traversaladapter
Name: python-module-%oname
Version: 0.1
Release: alt2.1
Summary: Allow registering arbitrary adapters for the type or interface of model objects
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.bfg.traversaladapter/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze.bfg zope.interface zope.testing

%description
An alternate implementation of the
repoze.bfg.interfaces.ITraverserFactory (a "traverser") which allows you
to register an adapter factory for the type or interface(s) of objects
encountered during traversal. This is a generalization of the
repoze.bfg.traversalwrapper package which automatically wraps each
traversed object into a location-aware proxy.

%package tests
Summary: Tests for repoze.bfg.traversaladapter
Group: Development/Python
Requires: %name = %version-%release

%description tests
An alternate implementation of the
repoze.bfg.interfaces.ITraverserFactory (a "traverser") which allows you
to register an adapter factory for the type or interface(s) of objects
encountered during traversal. This is a generalization of the
repoze.bfg.traversalwrapper package which automatically wraps each
traversed object into a location-aware proxy.

This package contains tests for repoze.bfg.traversaladapter.

%prep
%setup

touch CHANGES.txt

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
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

