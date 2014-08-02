%define oname pyramid_traversalwrapper

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt2
Summary: Supplies a model graph traverser which proxies location-ignorant model objects
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid_traversalwrapper/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires pyramid zope.interface zope.proxy

%description
An alternate implementation of the pyramid.interfaces.ITraverserFactory
(a "traverser") which wraps each traversed object in a proxy. This
allows a "location-ignorant" model (a model which does not possess
intrinsic __name__ and __parent__ attributes) to be used as the root
object and as any object returned from any other model's __getitem__
method during traversal.

%package -n python3-module-%oname
Summary: Supplies a model graph traverser which proxies location-ignorant model objects
Group: Development/Python3
%py3_requires pyramid zope.interface zope.proxy

%description -n python3-module-%oname
An alternate implementation of the pyramid.interfaces.ITraverserFactory
(a "traverser") which wraps each traversed object in a proxy. This
allows a "location-ignorant" model (a model which does not possess
intrinsic __name__ and __parent__ attributes) to be used as the root
object and as any object returned from any other model's __getitem__
method during traversal.

%package -n python3-module-%oname-tests
Summary: Tests for pyramid_traversalwrapper
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
An alternate implementation of the pyramid.interfaces.ITraverserFactory
(a "traverser") which wraps each traversed object in a proxy. This
allows a "location-ignorant" model (a model which does not possess
intrinsic __name__ and __parent__ attributes) to be used as the root
object and as any object returned from any other model's __getitem__
method during traversal.

This package contains tests for pyramid_traversalwrapper.

%package tests
Summary: Tests for pyramid_traversalwrapper
Group: Development/Python
Requires: %name = %version-%release

%description tests
An alternate implementation of the pyramid.interfaces.ITraverserFactory
(a "traverser") which wraps each traversed object in a proxy. This
allows a "location-ignorant" model (a model which does not possess
intrinsic __name__ and __parent__ attributes) to be used as the root
object and as any object returned from any other model's __getitem__
method during traversal.

This package contains tests for pyramid_traversalwrapper.

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

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.txt docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Sat Aug 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1.1
- Rebuild with Python-2.7

* Wed Jul 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

