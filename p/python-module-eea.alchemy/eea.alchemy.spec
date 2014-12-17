%define mname eea
%define oname %mname.alchemy
Name: python-module-%oname
Version: 6.0
Release: alt1.dev.git20141014
Summary: Bulk auto-discover geographical coverage, temporal coverage, keywords and more
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/eea.alchemy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/eea/eea.alchemy.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-BeautifulSoup4
BuildPreReq: python-module-eea.faceted.vocabularies
BuildPreReq: python-module-collective.js.jqueryui
BuildPreReq: python-module-eea.relations
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.CMFDefault
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.uuid
BuildPreReq: python-module-plone.app.form
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.app.controlpanel
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.pagetemplate
BuildPreReq: python-module-zope.browser
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname eea.faceted.vocabularies collective.js.jqueryui
%py_requires eea.relations Products.CMFCore Products.Archetypes
%py_requires Products.GenericSetup Products.statusmessages plone.uuid
%py_requires Products.CMFDefault plone.app.layout plone.app.form
%py_requires plone.registry plone.app.controlpanel zope.schema
%py_requires zope.component zope.interface zope.pagetemplate
%py_requires zope.browser zope.formlib zope.i18nmessageid

%description
Auto-discover geographical coverage, temporal coverage, related items
and keywords from documents common metadata (title, description, body,
etc), auto highlight keywords within a page content based on selected
tags and auto-update related items based on internal links found within
object's metadata.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
Auto-discover geographical coverage, temporal coverage, related items
and keywords from documents common metadata (title, description, body,
etc), auto highlight keywords within a page content based on selected
tags and auto-update related items based on internal links found within
object's metadata.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
install -d %buildroot%python_sitelibdir/%mname
cp -fR %mname/alchemy %buildroot%python_sitelibdir/%mname/
cp -fR *.egg-info %buildroot%python_sitelibdir/

%check
python setup.py test

%files
%doc *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0-alt1.dev.git20141014
- Initial build for Sisyphus

