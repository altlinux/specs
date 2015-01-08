%define mname collective
%define oname %mname.portlet.rich
Name: python-module-%oname
Version: 0.6
Release: alt1.dev0.git20150106
Summary: Rich-text portlet for Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.portlet.rich/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.portlet.rich.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFPlone-tests
BuildPreReq: python-module-collective.formlib.link
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-plone.app.vocabularies
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.app.form
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.app.schema
BuildPreReq: python-module-five.formlib
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname.portlet Products.CMFPlone collective.formlib.link
%py_requires Products.ATContentTypes Products.CMFCore plone.namedfile
%py_requires plone.portlets plone.i18n plone.app.vocabularies
%py_requires plone.app.portlets plone.app.form zope.interface
%py_requires zope.formlib zope.component zope.schema zope.i18nmessageid
%py_requires zope.app.schema five.formlib

%description
This is an extended version of plone.portlet.static with additional
fields suitable for display in a static text portlet:

* Image - by reference, using the USB-widget.
* Optional URL - the title is linked to this URL, if set.
* Links - a list of internal and external links may be provided; a CSS
  class name for the list output may be specified.
* Omit border
* Custom footer - with option to specify link

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase Products.CMFPlone.tests

%description tests
This is an extended version of plone.portlet.static with additional
fields suitable for display in a static text portlet:

* Image - by reference, using the USB-widget.
* Optional URL - the title is linked to this URL, if set.
* Links - a list of internal and external links may be provided; a CSS
  class name for the list output may be specified.
* Omit border
* Custom footer - with option to specify link

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
%python_sitelibdir/%mname/portlet/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/portlet/*/tests

%files tests
%python_sitelibdir/%mname/portlet/*/tests

%changelog
* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.dev0.git20150106
- Initial build for Sisyphus

