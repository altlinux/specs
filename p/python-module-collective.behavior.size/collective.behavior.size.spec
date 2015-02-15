%define mname collective.behavior
%define oname %mname.size
Name: python-module-%oname
Version: 0.3
Release: alt1.git20131028
Summary: Provides size related behavior, such as weight and three dimensional size
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.behavior.size/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.behavior.size.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-mock
BuildPreReq: python-module-plone.behavior
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-Products.CMFCore

%py_provides %oname
%py_requires %mname plone.behavior plone.supermodel plone.autoform
%py_requires zope.i18nmessageid zope.schema zope.interface

%description
collective.behavior.size provides size related behavior, such as weight
and three dimensional size, to dexterity content types.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires mock plone.app.testing Products.CMFCore

%description tests
collective.behavior.size provides size related behavior, such as weight
and three dimensional size, to dexterity content types.

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
%doc *.rst
%python_sitelibdir/collective/behavior/size
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/behavior/size/tests

%files tests
%python_sitelibdir/collective/behavior/size/tests

%changelog
* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20131028
- Initial build for Sisyphus

