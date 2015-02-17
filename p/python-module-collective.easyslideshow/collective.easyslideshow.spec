%define mname collective
%define oname %mname.easyslideshow
Name: python-module-%oname
Version: 3.0
Release: alt1.git20150206
Summary: An easy slideshow solution for Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.easyslideshow/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.easyslideshow.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-collective.autopermission
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-collective.testcaselayer
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-plone.app.vocabularies
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.folder
BuildPreReq: python-module-plone.app.controlpanel
BuildPreReq: python-module-zope.app.component
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.CMFCore Products.ATContentTypes zope.schema
%py_requires Products.CMFPlone Products.statusmessages plone.indexer
%py_requires plone.app.vocabularies plone.portlets plone.app.portlets
%py_requires plone.folder plone.app.controlpanel zope.component
%py_requires zope.app.component zope.i18nmessageid zope.formlib
%py_requires zope.interface zope.annotation zope.event

%description
EasySlideshow is a Plone product that makes it easy for any content
editor to create and manage online slideshows. It comes with all the
settings you need to customize your slideshows, such as:

* Adjusting the delay between slide transitions;
* Managing the height/width of slideshow images;
* Controlling whether or not captions are shown with slides;
* Selecting whether or not users can pause the slideshow when cursor is
  hovering over the slideshow;
* Selecting slides timeout;
* Displaying navigation as numbers, titles, thumbnails, or not at all.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing collective.testcaselayer
%py_requires Products.PloneTestCase Products.Five.testbrowser

%description tests
EasySlideshow is a Plone product that makes it easy for any content
editor to create and manage online slideshows.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1.git20150206
- Initial build for Sisyphus

