%define oname Products.TemplateFields
Name: python-module-%oname
Version: 1.2.6
Release: alt1.dev.svn20100610
Summary: Supplies an Archetypes field useful for editing and storing Zope Page Templates
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.TemplateFields/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://svn.plone.org/svn/archetypes/Products.TemplateFields/trunk/
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.validation
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.Archetypes Products.validation

%description
This product provides two Archetype fields that store and render
templates. There's the DTMLField for DTML templates and the ZPTField for
ZPT templates.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase zope.component.testing
%py_requires zope.security.testing

%description tests
This product provides two Archetype fields that store and render
templates. There's the DTMLField for DTML templates and the ZPTField for
ZPT templates.

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
* Mon Oct 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.6-alt1.dev.svn20100610
- Initial build for Sisyphus

