%define mname collective
%define oname %mname.phantasy
Name: python-module-%oname
Version: 2.7
Release: alt1.dev0.git20150119
Summary: Dynamic theme for Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.phantasy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.phantasy.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-nose
BuildPreReq: python-module-Products.FCKeditor
BuildPreReq: python-module-archetypes.schemaextender
BuildPreReq: python-module-Products.SmartColorWidget
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.validation
BuildPreReq: python-module-Products.ResourceRegistries
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.FCKeditor archetypes.schemaextender
%py_requires Products.SmartColorWidget Products.Archetypes plone.memoize
%py_requires Products.CMFCore Products.ATContentTypes Products.CMFPlone
%py_requires Products.validation Products.ResourceRegistries
%py_requires plone.app.layout zope.component zope.interface
%py_requires zope.i18nmessageid

%description
Change the skin of your plone site, change the skin of any content based
on ATFolder on the site, using a simple form.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase zope.component.testing zope.testing

%description tests
Change the skin of your plone site, change the skin of any content based
on ATFolder on the site, using a simple form.

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
nosetests -v

%files
%doc *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7-alt1.dev0.git20150119
- Initial build for Sisyphus

