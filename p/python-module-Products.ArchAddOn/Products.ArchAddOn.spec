%define oname Products.ArchAddOn
Name: python-module-%oname
Version: 1.7
Release: alt1.git20130921
Summary: Straightforward toolbox of field types, widgets, and validators for Archetypes
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.ArchAddOn/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.ArchAddOn.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFPlone python-module-unittest2
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_provides Products.CMFPlone

%description
Straightforward toolbox of field types, widgets, and validators for
Archetypes.

Please feel free to add your own new fields, widgets, and validators
here, if you think they are general-purpose. I intend for this to be not
sample or learning archetypes add ons (ArchExample is for that), but
real-world usable toolbox pieces.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.component.testing zope.security.testing
%py_requires Products.PloneTestCase

%description tests
Straightforward toolbox of field types, widgets, and validators for
Archetypes.

Please feel free to add your own new fields, widgets, and validators
here, if you think they are general-purpose. I intend for this to be not
sample or learning archetypes add ons (ArchExample is for that), but
real-world usable toolbox pieces.

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
%doc *.rst docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Tue Oct 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1.git20130921
- Initial build for Sisyphus

