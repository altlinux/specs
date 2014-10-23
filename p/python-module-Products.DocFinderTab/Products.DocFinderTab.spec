%define oname Products.DocFinderTab
Name: python-module-%oname
Version: 1.0.5
Release: alt1
Summary: Makes Dieter Maurer's DocFinder available from a ZMI management tab
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.DocFinderTab/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.component-tests python-module-nose
BuildPreReq: python-module-zope.security-tests

%py_provides %oname

%description
This product makes Dieter Maurer's DocFinder available from a ZMI
management tab. Looking inside an object becomes as easy as clicking its
"Doc" tab!

DocFinderTab allows you to view an object's:

* Class (and base class) names and docstrings.
* Attribute names, roles, arguments, and docstrings.

DocFinderTab can be of great help when discovering object APIs and
debugging security problems.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.component.testing zope.security.testing

%description tests
This product makes Dieter Maurer's DocFinder available from a ZMI
management tab. Looking inside an object becomes as easy as clicking its
"Doc" tab!

DocFinderTab allows you to view an object's:

* Class (and base class) names and docstrings.
* Attribute names, roles, arguments, and docstrings.

DocFinderTab can be of great help when discovering object APIs and
debugging security problems.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test

%files
%doc *.txt
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Thu Oct 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt1
- Initial build for Sisyphus

