%define oname Products.Marshall
Name: python-module-%oname
Version: 2.1.5
Release: alt1.dev0.git20150211
Summary: Configurable Marshallers for Archetypes
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.Marshall/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/Products.Marshall.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-transaction
BuildPreReq: python-module-plone.uuid
BuildPreReq: python-module-zope.contenttype
BuildPreReq: python-module-zope.deprecation
BuildPreReq: python-module-Products.Archetypes-tests
BuildPreReq: python-module-Products.CMFCore-tests
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests
BuildPreReq: python-module-Products.ATContentTypes-tests
BuildPreReq: python-module-WebDAV
BuildPreReq: python-module-plone.app.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone.uuid zope.contenttype zope.deprecation zope.interface
%py_requires Products.Archetypes Products.CMFCore Products.GenericSetup

%description
People coming to Plone from other CMS or from no CMS at all often want
to be able to bulk import existing content. There are also cases of
sites which produce a high volume of content that needs to be published
constantly.

The easiest way to achieve the goal of allowing import/export of
structured content currently is through introspectable schemas.
Archetypes provides this right now. However, Archetypes expects a schema
to have only one marshaller component, and the default ones are not able
to marshall all the facets of a complex piece of content by themselves.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.component.testing zope.security.testing
%py_requires Products.ATContentTypes.tests Products.Archetypes.tests
%py_requires Products.CMFCore.testing plone.app.testing

%description tests
People coming to Plone from other CMS or from no CMS at all often want
to be able to bulk import existing content. There are also cases of
sites which produce a high volume of content that needs to be published
constantly.

The easiest way to achieve the goal of allowing import/export of
structured content currently is through introspectable schemas.
Archetypes provides this right now. However, Archetypes expects a schema
to have only one marshaller component, and the default ones are not able
to marshall all the facets of a complex piece of content by themselves.

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
%doc *.txt docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.5-alt1.dev0.git20150211
- Version 2.1.5.dev0

* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.4-alt1.dev0.git20140416
- Initial build for Sisyphus

