%define mname collective
%define oname %mname.vaporisation

%def_disable check

Name: python-module-%oname
Version: 1.3.7
Release: alt1.git20150217
Summary: Plone portlet for vaporisation tagcloud
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.vaporisation/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.vaporisation.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.app.form
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.app.search
BuildPreReq: python-module-plone.app.contentlisting
BuildPreReq: python-module-plone.app.vocabularies
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.app.schema
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.component-tests

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.CMFCore Products.Archetypes plone.app.form
%py_requires Products.CMFPlone plone.app.portlets plone.portlets
%py_requires plone.memoize plone.app.search plone.app.contentlisting
%py_requires plone.app.vocabularies zope.i18nmessageid zope.schema
%py_requires zope.interface zope.component zope.app.schema zope.event
%py_requires zope.formlib zope.lifecycleevent

%description
The collective.vaporisation addons for Plone give to the user a tag
cloud portlet.

A tag cloud (or weighted list in visual design) is a visual depiction of
keywords used into your site. Tags are usually single words and are
normally listed alphabetically, and the importance of a tag is shown
with font size. Thus, it is possible to find a tag alphabetically and by
popularity. The tags are hyperlinks that lead to a collection of
contents that are associated with a keyword. This hyperlinks makes a
Plone search that show the list of contents marked with the
keyword selected.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing Products.PloneTestCase zope.component.testing

%description tests
The collective.vaporisation addons for Plone give to the user a tag
cloud portlet.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.7-alt1.git20150217
- Initial build for Sisyphus

