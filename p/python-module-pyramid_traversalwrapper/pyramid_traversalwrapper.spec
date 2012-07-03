%define oname pyramid_traversalwrapper
Name: python-module-%oname
Version: 0.1
Release: alt1.1
Summary: Supplies a model graph traverser which proxies location-ignorant model objects
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid_traversalwrapper/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%py_requires pyramid zope.interface zope.proxy

%description
An alternate implementation of the pyramid.interfaces.ITraverserFactory
(a "traverser") which wraps each traversed object in a proxy. This
allows a "location-ignorant" model (a model which does not possess
intrinsic __name__ and __parent__ attributes) to be used as the root
object and as any object returned from any other model's __getitem__
method during traversal.

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

%build
%python_build

%install
%python_install

%files
%doc *.txt docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1.1
- Rebuild with Python-2.7

* Wed Jul 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

