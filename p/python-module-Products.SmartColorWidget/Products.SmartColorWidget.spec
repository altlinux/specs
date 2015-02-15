%define oname Products.SmartColorWidget
Name: python-module-%oname
Version: 1.1.6
Release: alt1.dev0.git20130612
Summary: Smart color picker widget for Archetypes
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.SmartColorWidget/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.SmartColorWidget.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-zope.app.component

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone.browserlayer Products.Archetypes Products.CMFCore
%py_requires zope.app.component zope.component zope.interface

%description
SmartColorWidget is a user-friendly color picker widget for Archetypes.
It allow quick and easy color selection from 3 different ways:

* HTML color value
* Color table and lightness bar slider
* Hue/Lightness/Saturation fields

The 3 inputs modes are javascript-wired and dynamically change when
anything is modified.

%package examples
Summary: Examples for %oname
Group: Development/Python
Requires: %name = %EVR

%description examples
SmartColorWidget is a user-friendly color picker widget for Archetypes.
It allow quick and easy color selection from 3 different ways:

* HTML color value
* Color table and lightness bar slider
* Hue/Lightness/Saturation fields

The 3 inputs modes are javascript-wired and dynamically change when
anything is modified.

This package contains examples for %oname.

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
%doc *.rst docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/examples

%files examples
%python_sitelibdir/Products/*/examples

%changelog
* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.6-alt1.dev0.git20130612
- Initial build for Sisyphus

