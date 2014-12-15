%define oname Products.OrderableReferenceField
Name: python-module-%oname
Version: 1.3
Release: alt1.svn20110822
Summary: Provides an Archetype field that's very similiar to the Archetypes Reference field
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.OrderableReferenceField/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.plone.org/svn/archetypes/Products.OrderableReferenceField/trunk/
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.Relations
BuildPreReq: python-module-Products.ATReferenceBrowserWidget
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: %name-examples = %EVR
Requires: python-module-Zope2
%py_requires Products.Archetypes Products.Relations Products.CMFCore
%py_requires Products.ATReferenceBrowserWidget

%description
This product provides an Archetype field that's very similiar to the
Archetypes Reference field, with the addition that it stores the order
of referenced objects.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
This product provides an Archetype field that's very similiar to the
Archetypes Reference field, with the addition that it stores the order
of referenced objects.

This package contains tests for %oname.

%package examples
Summary: Examples for %oname
Group: Development/Python
Requires: %name = %EVR

%description examples
This product provides an Archetype field that's very similiar to the
Archetypes Reference field, with the addition that it stores the order
of referenced objects.

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
%doc *.txt docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests
%exclude %python_sitelibdir/Products/*/examples
%exclude %python_sitelibdir/Products/*/profiles/example

%files tests
%python_sitelibdir/Products/*/tests

%files examples
%python_sitelibdir/Products/*/examples
%python_sitelibdir/Products/*/profiles/example

%changelog
* Mon Dec 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.svn20110822
- Initial build for Sisyphus

