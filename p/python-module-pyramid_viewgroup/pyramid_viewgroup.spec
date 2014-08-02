%define oname pyramid_viewgroup

%def_with python3

Name: python-module-%oname
Version: 0.5
Release: alt2
Summary: An anlologue of Zope 3 "content providers" for Pyramid
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid_viewgroup/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires pyramid pyramid_zcml

%description
pyramid_viewgroup is an extension for the pyramid web framework. The
extensio makes it possible to make a viewgroup declaration which acts
much like view inasmuch as it results in a Pyramid view registration.
Unlike a "normal" view registration, however, a viewgroup registration
refers to one or more other Pyramid views (matching them by name, for
interface, and request type). When a viewgroup is invoked (either via
traversal or via programmatic view execution), a viewgroup will return a
response which appends all the referenced view renderings together in a
single body.

%package -n python3-module-%oname
Summary: An anlologue of Zope 3 "content providers" for Pyramid
Group: Development/Python3
%py3_requires pyramid pyramid_zcml

%description -n python3-module-%oname
pyramid_viewgroup is an extension for the pyramid web framework. The
extensio makes it possible to make a viewgroup declaration which acts
much like view inasmuch as it results in a Pyramid view registration.
Unlike a "normal" view registration, however, a viewgroup registration
refers to one or more other Pyramid views (matching them by name, for
interface, and request type). When a viewgroup is invoked (either via
traversal or via programmatic view execution), a viewgroup will return a
response which appends all the referenced view renderings together in a
single body.

%package -n python3-module-%oname-tests
Summary: Tests for pyramid_viewgroup
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
pyramid_viewgroup is an extension for the pyramid web framework. The
extensio makes it possible to make a viewgroup declaration which acts
much like view inasmuch as it results in a Pyramid view registration.
Unlike a "normal" view registration, however, a viewgroup registration
refers to one or more other Pyramid views (matching them by name, for
interface, and request type). When a viewgroup is invoked (either via
traversal or via programmatic view execution), a viewgroup will return a
response which appends all the referenced view renderings together in a
single body.

This package contains tests for pyramid_viewgroup.

%package tests
Summary: Tests for pyramid_viewgroup
Group: Development/Python
Requires: %name = %version-%release

%description tests
pyramid_viewgroup is an extension for the pyramid web framework. The
extensio makes it possible to make a viewgroup declaration which acts
much like view inasmuch as it results in a Pyramid view registration.
Unlike a "normal" view registration, however, a viewgroup registration
refers to one or more other Pyramid views (matching them by name, for
interface, and request type). When a viewgroup is invoked (either via
traversal or via programmatic view execution), a viewgroup will return a
response which appends all the referenced view renderings together in a
single body.

This package contains tests for pyramid_viewgroup.

%prep
%setup

%if_with python3
cp -fR . ../python3
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
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sat Aug 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt2
- Added module for Python 3

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1
- Version 0.5

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Version 0.4

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt1.1
- Rebuild with Python-2.7

* Wed Jul 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

