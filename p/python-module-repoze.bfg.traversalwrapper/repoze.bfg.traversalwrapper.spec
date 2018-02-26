%define oname repoze.bfg.traversalwrapper
Name: python-module-%oname
Version: 0.3
Release: alt2.1
Summary: Supply a model graph traverser which proxies location-ignorant model objects
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.bfg.traversalwrapper/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze.bfg zope.interface zope.proxy zope.testing

%description
An alternate implementation of the
repoze.bfg.interfaces.ITraverserFactory (a "traverser") which wraps each
traversed object in a proxy. This allows a "location-ignorant" model (a
model which does not possess intrinsic __name__ and __parent__
attributes) to be used as the root object and as any object returned
from any other model's __getitem__ method during traversal.

%package tests
Summary: Tests for repoze.bfg.traversalwrapper
Group: Development/Python
Requires: %name = %version-%release

%description tests
An alternate implementation of the
repoze.bfg.interfaces.ITraverserFactory (a "traverser") which wraps each
traversed object in a proxy. This allows a "location-ignorant" model (a
model which does not possess intrinsic __name__ and __parent__
attributes) to be used as the root object and as any object returned
from any other model's __getitem__ method during traversal.

This package contains tests for repoze.bfg.traversalwrapper.

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
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

