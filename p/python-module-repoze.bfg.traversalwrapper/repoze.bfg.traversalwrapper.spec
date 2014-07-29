%define oname repoze.bfg.traversalwrapper

%def_with python3

Name: python-module-%oname
Version: 0.3
Release: alt3
Summary: Supply a model graph traverser which proxies location-ignorant model objects
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.bfg.traversalwrapper/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires repoze.bfg zope.interface zope.proxy zope.testing

%description
An alternate implementation of the
repoze.bfg.interfaces.ITraverserFactory (a "traverser") which wraps each
traversed object in a proxy. This allows a "location-ignorant" model (a
model which does not possess intrinsic __name__ and __parent__
attributes) to be used as the root object and as any object returned
from any other model's __getitem__ method during traversal.

%package -n python3-module-%oname
Summary: Supply a model graph traverser which proxies location-ignorant model objects
Group: Development/Python3
%py3_requires repoze.bfg zope.interface zope.proxy zope.testing

%description -n python3-module-%oname
An alternate implementation of the
repoze.bfg.interfaces.ITraverserFactory (a "traverser") which wraps each
traversed object in a proxy. This allows a "location-ignorant" model (a
model which does not possess intrinsic __name__ and __parent__
attributes) to be used as the root object and as any object returned
from any other model's __getitem__ method during traversal.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.bfg.traversalwrapper
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
An alternate implementation of the
repoze.bfg.interfaces.ITraverserFactory (a "traverser") which wraps each
traversed object in a proxy. This allows a "location-ignorant" model (a
model which does not possess intrinsic __name__ and __parent__
attributes) to be used as the root object and as any object returned
from any other model's __getitem__ method during traversal.

This package contains tests for repoze.bfg.traversalwrapper.

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

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/tests.*
%endif

%changelog
* Tue Jul 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

