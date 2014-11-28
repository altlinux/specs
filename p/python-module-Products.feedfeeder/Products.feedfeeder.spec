%define oname Products.feedfeeder
Name: python-module-%oname
Version: 2.7
Release: alt1.dev0.git20141127
Summary: Turn external feed entries into content items
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.feedfeeder/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.feedfeeder.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-feedparser python-module-BeautifulSoup4
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.app.annotation
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.CMFCore Products.statusmessages Products.CMFPlone
%py_requires Products.Archetypes Products.ATContentTypes zope.interface
%py_requires plone.app.layout zope.lifecycleevent zope.event
%py_requires zope.component zope.app.annotation zope.annotation
%py_requires zope.i18nmessageid

%description
Feedfeeder has just a few things it needs to do:

* Read in a few ATOM feeds (not too many).
* Create FeedFeederItems out of the entries pulled from the ATOM feeds.
  Any feed items that contain enclosures will have the enclosures pulled
  down and added as File items to the feed item.
* This means figuring out which items are new, which also means having a
  good ID generating mechanism.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase zope.testing

%description tests
Feedfeeder has just a few things it needs to do:

* Read in a few ATOM feeds (not too many).
* Create FeedFeederItems out of the entries pulled from the ATOM feeds.
  Any feed items that contain enclosures will have the enclosures pulled
  down and added as File items to the feed item.
* This means figuring out which items are new, which also means having a
  good ID generating mechanism.

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
%doc *.txt *.rst docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7-alt1.dev0.git20141127
- Initial build for Sisyphus

