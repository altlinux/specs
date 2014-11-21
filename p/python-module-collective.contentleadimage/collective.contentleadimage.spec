%define mname collective
%define oname %mname.contentleadimage
Name: python-module-%oname
Version: 1.3.6
Release: alt1.dev0.git20140430
Summary: Adds lead image to any content in plone site
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.contentleadimage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.contentleadimage.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-archetypes.schemaextender
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFDefault
BuildPreReq: python-module-Products.validation
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-plone.app.imaging
BuildPreReq: python-module-plone.app.controlpanel
BuildPreReq: python-module-plone.protect
BuildPreReq: python-module-plone.app.form
BuildPreReq: python-module-plone.app.viewletmanager
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.theme
BuildPreReq: python-module-plone.app.blob
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-Products.CacheSetup
BuildPreReq: python-module-plone.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.schema zope.formlib zope.interface zope.annotation
%py_requires plone.app.blob zope.component zope.event
%py_requires plone.app.viewletmanager plone.app.layout plone.theme
%py_requires plone.app.imaging plone.app.controlpanel plone.app.form
%py_requires Products.ATContentTypes Products.Archetypes plone.protect
%py_requires Products.CMFCore Products.CMFDefault Products.validation
%py_requires %mname archetypes.schemaextender plone.browserlayer
%py_requires plone.indexer Products.CMFPlone Products.statusmessages
%py_requires zope.i18n zope.publisher Products.CacheSetup

%description
This products adds complete support for adding descriptive image to any
Archetypes based content in Plone site. Each object has new tab "Edit
lead image", which allows to upload new or remove current image. It is
similar behaviour as Plone News Item (you can add image to news item and
this image is displayed in news item overview listing.

There is folder_leadimage_view page template, which can be used to list
all items in the folder together with images attached.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.testing

%description tests
This products adds complete support for adding descriptive image to any
Archetypes based content in Plone site. Each object has new tab "Edit
lead image", which allows to upload new or remove current image. It is
similar behaviour as Plone News Item (you can add image to news item and
this image is displayed in news item overview listing.

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
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.6-alt1.dev0.git20140430
- Initial build for Sisyphus

