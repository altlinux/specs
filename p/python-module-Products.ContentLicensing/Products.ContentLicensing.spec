%define oname Products.ContentLicensing
Name: python-module-%oname
Version: 1.0.5
Release: alt1.svn20071013
Summary: Content Licensing Tool
License: GPLv2+
Group: Development/Python
Url: http://svn.plone.org/svn/collective/ContentLicensing/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.plone.org/svn/collective/ContentLicensing/trunk/
Source: %name-%version.tar

BuildPreReq: python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFPlone-tests
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.contentmigration
BuildPreReq: python-module-Products.ExternalMethod
BuildPreReq: python-module-zope.app.publisher
BuildPreReq: python-module-zope.app.annotation
BuildPreReq: python-module-zope.event

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.CMFPlone Products.Archetypes Products.CMFCore
%py_requires Products.contentmigration Products.ExternalMethod
%py_requires zope.app.publisher zope.interface zope.app.annotation
%py_requires zope.event

%description
This tool is used to manage copyright licenses within plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.CMFPlone.tests

%description tests
This tool is used to manage copyright licenses within plone.

This package contains tests for %oname.

%prep
%setup

%install
install -d %buildroot%python_sitelibdir/Products/ContentLicensing
cp -fR * %buildroot%python_sitelibdir/Products/ContentLicensing/

%files
%python_sitelibdir/Products/*
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Thu Dec 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt1.svn20071013
- Initial build for Sisyphus

