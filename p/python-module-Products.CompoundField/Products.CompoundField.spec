%define oname Products.CompoundField
Name: python-module-%oname
Version: 1.2
Release: alt1.dev2.git20130509
Summary: Compound- and Array-Field and -Widget for Archetypes
License: D-FSL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.CompoundField/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.CompoundField.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFDynamicViewFTI
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Marshall
BuildPreReq: python-module-Products.validation
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.Archetypes Products.CMFPlone Products.CMFCore
%py_requires Products.CMFDynamicViewFTI Products.Marshall zope.interface
%py_requires Products.validation

%description
This Product includes CompoundField and ArrayField. Both are fields for
use within Archetypes Products.

CompoundField
    field that itself consists of several sub-fields defined in an own
    Schema.
ArrayField
    field containing one field severals times.

It also provide basic widgets for both fields.

EnhancedArrayWidget is an improved ArrayWidget, using Javascript to
expand and shrink the array client side.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
This Product includes CompoundField and ArrayField. Both are fields for
use within Archetypes Products.

CompoundField
    field that itself consists of several sub-fields defined in an own
    Schema.
ArrayField
    field containing one field severals times.

It also provide basic widgets for both fields.

EnhancedArrayWidget is an improved ArrayWidget, using Javascript to
expand and shrink the array client side.

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
%doc *.txt model
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/test*
%exclude %python_sitelibdir/Products/*/*/test*

%files tests
%python_sitelibdir/Products/*/test*
%python_sitelibdir/Products/*/*/test*

%changelog
* Thu Dec 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.dev2.git20130509
- Initial build for Sisyphus

