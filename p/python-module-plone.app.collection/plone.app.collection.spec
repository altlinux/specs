%define oname plone.app.collection

Name: python-module-%oname
Version: 1.1.2
Release: alt2.dev0.git20140826
Summary: This package adds 'saved search' functionality to Plone
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.collection/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.collection.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.app.contentlisting
BuildPreReq: python-module-plone.app.form
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.app.querystring
BuildPreReq: python-module-plone.app.vocabularies
BuildPreReq: python-module-plone.app.widgets
BuildPreReq: python-module-plone.portlet.collection
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFQuickInstallerTool
BuildPreReq: python-module-Products.validation
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.ATContentTypes

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.formlib zope.i18nmessageid zope.interface zope.schema
%py_requires Products.CMFQuickInstallerTool Products.validation
%py_requires plone.portlet.collection plone.portlets Products.CMFCore
%py_requires plone.app.vocabularies plone.app.widgets zope.component
%py_requires plone.app.portlets plone.app.querystring zope.configuration
%py_requires plone.app plone.app.contentlisting plone.app.form
%py_requires Products.Archetypes Products.CMFPlone

%description
Collections in Plone are the most powerful tool content editors and site
managers have to construct navigation and site sections.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing
%py_requires Products.ATContentTypes

%description tests
Collections in Plone are the most powerful tool content editors and site
managers have to construct navigation and site sections.

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
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt2.dev0.git20140826
- Added necessary requirements
- Enabled testing

* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.dev0.git20140826
- Initial build for Sisyphus

